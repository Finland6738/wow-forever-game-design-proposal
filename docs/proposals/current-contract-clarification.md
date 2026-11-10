# Current Contract Review — v0.11

[← Proposal](../../README.md) · [Decision register](../13-glossary-and-decisions.md) · [Evaluation plan](../05-roadmap-and-evaluation.md)

**Decision snapshot: 11 November 2026.** This review reconciles the author's twelve-point brief and subsequent answers. It supersedes earlier fixed-stat Rune allowances, globally usable raid rewards and single-route city switching. Historical changelog entries remain historical records. These are concept specifications, not measured balance or production approval.

## Step 1 — Director: preserve the level-60 promise

Keep a stable permanent power budget, group achievement and simple rules with tactical depth. A finite post-60 preparation step earns the [raid-entry preset](../systems/raid-entry-preset.md), retained as the default for new raid seasons. Releases add encounters and choices, not a higher permanent baseline. Existing bounded update/difficulty equipment effects remain a separate local progression channel requiring numerical validation.

The preset is not an instant complete set merely for reaching 60. Tasks, acquisition time, role coverage and physical-item versus entitlement representation remain open. Test a newcomer, a returning player and a role switch before declaring entry solved.

## Step 2 — Systems: completion-based Runes

[Runes](../systems/runes.md) record authored milestones and targeted unlocks. Reject 0.01% per cast, the 1% ability cap, exponential use requirements and all accumulated Rune stat allowances, including raid-only variants. Repeating casts, prolonging boss phases or farming trash cannot improve a Rune reward. No extra Rune rank, Mastery-XP tree or combat slot is introduced.

Objectives need declared rewards, role-aware evidence and duplicate handling. Validate failed encounters, repeated objectives and resets. Tactical utility can be valuable without becoming a numerical accumulator.

## Step 3 — Endgame: a raid-only talent library

The final boss teaches its difficulty's reviewed talent. Veteran does not also teach Normal. Ownership is permanent, with **one selected active OR passive option**, separate from the normal 51 class talent points.

| Learned reward | Normal raid | Veteran raid | World / any dungeon / all PvP |
| --- | --- | --- | --- |
| Normal final-boss talent | Active if selected | Inactive | Inactive |
| Veteran final-boss talent | Inactive | Active if selected | Inactive |

Historical options can be used in other raids of the same difficulty. Returning for a desired option is intended; accessible entry does not promise a complete optimized library. More utility or choice may make a raid easier, but one slot alone does not prove balance. Future encounters need several valid answers rather than one required historical talent.

Selection is outside combat, with encounter-state, cooldown and persistent-effect checks. Ordinary class abilities remain normal class tools; only this reward slot has the raid-only restriction. See the [Repertoire contract](../systems/adventurer-abilities.md).

## Step 4 — Combat and balance: support earns its place

Both 1 tank + 1 healer + 3 DPS and 1 tank + 1 healer + 2 DPS + 1 support must work in ordinary five-player content. Support actively uses buffs, debuffs, control and prevention to exchange some speed for smoother, safer execution. **No numerical duration or wipe-risk target is adopted.** The earlier 15–25% figures remain discussion examples.

Compare the same encounters, skill and gear profiles: completion, time, recoveries, utility opportunities and failure causes. Do not secretly lower boss health for the support lineup. Raid stacking and timed/ranked treatment require separate tests. See [roles](../identity/class-roles-and-specializations.md).

## Step 5 — Raid difficulty and progression duration

Normal aims to be approachable for roughly **70%** and Veteran for roughly **30%** of the relevant raiding-guild cohort. These are design targets, not entry quotas, mutually exclusive groups or validated completion rates. Define the cohort, success milestone, attendance, sessions/week and competence before measuring results.

Veteran targets **1–2 months of mechanical progression for its reference guild**. The author's Ulduar hard-mode reference is a qualitative upper difficulty compass, not a verified equivalence or an encounter-copy requirement. Strong groups may finish earlier. Difficulty comes from coordination and execution, not calendar locks, permanent stat growth or Rune-use farming.

## Step 6 — Class design: Artificer tank

Puppet Warden uses stationary dummies that taunt, generate threat, have independent HP repaired only by their owner, and move through deliberate commands. The Artificer contributes melee damage, repairs and defensive tools/cooldowns. The additional autonomous capstone puppet is powerful, temporary and has a cooldown. Last-dummy loss permits brief owner emergency defense and reconstruction at a real cost.

Aim for responsibility comparable to other tanks, not needless extra micromanagement. Threat transfer, repair/rebuild economy, damage intake and emergency timings remain open. The healer still supports the player and party; owner-only repairs must not make healing irrelevant to survival. Test moving bosses, range/line of sight, dummy loss and recovery. See [Artificer](../identity/classes/artificer.md).

## Step 7 — Encounter design: several solutions, distinct classes

No specific class is mandatory. A dangerous caster might be addressed by interruption, valid control, displacement/line of sight or eliminating the threat, according to the encounter. Immunities must leave multiple credible group solutions. This does not give every class every tool or guarantee every imaginable composition. Preserve signatures and test diverse rosters. See [Group Tools](../identity/group-tools-and-class-identity.md).

## Step 8 — World and narrative: visible territorial ownership

Captured forts, camps and towers display controlling faction and city banners. Structures, designated guards and bosses adopt that city's style. Neutral/uncontrolled objectives use the regional hostile NPC faction. Commit one authoritative ownership result and a safe appearance transition; no duplicate capture reward or free boss reset.

City variants retain comparable encounter budgets and readable mechanics. Mixed-city claims, faction-only default sponsorship, collision/navigation and art coverage remain open. Ordinary quest/service NPCs are outside the capture system. A broader province/supply simulation is not required for the first prototype. See [Faction Warfare](../activities/faction-warfare.md).

## Step 9 — Competition: Challenge and Arena

Challenge keeps the requested historical group-led feel: form a group, agree on start, reset the instance, practice and consult leaderboards. The proposal retains normalized, keyless, freely repeatable attempts, with explicit roster/reset/ruleset integrity. See [Challenge](../activities/challenge-dungeons.md).

Arena takes inspiration from hidden matchmaking rating versus visible ranked progress, using these five **proposal-specific** profiles:

| Queue | Matched partition |
| --- | --- |
| Solo duel | 1 vs 1 |
| Premade pair | 2 vs 2 |
| Solo-assembled pair | 1+1 vs 1+1 |
| Full premade | 5 vs 5 |
| Split premade | 2+3 vs 2+3 |

Do not silently merge partitions at low population. Rating formulas, divisions/points, role compatibility, 1v1 stalemates, reward eligibility and queue viability remain open. Five queues create population and maintenance risks requiring evidence. No additional five-solo queue is selected. See [Arenas](../activities/arenas.md).

## Step 10 — Race design: equipment and recognition

All ten race dossiers retain neutral introductions and either-faction choice. Anatomical adaptations preserve recognizable items and ordinary item effects. Wrists, cloaks and gloves may be adapted or hidden; footwear needs individual review. Head and weapon presentation are key readability requirements. Test class recognition through silhouette, animations, effects and nameplates together, since equipment alone cannot guarantee it.

NPC bodies are references, not proof of armor/animation feasibility. No mesh, skeleton or attachment audit has been completed. See [races](../identity/races.md) and the [implementation standard](../identity/implementation-standard.md).

## Step 11 — Social and economy: two city-switch routes

At each service change, the player chooses:

| Route | Standing consequence | Military consequence |
| --- | --- | --- |
| Preserve standing | Keep accumulated city Warfare standing | Territorial/political quarantine; ordinary combat/group play allowed, conquest claims and victory credit restricted |
| Immediate eligibility | Lose 50% of the departed city's **current Warfare standing** | No new quarantine from this switch |

The destination retains its own earlier ledger, or starts at zero. Repeated applicable departures halve the then-current balance. This never removes character XP, level, Honor or ordinary reputation. Quarantine duration is open; 14 days was an example. Non-conquest participation credit during quarantine remains open. Describing future voting/victory-credit restrictions does not introduce an actual political voting system or new currency.

Guilds remain trans-city. The NPC-managed flag on/off is a separate participation action causing neither penalty. Base cosmetics remain owned; city variants require eligible current service. Existing combat and capture commitments cannot vanish through a switch.

**Recommended anti-bypass rule, still to validate:** an existing quarantine survives another switch, including one using the standing-loss route. Low/zero standing makes the loss route weak protection, so both routes require claim-ledger checks against capture trading, claim theft and alternate-character abuse. See [City Rewards](../activities/warfare-rewards.md).

## Step 12 — Live operations: reward history and community

Recognize variety, mastery and contribution through historical titles, city decorations, winner monuments, accomplishment registers and exclusive visual variants. Distinguish historical ownership from current service insignia. No mandatory daily checklist or repeat grind adding permanent power is adopted.

Exclusive visuals need clear criteria, archives and newcomer opportunities that preserve historical success. No battle pass, automatic seasonal reset or new required currency is implied. See [recognition](../08-prestige-ranks.md).

## Evidence before implementation approval

1. Lock the permanent power/effect catalog and prototype the retained entry preset across roles.
2. Test a small raid-talent library, difficulty transitions, swaps and historical acquisition.
3. Compare support/traditional groups and moving Artificer encounters; test actual 51-point hybrid builds.
4. Pilot one Warfare area with city art variants, both switch routes and explicit mixed-claim/support rules.
5. Measure population per strict Arena profile before fixing ranked formulas.
6. Audit race wardrobe, animations and PvP recognition before calling a candidate production-ready.

Numerical tuning, engine feasibility, production cost and real player outcomes remain evidence gates.
