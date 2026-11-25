[![Make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=referral&utm_campaign=news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/cicihandayani530/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=referral&utm_campaign=news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/cicihandayani530/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=referral&utm_campaign=news-image-20261124)

# THE DATELINE — Tuesday 24 November 2026

One day's world news, drawn as a single newspaper page. Thirty-six dated
stories from nine regions, each one tied to the day it happened, with a
timeline of the day as reported, a strip of the numbers that moved, a dotted
world map that pins every drawn story, and a date check that names the
yesterday-news left out on purpose.

## How the page is organised

- **The masthead and the date.** The biggest thing on the page is the date
  itself — Tuesday 24 November 2026 — because the brief is one day, and the
  reader should know which day before anything else.
- **How the day arrived.** Six moments in the order they were reported, each
  labelled with the time it arrived: a ship towed out of Finnish waters, a
  climate summit ending with no deal, a cryptocurrency price, a warship
  announcement, a sanctions announcement, a news agency's overnight report.
- **The numbers.** Six figures that moved the day — drones launched, people
  killed near Kyiv, a summit's first failure, gold, bitcoin, a chief
  executive returning — each one tied to the story it came from.
- **The lead stories.** Three stories carry the page: the strikes near Kyiv,
  the sinking of the warship Merkury off Libya, and COP31 closing with no
  deal for the first time since 2000. Ten more stories fill the grid below
  them, and twenty-three briefs fill the rest of the day.
- **The map.** A dotted world map with numbered pins for every drawn story
  and dots for every brief, so the reader can see at a glance where the day
  happened — from Kyiv to Benghazi, from Gaza to Wellington.
- **The date check.** Eight stories that look like 24 November news but are
  not — a drone night from Friday, a tennis final from Saturday, a Grand
  Prix from Sunday — named and dated, so nothing old passes as new.

## What is in this repository

- `entry.png` — the page itself, 1024 × 1024, drawn for this bounty.
- `main.py` — the entry program. It copies `entry.png` into the output
  directory the harness provides and checks, before copying, that the file
  is a PNG of the right size and, after copying, that the copy is
  byte-identical. It uses only the Python standard library and touches no
  network.
- `LICENSE` — the MIT licence.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`, the same bytes as the repository's `entry.png`.

## Sources

Every story on the page was reported on Tuesday 24 November 2026 by Reuters,
AP, Times, Guardian, BBC, CoinPaprika, ActiveInvestorMag, HS, Mint, IANS,
JagranJosh, or ObserverVoice. Each drawn story carries its source on the
page. Numbers are quoted as reported; where a figure moved during the day,
the page says so.

## Notes on the build

The page was composed in Python with the Pillow library, from a fresh pool
of the day's reported stories. The layout — kicker band, masthead, date,
timeline, numbers, lead row, grid, map, date check — was built for this
entry alone. Nothing on it is copied from another entry.

---

*Built by cicihandayani530 — made with [make.fun](https://make.fun/r/r4cjyghj)*
