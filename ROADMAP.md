# bananaintelligence.ai Roadmap

## Up next
Last refreshed: 2026-11-01

<!-- roadmap:matrix:start -->
| # | Item | Value / use case | Depends on | Owner | Status |
|---|---|---|---|---|---|
| 3 | Update the share image and its alt text to "Excellence. For everyone." | Link previews still show the old "exclusive to the elites" line and would contradict the site | none | Agent | next |
| 4 | Run the code review on the motto branch and show Nate the findings | CLAUDE.md requires a review before anything ships to the live site | #3 | Agent | blocked: #3 |
| 5 | OK to merge the motto branch to main, which deploys the live site (default: yes if the review is clean) | Visitors see the new motto, share image, and page text together | #4 | Nate | blocked: #4 |
<!-- roadmap:matrix:end -->

## Later
- Revisit the Plain Ballot line on the site after the Nov 3 election (PORTFOLIO: rethink after Nov 3)
- Refresh the DayStart line and App Store link when the next release ships (PORTFOLIO: about Nov 9)

## Shipped
| # | Item | Value / use case | Depends on | Owner | Status |
|---|---|---|---|---|---|
| 2 | Add cookieless page view counts (Vercel Web Analytics) | Shows how many visitors click through to a product | none | Agent | done 2026-10-27 |
| 1 | Real asks, a real contact section, and 44px tap targets | Visitors can get DayStart or the ballot guide, or reach Nate, in one tap | none | Agent | done 2026-10-27 |
