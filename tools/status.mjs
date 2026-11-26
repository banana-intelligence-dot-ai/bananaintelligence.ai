#!/usr/bin/env node
// Writes each app's status line and the hero count from data/apps.json into the pages that show them.
// Usage: node tools/status.mjs          write the pages
//        node tools/status.mjs --check  exit 1 if any page disagrees with the data (the deploy runs this)
// HTML pages mark each filled spot with <!--s:KEY-->...<!--/s-->, where KEY is "count" or an app name.
// agents.md and llms.txt are plain text for agents, so they are matched by line instead of marked.
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const { apps } = JSON.parse(readFileSync(join(ROOT, "data/apps.json"), "utf8"));
const STATUSES = new Set(["live", "beta", "paused"]);

for (const a of apps) {
  if (!STATUSES.has(a.status)) throw new Error(`${a.name}: status must be live, beta or paused`);
  if (a.line.includes("{time}") !== Boolean(a.time)) throw new Error(`${a.name}: use {time} in the line exactly when a time is set`);
  if (/[–—]/.test(a.line + (a.time ?? ""))) throw new Error(`${a.name}: no en or em dashes in copy`);
}

/** The line a visitor reads, with its time and an honest status. */
export const lineFor = a => a.line.replace("{time}", a.time ?? "") + (a.status === "beta" ? " In beta." : a.status === "paused" ? " Paused." : "");

const live = apps.filter(a => a.status === "live").length;
const beta = apps.filter(a => a.status === "beta").length;
export const count = `${live} apps live.` + (beta ? ` ${beta} in beta.` : "");

const values = { count, ...Object.fromEntries(apps.map(a => [a.name, lineFor(a)])) };
const escapeHtml = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");
const escapeRe = s => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

function fillMarks(text, file) {
  const seen = new Set();
  const out = text.replace(/<!--s:([^>]+?)-->([\s\S]*?)<!--\/s-->/g, (_, key) => {
    if (!(key in values)) throw new Error(`${file}: unknown status key "${key}"`);
    seen.add(key);
    return `<!--s:${key}-->${escapeHtml(values[key])}<!--/s-->`;
  });
  if (!seen.size) throw new Error(`${file}: no status marks found`);
  return out;
}

function fillAgentLines(text) {
  for (const a of apps) {
    const re = new RegExp(`^- ${escapeRe(a.name)}: .* ${escapeRe(a.url)}$`, "m");
    if (!re.test(text)) throw new Error(`agents.md: no product line for ${a.name}`);
    text = text.replace(re, `- ${a.name}: ${lineFor(a).replace(/’/g, "'")} ${a.url}`);
  }
  return text;
}

function fillLlmsCount(text) {
  const re = /\d+ apps live\.(?: \d+ in beta\.)?/;
  if (!re.test(text)) throw new Error("llms.txt: no app count found");
  return text.replace(re, count);
}

const FILES = {
  "index.html": fillMarks,
  "how-we-build/one-person-many-apps/index.html": fillMarks,
  "agents.md": fillAgentLines,
  "llms.txt": fillLlmsCount,
};

const check = process.argv.includes("--check");
let stale = [];
for (const [file, fill] of Object.entries(FILES)) {
  const path = join(ROOT, file);
  const before = readFileSync(path, "utf8");
  const after = fill(before, file);
  if (after === before) continue;
  if (check) stale.push(file);
  else writeFileSync(path, after);
}
if (stale.length) {
  console.error(`Status out of date in: ${stale.join(", ")}. Run node tools/status.mjs and commit.`);
  process.exit(1);
}
console.log(check ? `Status check passed: ${count}` : `Status written: ${count}`);
