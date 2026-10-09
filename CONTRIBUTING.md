# Contributing to the MTS Framework

Thanks for wanting to help. This repo is the framework's source and the source of
the developer wiki. You do **not** need to write code to contribute — ideas, bug reports,
and wiki pages all count.

Treat other people in Issues, Discussions, and PRs with the same respect you'd want in a small workshop, not a comment section.

## Where things go

| What you have | Where it belongs |
|---|---|
| An idea, a design question, a "what if we…" | [Discussions](../../discussions) |
| Open-ended talk (lore, systems, player experience) | [Discussions](../../discussions) |
| A bug you can reproduce | [Issues](../../issues) |
| A concrete wiki gap or correction | [Issues](../../issues) |
| A specific, implementable task | [Issues](../../issues) |
| A finished change (code, wiki, docs) | A pull request |
| A standalone mod | Keep it in `game/mods/<YourMod>/` and [ship the folder](wiki/Modding.md) — do not open a PR for it |

**Discussions** are for thinking out loud. **Issues** are for work that should get
done. If you are not sure yet, start a Discussion. When the idea is sharp enough to
act on (a bug, a wiki page to write, a change with a clear shape), open an Issue and
link the Discussion.

Search existing Discussions and Issues before opening a new one.

## Reporting a bug

Use the **Bug report** issue template and include:

- Framework version, or the git branch / commit
- OS
- Steps to reproduce, and what you expected instead
- Whether any mods were enabled
- `traceback.txt` and/or `log.txt` from the game folder when Ren'Py throws

A short, reproducible report is more useful than a long one.

## Wiki

The GitHub Wiki is **authored in this repo**, in the `wiki/` folder — not in the
Wiki tab's web editor. Edit the markdown here and send a PR. Maintainers publish it
with the sync script (`wiki/README.md`).

If you want to **propose** a wiki expansion (new page, missing section, wrong API)
without writing it yourself, open an Issue and say which page and what is missing.

When you **write** the page:

1. Add `wiki/My-Page.md` (hyphens for spaces in the filename).
2. **No `# H1`** — GitHub uses the filename as the title.
3. Cross-page links look like `[Events](Events)`, not a `.md` path.
4. Link the page from `wiki/_Sidebar.md` (and `wiki/Home.md` if it belongs on the landing page).
5. Point "Related files" at the real `game/scripts/…` sources.

Developer system guides live next to this file in `wiki/` ([Events](wiki/Events.md),
[Building Situations](wiki/Building-Situations.md), [Modding](wiki/Modding.md), …).
Read the matching page before changing the system it documents.

## Development setup

1. **Ren'Py 8.1.3** — [download](https://www.renpy.org/release/8.1.3). Newer 8.1.x may
   work; use 8.1.3 if something breaks.
2. **Clone** this repository.
3. Add the project in the Ren'Py launcher and run it once. The bundled example
   content should start without errors.

## Pull requests

1. Fork (or branch, if you have write access).
2. Keep the PR focused — one problem or one wiki page family, not a mixed bag.
3. Match the style of the surrounding `.rpy` / markdown. Do not reformat files you
   did not need to change.
4. Test the path you touched in the running game when the change is playable.
5. Describe **why** the change exists and how you checked it. Link the Issue if there
   is one.
6. Do not commit secrets or generated junk (see below).

New game content that is meant to stay optional should be a **mod**, not a core PR.
See [Modding — Quick Start](wiki/Modding.md). `game/mods/*` is gitignored except for
the bundled CheatMod, so a personal mod will not show up in a PR anyway.

## Do not commit

- `game/saves/`, `game/cache/`, compiled `.rpyc` files
- `.env` or other credentials
- `log.txt`, `traceback.txt`, `errors.txt`
- Personal mods under `game/mods/` (except changes to the bundled CheatMod)
- Game-specific content or art — the framework stays blank

## License

- **Code and docs in this repository:** MIT (see `LICENSE`)
- **Bundled GUI artwork:** CC BY 4.0

By opening a PR you offer the change under the same licenses.

## Questions

Unsure where a thought belongs? Open a Discussion. That is the right default.
