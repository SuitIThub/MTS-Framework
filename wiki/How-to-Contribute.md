This page is the short version of how to help. The full checklist (setup, pull
requests, what not to commit) lives in
`CONTRIBUTING.md` in the
repository root.

You do **not** need to write code. Ideas, bug reports, and wiki pages all count. The
game is **18+**; contributors must be adults.

## Where things go

| What you have | Where it belongs |
|---|---|
| An idea, a design question, a "what if we…" | [Discussions](../discussions) |
| Open-ended talk (lore, systems, player experience) | [Discussions](../discussions) |
| A bug you can reproduce | [Issues](../issues) |
| A concrete wiki gap or correction | [Issues](../issues) |
| A specific, implementable task | [Issues](../issues) |
| A finished change (code, wiki, docs) | A pull request against the repo |
| A standalone mod | Follow [Modding](Modding) and ship the folder — not a PR |

**Discussions** are for thinking out loud. **Issues** are for work that should get
done. If you are not sure yet, start a Discussion. When the idea is sharp enough to
act on, open an Issue and link the Discussion.

Search first. GitHub is what we can still find in six months.

## Wiki edits

This wiki is **authored in the main repo**, in the `wiki/` folder. Do **not** edit
pages in the GitHub Wiki web UI — those changes are overwritten on the next sync.

- Propose a missing page or a wrong section as an **Issue** (which page, what is
  missing).
- Write the change in `wiki/` and open a **pull request**.
- New page: `My-Page.md` (hyphens for spaces), **no `# H1`**, links like
  `[Events](Events)`, and a line in [_Sidebar](_Sidebar).
- Character cards: drop files into `wiki/characters/<Name>/` unchanged. Never rename,
  recompress, or open-and-save them. Page `<img>` tags use the generated
  `*.preview.png`; the link around them stays on the original file. See the
  repo's `wiki/README.md`.

System guides to read before changing the thing they document: [Developer
Overview](Developer-Guide), [Events](Events), [Building Situations](Building-Situations),
[Building Unlockables](Building-Unlockables), [Modding](Modding).

## Code and mods

Clone the repo, install [Ren'Py 8.1.3](https://www.renpy.org/release/8.1.3), then add
the project in the Ren'Py launcher.

Keep PRs focused. Match surrounding style. Do not commit
`game/images/`, saves, `.env`, or personal mods — `game/mods/*` is gitignored except
for CheatMod.

New optional content belongs in a mod, not in core. See [Modding](Modding).
