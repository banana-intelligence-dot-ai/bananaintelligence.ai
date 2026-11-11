#!/usr/bin/env python3
"""Blind sets with motion: for each set, A..D get a still (X.jpg) and a frame sheet (X-frames.jpg).
Usage: blindsets.py OUT ours_dir ref_dir --seed N   (dirs hold NAME-still.jpg and NAME-frames.jpg)"""
import sys, os, json, random, subprocess, argparse
ap = argparse.ArgumentParser(); ap.add_argument('out'); ap.add_argument('ours'); ap.add_argument('refs')
ap.add_argument('--seed', type=int, default=7); ap.add_argument('--names', default='greptile,wispr,spade')
a = ap.parse_args(); rng = random.Random(a.seed); key = {}
items0 = [('ours', a.ours, 'ours')] + [(n, a.refs, n) for n in a.names.split(',')]
for s in range(1, 4):
    items = items0[:]; rng.shuffle(items); d = os.path.join(a.out, f'set{s}'); os.makedirs(d, exist_ok=True); key[f'set{s}'] = {}
    for L, (who, dr, n) in zip('ABCD', items):
        subprocess.run(['magick', os.path.join(dr, n + '-still.jpg'), '-resize', '1440x900!', '-strip', '-quality', '82', os.path.join(d, L + '.jpg')], check=True)
        subprocess.run(['magick', os.path.join(dr, n + '-frames.jpg'), '-strip', '-quality', '80', os.path.join(d, L + '-frames.jpg')], check=True)
        key[f'set{s}'][L] = who
os.makedirs(os.path.dirname(os.path.abspath(a.out)) + '/keys', exist_ok=True)
kp = os.path.join(os.path.dirname(os.path.abspath(a.out)), 'keys', os.path.basename(a.out.rstrip('/')) + '.json')
json.dump(key, open(kp, 'w'), indent=1)
print({k: [l for l, w in v.items() if w == 'ours'][0] for k, v in key.items()}, kp)
