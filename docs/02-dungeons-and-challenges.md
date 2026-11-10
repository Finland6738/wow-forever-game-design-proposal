# Heroic dungeons and keyless Challenge Modes

[← Main proposal](../README.md) · [Documentation index](README.md) · [Technical rules](04-technical-framework.md)

## Two activities with different purposes

Heroic dungeons provide untimed, tactical five-player adventures and accessible permanent equipment. Challenge Modes provide normalized timed competition, mastery and prestige. A player can enjoy either activity without following the other's reward track.

| Property | Level-60 Heroic | Challenge Mode |
| --- | --- | --- |
| Entry | Level 60; reasonable baseline preparation | Level 60; approved normalized loadout available immediately |
| Group | Five players | Five players; roster fixed during a ranked attempt |
| Pace | Deliberate pulls, recovery and exploration | A timed run with explicit start and completion conditions |
| Equipment | Lasting baseline and budgeted sidegrades | Versioned, normalized profiles and effect rules |
| Rewards | Baseline equipment alternatives, recipes, materials, collections | Medals, records, cosmetics and other prestige |
| Difficulty growth | Fixed encounter design | Fixed encounter design and faster completion targets |
| Access resource | No proposed consumable entry requirement | No keys, charges or consumable entry items |

Both are proposals. The familiar names express design intent, rather than confirmation that these modes exist in Forever.

## A third format: procedural expeditions

The [procedural-expedition proposal](07-procedural-expeditions.md) adds a separate untimed activity for 5–20 level-60 players. Open-world portals lead to generated routes, varied packs/bosses and a committed depth of 1–5 floors. It does not change the five-player Heroic or Challenge format above, and random seeds do not share a universal timed leaderboard. Gold/material reward rates and finite floor scaling need their own evaluation.

## Heroic design goals

The long-term ambition is to revisit the existing leveling dungeon catalog at level 60 while preserving its leveling versions. A conversion needs actual encounter work: rescaling health and damage alone is insufficient.

Preserve recognizable routes, atmosphere and enemy groups. Add packs only where they improve pacing or decision-making. Rework trash abilities and add a small number of meaningful boss mechanics. Long, branching dungeons may need clearly defined wings rather than forcing every group into a marathon.

The intended tactical vocabulary includes crowd control, target priority, interrupt rotations, dispels, line of sight, threat management, defensive cooldowns and resource recovery. Telegraph dangerous actions through readable animations, audio and combat feedback.

### Example: a four-enemy pack

| Enemy | Threat | Possible answers |
| --- | --- | --- |
| Healer | Restores allies with an interruptible spell | Interrupt, control or focus damage |
| Summoner | Completes a ritual that adds reinforcements | Interrupt, displace where supported, or eliminate quickly |
| Guardian | Pressures the tank and punishes careless positioning | Mitigation, threat control and positioning |
| Scout | Escapes toward another group | Slow, root, stun or kill before escape |

One group might control the healer and interrupt the summoner. Another might burst the healer and restrain the scout. Tune for several viable compositions rather than requiring one specific class ability. Use diminishing returns and immunity rules consistently and explain them.

Not every pack should have four simultaneous priorities. Alternate demanding pulls with simpler encounters and provide reasonable recovery opportunities. Difficulty created by readable choices is more sustainable than constant attrition or surprise wipes.

## Heroic rewards and access

Questing, professions and other non-raid activities remain parallel routes to the permanent baseline. Heroics can be a convenient preparation path without becoming the only valid path or a requirement to collect every dungeon's set.

Equipment offers role-appropriate stat profiles and capped sidegrades. Recipes, materials, appearances and collections support repeated visits. A universally superior permanent trinket would undermine this model even if its item level matched other items.

Determine normal loot cadence separately from access to play. Controls on reward exploitation must not be disguised as Challenge Mode attempt limits. Avoid mandatory daily currency chains linking Heroics to Veteran progression.

## Challenge Mode rules

The inspiration is the original MoP philosophy: normalized dungeon runs measured against time targets. Blizzard's historical discussion emphasizes normalized challenge and the effect of class/itemization changes on fairness. See [sources](references.md). The following detailed rules are proposed here.

1. Any level-60 five-player group can enter without a key or consumed entry resource.
2. The group chooses a dungeon, reviews its objectives and normalized loadout, and confirms readiness.
3. The server validates the roster, establishes the ruleset version, initializes resources and starts the timer atomically.
4. Completion requires all specified bosses and encounter objectives, including an enemy-completion threshold only where that is suitable for the dungeon.
5. Bronze, Silver and Gold targets reward completion milestones. Personal records and per-dungeon leaderboards support further mastery.
6. Retries are unlimited. The group can reset, change its route or composition, and immediately begin another attempt.
7. Rewards provide no permanent or contextual raid-power progression.

There are no infinitely scaling levels, rotating affixes, key depletion or weekly raid-equivalent equipment rewards. Adding another difficulty treadmill would contradict the purpose of this activity.

## Normalize effective power, not just item level

For the competitive pilot, provide accessible approved equipment templates with role-appropriate stat distributions and bounded effect choices. Owned items can map to those same profiles, but an old raid item must not unlock a stronger Challenge option unavailable to a new competitor.

This sacrifices some unrestricted equipment experimentation in exchange for a more credible competition environment. Preserve choices in stat profiles, talents and approved effects where balance permits. Templates do not make classes identical, and class diversity still requires monitoring.

Specify weapon damage, armor, primary/secondary stats, caps, procs, set effects, enchants, consumables, profession benefits and pets. Disable all contextual raid bonuses and external territorial buffs. Either normalize relevant permanent unlocks to the profile or make their equivalent available within the mode.

If a previously unknown effect appears, use an approved replacement or prevent a ranked start with a clear explanation. Do not silently leave an unreviewed item at full power.

## Party changes, disconnects and resets

Groups may remove and replace participants freely **between attempts**, without losing an entry resource. A different participant joining an active ranked run invalidates that run for rankings. The group can restart immediately or continue unranked if the implementation supports that transition.

The same character reconnecting does not count as a replacement. The timer keeps running; reconnect must restore the same run identity and validated state. Disconnect recovery must not reset cooldowns or restore resources beyond the published rules.

At restart, the server rebuilds encounter state and applies a consistent starting-resource policy. Validate health, mana or equivalent resources, cooldowns, pets, temporary summons, buffs and encounter triggers. A deterministic reset is necessary to avoid spending minutes outside the dungeon preparing each attempt.

Technical safeguards may rate-limit malicious request floods or instance-creation abuse. They should use idempotent resets and dedicated run state where possible, so ordinary repeated attempts do not hit a broad farming cap intended for another activity.

## Leaderboard integrity and longevity

Rank runs by dungeon and ruleset version. The version includes normalization, encounter scripts, relevant class balance and objective definitions. Server timestamps and completion evidence establish the result; client-reported times do not.

Routes may use legitimate class tools, but objectives should prevent skipping the substance of the dungeon. Audit outlier runs and investigate exploits before altering rankings. A death penalty, exact tie-break policy and treatment of intentional resets need published rules before competition starts.

Material balance changes create a new ranking version and archive the previous records with their context. Minor fixes should not fragment rankings unnecessarily, but any change affecting achievable times must be assessed. Keep an actively maintained route to permanent medal rewards instead of relying on limited-time removal for motivation.

Class composition and subgroup filters may help interpretation, but too many categories can fragment participation. Begin with overall rankings and visible composition; add filters only if useful and supported by sufficient participation.

## Pilot scope and open decisions

Start with a few dungeons that support distinct tactical pulls, readable routes and credible completion conditions. Do not convert the entire catalog before proving encounter quality and maintenance cost. Long exploratory dungeons can remain excellent Heroics without becoming timed courses.

Open questions include medal thresholds, death penalties, equipment changes during a run, talent locking, profession consumables, reward duplication and ruleset archival cadence. Favor an understandable starting policy and publish it before ranked runs begin.

Measure ordinary Heroic completion, composition diversity, ranked abandonment, restart friction, exploit frequency and whether players feel compelled to farm unrelated content before participating.
