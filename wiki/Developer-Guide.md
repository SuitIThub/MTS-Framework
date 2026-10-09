# Developer & Modder Guide

Technical documentation for extending **the framework**. Everything here is
mod-capable: content is driven by keys, conditions, and effects, and mods register
through the same paths as the base game.

New to the project? Start with **[Modding — Quick Start](Modding)** — it walks you
from an empty folder to a working, enable-able mod, and points into the guides below.

## Getting started

1. Install the [Ren'Py SDK](https://www.renpy.org/latest.html) (the framework is
   developed against Ren'Py 8.1).
2. Open the repository root as a project in the Ren'Py launcher and press
   *Launch Project*. The bundled example content starts out of the box.
3. Put your art under `game/images/`. The framework ships only UI graphics and
   labelled placeholders (map, building sprites, backgrounds) that you replace with
   your own files under the same paths.

## Content guides

- **School levels** — the number is the `"school"` character's level (1–10). What
  each level *means* for your game is up to you; gates and image tokens are in the
  system guides below.
- **[Building Situations](Building-Situations)** — a *Situation* is an ongoing
  problem or development the player influences through a bidirectional progress bar
  and narrative hints, ending in a positive or negative resolution. This is the
  system that replaced quests. Covers bars, thresholds, passives/measures, teasers,
  event pools, resolutions, effects, hot-reload, and the full mod workflow.
- **[Building Unlockables](Building-Unlockables)** — an *Unlockable* (rule, club, or
  building unlock) is a Situation with a PTA-vote layer pre-built on top. Covers the
  injected vote/cancel/persuade measures, faction bars, money escrow, upgrade
  chains, unlock effects, and pictograms. **Read the Situations guide first** — an
  Unlockable *is* a Situation.

## System guides

The building blocks the content systems are made of:

- **[Events](Events)** — the scenes players reach by exploring; location pools,
  priorities, event flags (intro, camp), scene labels, and how everything below plugs in.
- **[Conditions](Conditions)** — the universal gating primitive (when something is
  available), with the `AND`/`OR`/`NOT` combinators and the full catalog.
- **[Value Ranges](Value-Ranges)** — the number-pattern grammar (`"3+"`, `"3-7"`,
  `"1,3,5"`) that stat, level, and time checks parse; the shared primitive behind them.
- **[Selectors](Selectors)** — dynamic values rolled at runtime into event kwargs
  (the acting character, a variant, a stat reading).
- **[Effects](Effects)** — the "what happens" actions (money, stats, unlocks,
  building open/close) and their apply/revert semantics.
- **[Modifiers](Modifiers)** — how stat changes are scaled and how recurring drift
  works; the engine behind stat/bar modifier effects.
- **[Options](Options)** — the shared trailing flags that fine-tune conditions,
  effects, selectors and events.
- **[Items & Inventory](Items-and-Inventory)** — item definitions, the save-backed
  `inventory_manager`, `ItemCondition`, the office-computer shop and deliveries,
  and the journal inventory page.
- **[Dialogue](Dialogue)** — how a `Person` becomes a speaking voice: speech modes
  (`say`/`think`/`whisper`/`shout`), the per-role styling categories, per-character
  `styleOverrides`, and the player-named Headmaster / Sam.
- **[Paperdoll](Paperdoll)** — the layered sprite compositor that puts a live,
  animatable character (body + head, changing pose/mood/mouth) on screen over a
  blurred background; general enough to display any stacked imagery.
- **[Images](Images)** — how a path string becomes a file: patterns, placeholders,
  `$` fallbacks, PNG/WebP, mod prefixes, and which helper to call from events,
  screens and classes.
- **[Maps](Maps)** — the map overview, map buildings (sprites, positions, open/close),
  extra maps and switching between them with `set_current_map`.
- **[Journal Alerts](Journal-Alerts)** — unseen journal news (new teaser,
  situation activated, …): topic registry, pending items, and the map highlight
  icon. Other journal surfaces register their own topic.

## How the pieces fit together

- **School level** is the campus climate (dress, talk, behaviour). Content
  authors define what each level means for their game; the number
  lives on the `"school"` character.
- **Situations** are the core player-guidance system (the bar + hints).
- **Unlockables** build on Situations to gate permanent unlocks behind a PTA vote.
- **Pictograms** are descriptive preview marks on bars/unlockables.
- **Events** are injected into building pools while a Situation is active.
- **Journal alerts** flag unseen journal news (new teaser, situation activated, …)
  and drive the map highlight icon; other journal pages can register their own
  topic. See [Journal Alerts](Journal-Alerts).

All of these are registered inside the start/after-load *lifecycle wave*; mods queue
their loader with `register_start_method(...)`. Image paths (thumbnails, teaser
images, pictogram icons) are auto-redirected to the active mod's folder.

## About these pages

All wiki pages are maintained in the **`wiki/` folder of the main repository** and
published with a sync script. Edit them there — not directly on the wiki — and see
the repo's `wiki/README.md` for the workflow.

Want to help? **[How to Contribute](How-to-Contribute)** — ideas and design talk go
in GitHub Discussions; bugs, wiki gaps, and concrete tasks go in Issues.
