# Contributing to the design

This repository develops an independent community game-design proposal in English. The [README](README.md) is the main entry point; [docs](docs/README.md) contains detail.

## Choose a discussion format

- Use [Discussions](https://github.com/Finland6738/wow-forever-game-design-proposal/discussions) for alternatives, player stories and open design questions.
- Use [Issues](https://github.com/Finland6738/wow-forever-game-design-proposal/issues) for a specific contradiction, missing rule, broken link or factual correction.
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
8. Use the established race names and English class archetypes in the catalog, with self-contained mechanic descriptions. Original alternatives remain labeled; put personal background in the author section.

## Wiki updates

Edit the repository Markdown, not the generated wiki pages. The [Sync GitHub Wiki workflow](https://github.com/Finland6738/wow-forever-game-design-proposal/actions/workflows/wiki-sync.yml) validates changes and publishes the full reading view after a merge into `main`. New documentation pages are included automatically.

Run `python -m unittest discover -s tests -v` and `python scripts/sync_wiki.py --output .preview/wiki-build` to check link rewriting, anchors and generation. These use Python's standard library. See [wiki maintenance](docs/14-wiki-maintenance.md) for naming, removed pages and recovery behavior.

## Automatic concept announcements

After wiki publication succeeds on `main`, the workflow announces changed concept sources in [Announcements](https://github.com/Finland6738/wow-forever-game-design-proposal/discussions/categories/announcements). Keep material decisions in `CHANGELOG.md`: new or edited bullets become the announcement summary. Without new bullets, the post lists the recorded commit subjects instead of inventing a design summary.

The scope includes the proposal README, design Markdown and diagram/image assets. Editorial edits inside these sources also count; the publisher does not infer semantic gameplay changes. Contributor guidance, source-reference maintenance, forum drafts, publishing documentation and code-only changes do not independently trigger a concept post.

Preview locally with `python scripts/announce_concept_changes.py --output .preview/announcement.md`. This default does not publish anything and compares against the initial configured baseline. The workflow uses the latest successfully announced ancestor as its checkpoint, links the source revision, and avoids duplicate posts after reruns. Only the explicit `--publish` option writes a Discussion.

Do not upload account information, private conversations or artwork without appropriate permission. Keep comments focused on the design and its effects on players.

## Lightweight review checklist

- Check that Markdown file links and section anchors resolve.
- Preview edited pages on GitHub and inspect diagrams at readable sizes.
- Check consistency across the README, detailed pages and forum draft.
- Confirm that new combat effects do not quietly require another update, difficulty or activity.
- Explain validation honestly: document checks do not establish game balance or engine feasibility.

For substantial changes, use a `codex/` branch or another descriptive contributor branch and a focused pull request. The lightweight publishing script handles wiki generation; ordinary prose remains directly editable Markdown.
