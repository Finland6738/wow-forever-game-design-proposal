# Roadmap, evidence and open decisions

[← Main proposal](../README.md) · [Documentation index](README.md)

## Use pilots and decision gates

This is a proposed order of investigation, not Blizzard's roadmap, a schedule or a development estimate. Reusing dungeon environments can reduce some asset work, but encounter redesign, normalization, interfaces and maintenance still need dedicated effort.

| Stage | Scope | Evidence needed before expansion |
| --- | --- | --- |
| 0 — Define the contract | Permanent equipment range, effect catalog, baseline acquisition routes and measurement tools | Role/build coverage; no obvious uncapped source of permanent power; understandable rules |
| 1 — Heroic pilot | A small representative dungeon selection with tactical redesign and baseline alternatives | Enjoyable pacing, viable compositions, accessible preparation and credible maintenance cost |
| 2 — Raid pilot | One update-wide group, including two independently enterable raids where feasible, with separate Normal/Veteran tracks | Direct Veteran access works; no previous-update dependency; sibling farming pressure is acceptable |
| 3 — Challenge pilot | A few suitable dungeons, approved normalized profiles, free retries and versioned rankings | No hidden legacy-gear requirement, low restart friction and reliable run validation |
| 4 — Elite-region pilot | One cooperative region, one territorial boss and optional crafting artifacts | Sustainable participation, non-monopolized reward access and reasonable technical performance |
| 5 — Broader world activities | A limited regional PvP test, small-group adventures, professions and optional Legacy integration | Ruleset consent, leveling protection, viable faction participation and no cross-activity power obligation |

Stages can overlap where work is independent. Challenge competition depends on a trustworthy normalization framework; full raid isolation is the central progression experiment and should not wait for the entire dungeon catalog. Do not launch every system simultaneously.

## What success looks like

Set thresholds before each pilot using baseline data. This proposal intentionally does not invent universal hour targets, completion rates or statistical significance claims.

| Question | Suggested measurement | Warning signal |
| --- | --- | --- |
| Can returning players join a new raid directly? | Preparation time, required item sources and first successful participation, split by role and prior equipment | Old raid items or several compulsory activity tracks dominate preparation |
| Are difficulties independent? | Normal participation among Veteran groups, item/currency dependencies and player-reported reasons | Groups feel they must clear Normal for Veteran power |
| Is shared raid scope healthy? | Order of sibling raids attempted, power acquisition efficiency and skipping behavior | The shortest raid becomes the expected weekly prerequisite |
| Are rewards satisfying? | Repeat participation, collection goals, local upgrade value and qualitative feedback | Players describe all drops as disposable or mandatory chores |
| Is the item budget holding? | Simulated and observed build output, survivability, proc interactions and outlier acquisition sources | Equal item levels hide dominant old effects or upward permanent power drift |
| Are dungeons composition-friendly? | Completion and abandonment by composition, role demand and mechanic failures | One class tool becomes a practical entry requirement |
| Are Challenges accessible and fair? | Retry latency, invalidation reasons, suspicious runs, template use and composition concentration | Keyless access still requires old-item farming or lengthy restart preparation |
| Is world participation open? | Reward eligibility by faction/group/role, repeat control and event availability | A guild, faction or damage-only participation rule excludes others |
| Are activities optional in practice? | Player-reported obligation and preparation-path analysis alongside participation counts | High engagement primarily reflects power coercion |

Assess short-term novelty and repeat behavior separately. A high participation rate does not alone prove that players enjoy an activity or that its rewards are appropriately independent.

## Decisions already selected

- Permanent equipment remains usable, with additional progression bonuses restricted by context.
- Approved raids in the same content update share a progression scope.
- Normal and Veteran maintain independent contextual power and acquisition tracks.
- Veteran adds prestige and its own internal progression without exporting extra power.
- Heroics provide tactical level-60 adventures; Challenge Modes provide keyless, normalized timed mastery.
- World, PvP and profession systems remain parallel rather than compulsory gearing steps.

## Open design questions

| Decision | Starting direction | What must be resolved |
| --- | --- | --- |
| Permanent baseline | Finite non-raid preparation with several routes | Role-specific profiles and the definition of adequate entry preparation |
| Contextual item representation | Keep item identity; consider a bonus archive | Ownership, inventory, trading and retrieval behavior |
| Shared raid loot cadence | One capped update/difficulty track with equivalent routes | Short-raid efficiency, loot allowance design and late-joiner progression |
| Local upgrade depth | Finite, meaningful improvements | Number of choices, magnitude, acquisition pace and how much reclear ease is healthy |
| Challenge normalization | Accessible approved templates/profile equivalents | Allowed effects, talents, consumables, equipment swaps and class variety |
| Competitive rules | Fixed roster, server timer, versioned objectives | Death penalties, ties, run evidence and archival policy |
| Elite-region access | Repeated cooperative events with personal eligibility | Participant envelope, support credit, event copies and faction access |
| Regional control | Temporary objectives and local rewards | Duration, comeback mechanics, consent transitions and economic side effects |

## Revision policy

Keep the invariants explicit. When a proposed change weakens one, describe the player benefit, new dependency and evidence that would justify the compromise. Record major decisions in the [change history](../CHANGELOG.md).

Publish the repository as the detailed discussion reference. The [forum summary draft](forum-summary.md) can introduce the central promise and link here after editorial review. No forum publication is included in this repository setup.
