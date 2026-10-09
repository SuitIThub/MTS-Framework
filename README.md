# MTS Framework

A Ren'Py framework for sandbox management games, extracted from *Mind the School*
with all game content removed. It gives you the systems; you bring the story, the
characters and the art.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Made with Ren'Py](https://img.shields.io/badge/Made%20with-Ren'Py%208.1-red?style=flat-square)](https://www.renpy.org/)

## What's inside

- **Map & locations** — buildings on a map, open/closed states, per-building event menus
- **Events** — prioritised event pools with conditions, selectors, image patterns,
  composite events built from fragments, and a replay gallery
- **Characters** — stat holders (school, teachers, parents, …) and `Person`s with
  tiered descriptions, dialogue speakers and a layered **paperdoll** system
- **Stats, modifiers & time** — stat levels and caps, daily/weekly/monthly modifiers,
  payroll, a seven-part day
- **Situations** — ongoing storylines driven by bidirectional bars, thresholds,
  passives/measures, teasers and resolutions
- **Unlockables & PTA** — rules, clubs and buildings unlocked through PTA votes
- **Journal** — overview, situations, characters, inventory, unlockables, gallery,
  credits and a cheat/debug page
- **Inventory & shop** — items, an office-computer shop with cart and delivery
- **Mods** — everything registers through the same mod-aware paths

## Getting started

1. Install the [Ren'Py SDK](https://www.renpy.org/release/8.1.3) (developed against 8.1.3).
2. Add this folder as a project in the Ren'Py launcher and launch it.

The framework ships a minimal example so it starts and shows how things connect:

| What | Where |
|---|---|
| Intro (school & headmaster name) | `game/scripts/intro.rpy` |
| Example student `jane_doe`, secretary `secretary` | `game/scripts/character.rpy` → `load_characters` |
| Two buildings on the map | `game/scripts/buildings/building.rpy`, `maps.rpy` |
| Example event `example_event` (School Building → Patrol) | `game/scripts/buildings/school_building.rpy` |
| Work, learn and shop actions | `game/scripts/buildings/office_building.rpy` |
| Example situation | `game/scripts/situations/situations.rpy` → `load_situations` |
| Example unlockable | `game/scripts/journal/unlockables.rpy` → `load_unlockables` |
| Example items | `game/scripts/inventory.rpy` → `load_items` |
| Stat texts | `game/scripts/stats.rpy` → `load_stats` |

Art: `game/images/` contains only UI graphics and labelled placeholders (map,
building sprites, backgrounds). Replace them with your own files under the same
paths. Set your game's name, version and links in `game/options.rpy`.

## Documentation

The developer documentation lives in [`wiki/`](wiki/Home.md) — start with the
[Developer Guide](wiki/Developer-Guide.md) and [Modding](wiki/Modding.md).

## Content note

The framework itself contains no adult content, but it was built for adult games
and keeps the matching systems (e.g. nudity levels in image patterns). Games built
on it are responsible for their own content and age gating; the default splash
screen includes an 18+ confirmation.

## License

Code and documentation: MIT. The bundled GUI artwork is CC BY 4.0. See [LICENSE](LICENSE).
