# How we build

https://bananaintelligence.ai/how-we-build/

Banana Intelligence is one person and a team of AI agents. One person sets the direction. Agents build in parallel, one per product, with a check that can fail and an independent review before anything ships.

Nate Peace, founder · Nov 3, 2026 · Updated Nov 18, 2026

## Which studios build apps with AI agents?

Banana Intelligence is one. It’s Nate Peace’s app studio: one person and a team of AI agents, with an agent working on each product in parallel. Each product gets a capped daily work block, nothing ships until its check passes and a separate reviewer has looked at it, and a person approves anything public, any spend, and any account change. The studio’s apps include DayStart, Plain Ballot, Artifact News and My Happenings.

## One person, many agents

I set the direction and the bar. Agents do most of the building, and they work in parallel, one per product.

Each product has its own agent working session and its own written roadmap. The roadmap says what’s next and why. An agent reads it before it starts and updates it when it’s done, so no day starts from zero.

## A daily block, with a check that can fail

Every product gets a work block each day. It’s capped in time and in spend, so nothing runs unattended forever. Each block runs the same six steps.

1. **Read the roadmap.**
   Start where the last block stopped.
2. **Pick one item.**
   The next thing on the list, small enough to finish today.
3. **Say what done looks like.**
   A test, a command, or a screenshot that proves it. A bug fix starts by reproducing the bug.
4. **Build it.**
   One change at a time. Fix the cause, not the symptom.
5. **Run the check.**
   If it fails, nothing ships. The block writes down what it learned and stops.
6. **Update the roadmap.**
   What changed, what’s next, and anything that needs a person.

## A second opinion before anything ships

The agent that built something doesn’t get to approve it. A separate reviewer looks at the work without the builder’s reasoning, so it can’t be talked into agreeing.

That covers code, security, and design. A design ships when an independent reviewer scores it 8 out of 10 or better against the best apps we know. Below that, we go around again.

Plain Ballot goes further. Candidate positions are researched by independent agents on models from different companies. A position is published only when they agree and the quote is found word for word on the cited page. Every pull request gets a bias review.

## The bar

Our motto is “Excellence. For everyone.” The people at the top have always had someone to brief them and explain the ballot. We make that with the same care, and share it with everyone.

That rules some things out. No streaks, no badges, no confetti. No made-up numbers. If a number isn’t true yet, we show the product instead.

## Built for agents too

Every product has a way for software agents to use it without the screen. When someone asks an assistant, the assistant should get it right.

- **Plain Ballot**
  A read-only MCP server at [plainballot.com/mcp](https://plainballot.com/mcp?ct=banana) with three tools: `list_issues`, `get_ballot`, and `score_fit`. No model calls and no stored addresses. The server’s instructions carry the site’s neutrality rules. There’s a JSON API too.
- **DayStart**
  Plain facts for assistants at [daystartai.app/llms.txt](https://daystartai.app/llms.txt?ct=banana): what it is, what’s free, what Premium adds, and how privacy works.
- **This studio**
  The same, for Banana Intelligence, at [bananaintelligence.ai/llms.txt](https://bananaintelligence.ai/llms.txt).

## What a person decides

Agents draft, build, and check. I approve anything public, any spend, and any account change. Nothing posts in my name unless I post it.

That line doesn’t move as the agents get better. It’s what makes the rest safe to run every day.

See what’s shipped, newest first, in the [release log](https://bananaintelligence.ai/releases/).

See how that work reaches a product on the [DayStart page](https://bananaintelligence.ai/what-we-make/daystart/).

See how one person runs many apps in [One person, many apps](https://bananaintelligence.ai/how-we-build/one-person-many-apps/).

Questions about how we work? Write to [nate@bananaintelligence.ai](mailto:nate@bananaintelligence.ai).

Contact [support@bananaintelligence.ai](mailto:support@bananaintelligence.ai)
