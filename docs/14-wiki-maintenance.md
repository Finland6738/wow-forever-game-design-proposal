# Wiki publishing and maintenance

[← Main proposal](../README.md) · [Documentation index](README.md) · [Contributing](../CONTRIBUTING.md)

## One source, two reading views

The [GitHub Wiki](https://github.com/Finland6738/wow-forever-game-design/wiki) is generated from the repository's Markdown. Edit the repository files to change the concept. A push or merge into `main` triggers the [Sync GitHub Wiki workflow](https://github.com/Finland6738/wow-forever-game-design/actions/workflows/wiki-sync.yml).

The pipeline validates source links and section anchors, runs generator tests, rebuilds the pages and publishes a normal commit to the separate wiki Git repository. It does not rewrite gameplay decisions, invent tuning values or publish the forum draft to a forum.

## What is included

- The full README proposal, including the author's background.
- Every Markdown document under `docs/`, including newly added and nested pages.
- Root Markdown guidance and the asset notes.
- A generated Home page, a detailed topic index, a sidebar and a source-revision footer.
- Dedicated activity and identity pages, grouped into PvE, Open World, PvP/Faction Warfare, Character/Progression and Project Reference.
- Per-page section navigation, rewritten wiki links and repository-hosted illustrations.

The generator converts relative document links to wiki links while keeping code examples intact. Images refer to the exact source revision, so a published page and its illustrated state remain consistent. Links to scripts or other non-page files point back to the repository.

## Contributor workflow

1. Edit the relevant Markdown, diagrams or image assets.
2. Check local links and run `python -m unittest discover -s tests -v`.
3. Preview the generated wiki with `python scripts/sync_wiki.py --output .preview/wiki-build` if useful.
4. Submit the normal repository change. Pull requests validate and build without publishing.
5. After merge into `main`, check the workflow result and the wiki's source-revision footer.

No separate manual wiki edit is needed. Direct edits to generated pages are replaced by the next synchronization. Additional unmanaged wiki pages are preserved, but concept documentation belongs in repository Markdown so it participates in review and automatic navigation.

## Addition, rename and removal

New source documents are discovered automatically. [wiki/navigation.json](../wiki/navigation.json) assigns topic labels, categories, descriptions and stable page names such as `Raids`, `Races` and `Classes`. Topics not yet assigned to a category remain visible under Additional Topics. Default names derive from source paths; conflicting names fail validation rather than overwriting a page.

When moving content between topic sources, update incoming section links as part of the same change. Category configuration and source links are validated before publication. Project Reference can be collapsed so technical material does not obscure activity navigation.

A manifest records which wiki files the generator owns. Removed or renamed source pages remove only their previously managed output; unrelated wiki pages are left alone. Broken references to a removed source block publication until corrected.

## Authentication and publishing scope

The workflow uses the temporary repository `GITHUB_TOKEN` with explicit `contents: write` permission. It uses GitHub's own checkout action and the runner's Python/Git tooling, without a personal access token or third-party wiki-publishing action.

Publishing runs only for the repository's `main` branch or a manual run targeting `main`; pull requests receive validation only. Concurrent publications are serialized, the source revision is recorded and wiki history is updated without a force push.

## Failure and recovery

| Situation | Outcome and remedy |
| --- | --- |
| Broken local link or section anchor | Validation fails before publication; fix the source link |
| Duplicate generated page name | Choose a distinct source path; existing pages are not silently overwritten |
| GitHub rejects wiki authentication | The run fails visibly; inspect repository wiki/Actions permissions before retrying |
| Another wiki commit arrives during publication | A normal push refuses a non-fast-forward; rerun to rebuild against the latest wiki state |
| A generated page is edited manually | Move the intended change into its repository source before the next synchronization |
| No generated content changed | The publisher exits successfully without an empty commit |
| A previous source revision is restored | Its validated content can be republished through the same workflow; wiki history remains available |

The workflow also supports manual dispatch from its Actions page. Automatic synchronization depends on a functioning GitHub Actions run; a failed check must not be described as a successful update.
