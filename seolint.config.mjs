// SEO check for the live site. This repo is the site (no build step), so it reads the HTML in place.
// Vercel runs it on every deploy (buildCommand in vercel.json), so an error fails the deploy.
// Run it yourself first: npx -y seolint@1.1.1  (errors must be zero; warnings are reported).
export default {
  host: "https://bananaintelligence.ai",
  inputs: ["."],
  ignore: [
    "daystart/**",     // DayStart's legal pages, served and canonical on daystart.bananaintelligence.ai
    "Homepage/**",     // local design files, not deployed pages
    "Email Icons/**",
    "node_modules/**",
  ],
};
