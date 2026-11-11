#!/usr/bin/env python3
"""Record a page the same way every time: 4 s of hero (pointer drifts across it), then a
smooth wheel scroll down about 3.5 screens. Writes NAME.mp4 (trimmed to start at first
paint), NAME-still.jpg (hero at 4 s) and NAME-frames.jpg (12-frame sheet, time-stamped).

Usage: record.py OUT name=url [...] [--root DIR --swap "a=>b"] [--reduced] [--dark]
"""
import argparse, os, shutil, subprocess, time, mimetypes
from urllib.parse import urlparse, unquote
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument('out'); ap.add_argument('pages', nargs='+')
ap.add_argument('--root'); ap.add_argument('--swap', action='append', default=[])
ap.add_argument('--reduced', action='store_true'); ap.add_argument('--dark', action='store_true')
ap.add_argument('--hold', type=float, default=4.0); ap.add_argument('--screens', type=float, default=3.5)
a = ap.parse_args()
a.out = os.path.abspath(a.out); os.makedirs(a.out, exist_ok=True)
W, H = 1440, 900

def serve(route):
    path = unquote(urlparse(route.request.url).path)
    f = os.path.join(a.root, path.lstrip('/'))
    if os.path.isdir(f): f = os.path.join(f, 'index.html')
    if not os.path.exists(f) and os.path.exists(f + '.html'): f += '.html'
    if os.path.exists(f) and f.endswith('.html'):
        body = open(f, encoding='utf-8').read()
        for sw in a.swap:
            o, n = sw.split('=>', 1); body = body.replace(o, n)
        route.fulfill(body=body, content_type='text/html; charset=utf-8')
    elif os.path.exists(f):
        route.fulfill(path=f, content_type=mimetypes.guess_type(f)[0] or 'application/octet-stream')
    else:
        route.fulfill(status=404, body='')

with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome', headless=True, args=['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist', '--autoplay-policy=no-user-gesture-required'])
    for item in a.pages:
        name, url = item.split('=', 1)
        tmp = os.path.join(a.out, '_vid_' + name)
        ctx = b.new_context(viewport={'width': W, 'height': H}, device_scale_factor=1,
                            color_scheme='dark' if a.dark else 'light',
                            reduced_motion='reduce' if a.reduced else 'no-preference')
        if a.root: ctx.route('http://site.test/**', serve)
        pg = ctx.new_page()
        os.makedirs(tmp, exist_ok=True)
        frames = []
        cdp = ctx.new_cdp_session(pg)
        def on_frame(ev):
            import base64
            fp = os.path.join(tmp, f'{len(frames):05d}.jpg')
            open(fp, 'wb').write(base64.b64decode(ev['data']))
            frames.append((ev['metadata']['timestamp'], fp))
            try: cdp.send('Page.screencastFrameAck', {'sessionId': ev['sessionId']})
            except Exception: pass
        cdp.on('Page.screencastFrame', on_frame)
        cdp.send('Page.startScreencast', {'format': 'jpeg', 'quality': 80, 'maxWidth': W, 'maxHeight': H, 'everyNthFrame': 1})
        t0 = time.time()
        try:
            pg.goto(url, wait_until='domcontentloaded', timeout=45000)
        except Exception as e:
            print(name, 'goto', e)
        # dismiss obvious cookie banners without accepting tracking
        for sel in ['button:has-text("Decline")', 'button:has-text("Reject")', 'button:has-text("Necessary only")']:
            try:
                if pg.locator(sel).first.is_visible(timeout=300): pg.locator(sel).first.click(timeout=800); break
            except Exception: pass
        t_paint = time.time() - t0
        pg.mouse.move(W * 0.2, H * 0.55)
        hold_start = time.time()
        # pointer drifts across the hero
        steps = 40
        for i in range(steps):
            pg.mouse.move(W * (0.2 + 0.6 * i / steps), H * (0.55 - 0.15 * (i / steps)))
            pg.wait_for_timeout(int(a.hold * 1000 / steps))
        pg.screenshot(path=os.path.join(a.out, name + '-still.jpg'), type='jpeg', quality=88)
        # smooth wheel scroll
        total = int(H * a.screens); done = 0
        while done < total:
            pg.mouse.wheel(0, 60); done += 60; pg.wait_for_timeout(55)
        pg.wait_for_timeout(1200)
        try: cdp.send('Page.stopScreencast')
        except Exception: pass
        ctx.close()
        mp4 = os.path.join(a.out, name + '.mp4')
        # screencast frames arrive only on change: hold each until the next one (concat demuxer)
        start = frames[0][0] if frames else 0
        lst = os.path.join(tmp, 'list.txt')
        with open(lst, 'w') as L:
            for i, (ts, fp) in enumerate(frames):
                nxt = frames[i + 1][0] if i + 1 < len(frames) else ts + 0.5
                L.write(f"file '{fp}'\nduration {max(0.016, nxt - ts):.4f}\n")
            L.write(f"file '{frames[-1][1]}'\n")
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-vf', 'fps=30,scale=1280:-2', '-c:v', 'libx264', '-crf', '28', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-an', mp4], check=True)
        shutil.rmtree(tmp, ignore_errors=True)
        # 12-frame sheet with time stamps
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4], capture_output=True, text=True).stdout.strip() or 0)
        times = [0.3, 0.8, 1.5, 2.5, 3.5] + [a.hold + 0.5 + i * (dur - a.hold - 1.0) / 6 for i in range(7)]
        fd = os.path.join(a.out, '_f_' + name); os.makedirs(fd, exist_ok=True)
        for i, t in enumerate(times):
            fp = os.path.join(fd, f'{i:02d}.jpg')
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{min(t, dur - 0.05):.2f}', '-i', mp4, '-frames:v', '1', '-vf', f"scale=640:-2,drawtext=text='{t:.1f}s':x=10:y=10:fontsize=22:fontcolor=white:box=1:boxcolor=black@0.6", fp], check=True)
        subprocess.run(['magick', 'montage', *sorted(os.path.join(fd, f) for f in os.listdir(fd)), '-tile', '4x3', '-geometry', '+4+4', '-background', '#888', os.path.join(a.out, name + '-frames.jpg')], check=True)
        shutil.rmtree(fd, ignore_errors=True)
        print(name, f'paint {t_paint:.1f}s', f'dur {dur:.1f}s', os.path.getsize(mp4) // 1024, 'KB')
    b.close()
