# Contributing to the design

This repository develops an independent community game-design proposal in English. The [README](README.md) is the main entry point; [docs](docs/README.md) contains detail.

## Choose a discussion format

- Use [Discussions](https://github.com/Finland6738/wow-forever-game-design/discussions) for alternatives, player stories and open design questions.
- Use [Issues](https://github.com/Finland6738/wow-forever-game-design/issues) for a specific contradiction, missing rule, broken link or factual correction.
- Open a pull request for a concrete wording, diagram or design change.

Useful feedback describes the affected player, a specific situation, the proposed behavior, its trade-off and a way to evaluate it. For example: explain how a shared short raid becomes mandatory, then propose an acquisition rule and a pilot measurement.

## Editing conventions

1. Keep the README understandable without reading the technical pages. Put implementation detail in the relevant document and link it.
2. Preserve the agreed progression contract, or explicitly explain why you propose changing it.
3. Mark examples, tuning hypotheses and unresolved decisions clearly. Proposed features must not read as Blizzard announcements.
4. Cite direct official sources for factual game claims and update the [source register](docs/references.md).
5. Use relative links for repository files. Add meaningful alternative text to images.
6. Put images in `assets/images/`, editable diagrams in `assets/diagrams/`, and document provenance in [assets/README.md](assets/README.md).
7. Record material design decisions in [CHANGELOG.md](CHANGELOG.md).

Do not upload account information, private conversations or artwork without appropriate permission. Keep comments focused on the design and its effects on players.

## Lightweight review checklist

- Check that Markdown file links and section anchors resolve.
- Preview edited pages on GitHub and inspect diagrams at readable sizes.
- Check consistency across the README, detailed pages and forum draft.
- Confirm that new combat effects do not quietly require another update, difficulty or activity.
- Explain validation honestly: document checks do not establish game balance or engine feasibility.

For substantial changes, use a `codex/` branch or another descriptive contributor branch and a focused pull request. This is a documentation project; it does not need a build system merely to edit prose.
