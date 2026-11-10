# Images and diagram sources

[← Main proposal](../README.md)

All assets are stored in the repository so its pages do not rely on hotlinked images or a private local directory. None is an official Blizzard screenshot, logo or promotional image.

| File | Purpose | Provenance |
| --- | --- | --- |
| [a-world-of-parallel-adventures.png](images/a-world-of-parallel-adventures.png) | Cover illustrating a lasting world with several adventures | Original AI-generated illustration, built-in ImageGen, 10 November 2026 |
| [raid-progression.svg](diagrams/raid-progression.svg) | Independent update and difficulty progression | Editable, repository-authored vector diagram |
| [progression-channels.svg](diagrams/progression-channels.svg) | Equipment, Runes, scoped bonuses, abilities and recognition | Editable, repository-authored vector diagram |
| [raid-difficulties.svg](diagrams/raid-difficulties.svg) | Separate Normal/Veteran equipment and ability acquisition | Editable, repository-authored vector diagram |
| [heroic-dungeon.svg](diagrams/heroic-dungeon.svg) | Tactical, untimed five-player Heroic encounters | Editable, repository-authored vector diagram |
| [challenge-loop.svg](diagrams/challenge-loop.svg) | Normalized timed attempts, validation and free retries | Editable, repository-authored vector diagram |
| [elite-region.svg](diagrams/elite-region.svg) | Cooperative approach to a territorial World Boss | Editable, repository-authored vector diagram |
| [warfare-layers.svg](diagrams/warfare-layers.svg) | Ordinary faction PvP, city flags, territorial ownership and service | Editable, repository-authored vector diagram |
| [settlement-cycle.svg](diagrams/settlement-cycle.svg) | NPC invasion, defense outcome and cooperative village reconstruction | Editable, repository-authored vector diagram |
| [procedural-expedition.svg](diagrams/procedural-expedition.svg) | World portals, finite generated floors and checkpoint scaling | Editable, repository-authored vector diagram |
| [recognition-domains.svg](diagrams/recognition-domains.svg) | Participation ranks, competitive standings and city service | Editable, repository-authored vector diagram |
| [rune-progression.svg](diagrams/rune-progression.svg) | Finite statistics with a fixed lifetime ceiling and no Rune rank | Editable, repository-authored vector diagram |
| [adventurer-repertoire.svg](diagrams/adventurer-repertoire.svg) | Permanent raid ability collection with one equipped option | Editable, repository-authored vector diagram |
| [identity-development.svg](diagrams/identity-development.svg) | Review gates for regions, race concepts and class studies | Editable, repository-authored vector diagram |
| [world-activities.svg](diagrams/world-activities.svg) | Professions, exploration and small-group adventures | Editable, repository-authored vector diagram |
| [power-validation.svg](diagrams/power-validation.svg) | Server-side checks for the effective loadout and ranked profiles | Editable, repository-authored vector diagram |

The diagrams use fictional update scopes and conceptual encounter flow. They do not show announced game systems or geography. Each SVG includes a title and description, and consuming Markdown includes alternative text.

All diagrams share the same muted green and gold palette, rounded cards, typography and arrow conventions. The README and topic pages reuse the same SVG files; changing an asset updates both reading views through the wiki publishing workflow. Dashed elements and explicit labels identify optional branches or unsettled prototype choices.

## Cover generation prompt

Generated with the built-in ImageGen tool, without reference images. The final prompt was:

```text
Use case: stylized-concept
Asset type: wide illustrated cover for a community MMORPG game-design repository
Primary request: an original high fantasy landscape expressing a lasting world with many parallel adventures rather than ever taller power tiers.
Scene/backdrop: a panoramic ancient forest valley, weathered stone ruins, a distant mountain citadel and a glowing dungeon entrance, connected by branching footpaths.
Subject: a small group of five varied fantasy adventurers seen from behind at a crossroads, looking into the expansive world; modest travel gear and distinctive silhouettes.
Style/medium: polished painterly fantasy concept art, rich environmental storytelling, readable large shapes, restrained detail, evocative of a classic MMORPG adventure.
Composition/framing: landscape banner approximately 3:1; world fills the frame, party small in the foreground, balanced open scenery.
Lighting/mood: warm dawn, inviting exploration, deep teal shadows, muted gold light.
Constraints: original scene, no recognizable franchise characters or copied game artwork, no official logos, no interface, no writing, no lettering, no watermark.
```

## Adding or revising assets

Use `images/` for raster illustrations and `diagrams/` for editable SVGs. Prefer descriptive lowercase filenames, relative links and a short provenance entry here. Keep diagrams readable without color alone and include their information in the surrounding text.

Keep images reasonably sized for a documentation repository. Preserve editable source files when the format supports them. Do not introduce third-party promotional art or screenshots without documenting the source and applicable permission.
