// Serves the Markdown version of a page when a request asks for it with
// "Accept: text/markdown". The choice is made on the Accept header only.
// It never looks at the user agent. Every other request gets the HTML page.
//
// Why this file exists: on Vercel, a file on disk wins over a vercel.json
// rewrite, so a rewrite from "/" to "/index.md" never runs. This runs first.
//
// PAGES must match PAGES in tools/build-markdown.py. tools/verify-markdown.py
// fails if the two lists differ.
const PAGES = [
  "/",
  "/how-we-build/",
  "/how-we-build/one-person-many-apps/",
  "/what-we-make/",
  "/what-we-make/louie/",
  "/what-we-make/daystart/",
  "/what-we-make/artifact-news/",
  "/what-we-make/my-happenings/",
  "/what-we-make/plain-ballot/",
  "/what-we-make/politicians-by-jev/",
  "/what-we-make/spooky-particles/",
  "/releases/",
];

export const config = {
  matcher: ["/", "/how-we-build/:path*", "/what-we-make/:path*", "/releases/:path*"],
};

const pass = () => new Response(null, { headers: { "x-middleware-next": "1" } });

// True when the Accept header lists text/markdown and does not rule it out with q=0.
function wantsMarkdown(accept) {
  for (const part of accept.toLowerCase().split(",")) {
    const [type, ...params] = part.split(";").map((s) => s.trim());
    if (type !== "text/markdown") continue;
    const q = params.find((p) => p.startsWith("q="));
    return !q || parseFloat(q.slice(2)) > 0;
  }
  return false;
}

export default function middleware(request) {
  const url = new URL(request.url);
  if (url.hostname.startsWith("daystart.")) return pass();
  const path = url.pathname.endsWith("/") ? url.pathname : url.pathname + "/";
  if (!PAGES.includes(path)) return pass();
  if (!wantsMarkdown(request.headers.get("accept") || "")) {
    return new Response(null, { headers: { "x-middleware-next": "1", Vary: "Accept" } });
  }
  return new Response(null, {
    headers: {
      "x-middleware-rewrite": new URL(path + "index.md", url).toString(),
      "Content-Type": "text/markdown; charset=utf-8",
      "X-Robots-Tag": "noindex",
      Vary: "Accept",
    },
  });
}
