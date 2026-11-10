# Procedural expeditions for groups of 5–20

[← Main proposal](../README.md) · [Documentation index](README.md) · [Dungeon modes](02-dungeons-and-challenges.md) · [Technical rules](04-technical-framework.md)

## Explore an uncertain route together

Portals appear in the open world and lead to level-60 cooperative expeditions for **5–20 players**. Each expedition assembles a new route from authored environment modules, then selects compatible enemy packs and bosses. The group may discover between **one and five floors**, with bounded increases in challenge as it descends.

The goal is exploration, improvisation and group coordination. These are untimed adventures with a finite depth, separate from fixed-layout Heroics, raid progression and normalized timed Challenge Modes. There are no keystones, escalating key levels or requirement to complete earlier expeditions.

Random generation creates variety, but a finite module library cannot guarantee a layout that has never appeared before. The design promises generated routes and encounter arrangements, rather than literal uniqueness forever.

## Entry and expedition identity

| Element | Proposed behavior |
| --- | --- |
| Discovery | Visible portals appear at approved world locations, avoiding mandatory travel chokepoints |
| Access | All participants are level 60; 5–20 characters required to begin |
| Entry resource | No consumed key or crafted admission item |
| Party binding | One server-owned expedition ID and seed bind the admitted group |
| Depth | The seed commits a finite total of 1–5 floors before play begins; later floors can remain undiscovered |
| Route | Connected modules produce different layouts, branches and encounter placements |
| Reconnect | Admitted characters return to the same expedition state through a reserved return path |
| World portal expires | No new groups start there; an admitted group's return access remains for a published grace period |
| Completion | The final floor completes the expedition and grants its configured rewards |

Keep the entry point open enough for groups to form without a narrow click race. Consider several simultaneous group instances per discovery opportunity, rather than first-click guild ownership. Portal lifetime, discovery frequency and concurrency limits need testing; rarity should not create hours of mandatory waiting.

A floor-one clear is a valid short expedition when the committed depth is one. If the seed contains another floor, the group discovers its entrance after the appropriate objectives. The seed, planned depth and reward schedule do not reroll when the party reconnects or reforms.

## Generation as constrained assembly

Build a library of authored rooms, corridors, junctions, transitions and boss spaces with explicit connectors and traversal metadata. A server-side generator constructs a connected route graph, assigns rooms, selects encounter families and places compatible packs and bosses. The geometry can change, rather than merely shuffling enemies in a static map.

Variation includes path direction and length, branches, room order, enemy composition, patrol patterns, encounter positions and selected boss mechanics. Use pacing constraints so a generated path does not become five minutes of empty corridors or a chain of unavoidable overlapping threats.

Before admitting players, validate connectivity, navigation, collision, exits, objective reachability, safe starting space, boss arenas and supported combat combinations. Reject or repair invalid seeds. If bounded generation attempts fail, use a prevalidated expedition layout and record the fallback instead of trapping players in a broken run.

Bosses and packs are chosen from reviewed pools. Random does not mean assembling arbitrary abilities with no compatibility rules. Incompatible immunities, unavoidable simultaneous attacks, inaccessible melee targets and mandatory rare class tools must be excluded.

## Finite floor progression

Each floor increases challenge within an authored five-floor envelope. Health, damage, resistance profiles, pack tactics and a small number of additional abilities can contribute. Every permitted depth needs a completable encounter plan at the permanent baseline, with the expected execution skill for that depth.

| Floor range | Intended emphasis | Constraint |
| --- | --- | --- |
| 1 | Learn the expedition's enemy family and tactical vocabulary | Readable entry challenge; no raid-item prerequisite |
| 2–3 | More demanding pack combinations and boss interactions | Add mechanics selectively, rather than one mandatory new ability on every enemy |
| 4–5 | Sustained coordination, positioning and adaptation | Finite tuning; preserve valid strategies for different groups |

Resistance can vary as requested, but should be bounded and telegraphed. Do not make a floor effectively immune to one damage school or require a class the party could not predict at entry. Counterplay should come from tactics and accessible tools rather than carrying several exclusive old-raid sets.

The numerical tuning and number of added abilities per floor are open. A five-floor expedition should be more demanding and longer than a one-floor expedition, without creating an endless ladder or increasing permanent equipment power.

## Flexible group size without resizing exploits

Use tested scaling profiles throughout the 5–20 range. Health and damage are only part of scaling: target counts, interrupt availability, healer pressure, mechanics requiring several simultaneous participants and the usefulness of melee space all matter.

At each floor's readiness checkpoint, validate the roster and commit its group-size profile. Do not downscale a live encounter because someone leaves or dies. Dead players remain part of its committed roster, and reconnects cannot generate an easier boss.

Allow replacements and planned size changes at safe checkpoints between floors, with no reward reset or seed change. Never exceed 20 admitted active participants. If fewer than five remain, allow recovery or withdrawal rather than starting a new floor below the minimum. A wipe alone does not reopen roster changes or lower that floor's committed profile; the group can regroup with its existing roster or withdraw to the permitted checkpoint. Recovery rules must not allow repeated fresh-cooldown substitutes to defeat an otherwise active encounter.

Reward eligibility follows the floors and objectives each character actually helped complete. A last-floor replacement does not inherit rewards for earlier floors, and a departing participant's legitimate earned rewards are not reassigned to their replacement.

## Reward options and economic discipline

The reward model remains a design decision. Start the pilot with **modest gold, common crafting resources, cosmetic discoveries and Adventurer prestige**. Do not add a raid-equivalent loot ladder or exclusive combat materials required elsewhere.

| Option | Appeal | Main risk and safeguard |
| --- | --- | --- |
| Gold | Clear value without inventing another equipment tier | Unbounded generation and easy-seed farming; tune expected gold per player-hour and monitor currency creation |
| Crafting materials | Supports professions and market activity | Supply shocks and compulsory farming; use alternatives and compare acquisition rates |
| Cosmetic discoveries | Memorable exploration rewards | Unrewarding repetition or extreme rarity; consider visible collection progress and duplicate protection |
| Adventurer prestige | Recognizes continued instanced participation without stats | Farming volume mistaken for skill; use the shared eligibility and anti-repeat rules |

Later floors can grant greater rewards for their additional time and difficulty, but should not multiply gold or materials exponentially. Cap the expedition's total configured reward liability and avoid a payout structure that makes repeated first-room resets or “deepest-floor fishing” the dominant activity.

Eligible players receive personal rewards; group size should not multiply each individual's payout simply because twenty people entered. Gold remains new currency even without equipment drops, so track both per-player rates and total currency generation. Resource faucets need supply monitoring as well.

Allow players to keep legitimately earned floor rewards when leaving at a checkpoint. Subsequent floors offer additional opportunity without threatening already earned rewards. Bind claims to expedition, character and floor/objective identities so reconnects and resets cannot duplicate them.

## Controls and open decisions

No universal leaderboard compares random seeds: route length, enemy composition and depth differ. If seeded competition is explored later, use an explicitly shared seed and ruleset as a separate format, without changing unrestricted exploratory expeditions into timed requirements.

Technical abuse controls may limit malicious instance creation, but should not introduce a scarce key or punish normal experimentation. Avoid revealing profitable seed metadata before the group commits, and measure abandonment patterns before applying anti-reroll rules that could harm ordinary groups.

Open choices include portal frequency, floor duration, reward balance, tile themes, group replacement policy details, retreat behavior and whether deeper entrances require explicit party confirmation. Progress can be saved at checkpoints if supported, with a published instance lifetime and clear expiry notice.

Pilot one environment family, a small encounter pool and limited depth first. Validate generation across many seeds and representative group sizes before enabling the full five-floor envelope. Record invalid-seed rates, navigation failures, composition failures, reward output, reroll frequency and completion by depth and group size.
