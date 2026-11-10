# Class Roles and Specializations

[← Classes](classes.md) · [Races](races.md) · [Artificer](classes/artificer.md) · [Summoner](classes/summoner.md)

## Selected direction

The proposal investigates **four distinct group responsibilities: tank, healer, DPS and pure support**. Melee/ranged describes delivery, while physical/magical describes damage; neither creates an additional mandatory group slot. Bruiser is deferred from the active role model.

A candidate class has three Vanilla-style talent trees. A build has a clear primary responsibility and budget; mixed-tree allocations require explicit review instead of an assumed modern specialization lock. A support build trades direct output for active utility. Supporting players need meaningful decisions, feedback and contribution credit.

## Role contract

| Role | Primary responsibility | What it must prove | What it does not imply |
| --- | --- | --- | --- |
| Tank | Manage enemy attention, positioning and incoming danger | Threat, survival, recovery, boss handling and understandable healer interaction | Every defensive-looking class is a tank |
| Healer | Recover allies and manage triage/resources | Sustained and emergency healing within the encounter model | Unlimited damage prevention or mandatory resource subsidy for another class |
| DPS | Supply the sustained/burst damage required by the group | Useful output at its intended range, priorities and mechanics | No utility, or equal maximum output in melee and at range |
| Pure support | Improve the group's ability to execute through utility | Active control, protection, resource/position tools and usefulness against bosses | Competitive direct damage, full healing or the main tank responsibility |

Support can have a modest personal attack and limited self-preservation. Its main contribution comes from its support toolkit. Those allowances permit ordinary play without redefining it as a full DPS or healer. Exact output shares remain open.

## Five-player compositions

Both of these compositions must be viable in ordinary five-player content:

| Composition | Purpose |
| --- | --- |
| 1 tank + 1 healer + 3 DPS | Traditional group; no new-class requirement |
| 1 tank + 1 healer + 2 DPS + 1 support | A support occupies one of the three flexible slots |

There is **no sixth player slot and no compulsory support slot**. Viable means a reasonably prepared group can finish the intended encounters, not that every composition must have identical speed, safety or tactics. A support lineup may gain control and recovery room while losing direct damage. If boss checks make that loss insurmountable, the role or encounter has failed the test.

**Selected ordinary-play trade-off:** the support lineup is generally a little slower, with more control and safety. This is an intended aggregate trade-off, not a rule forcing every individual run to be slower. Exact tolerance remains open. The discussed 15–25% time/wipe figures are not adopted targets; buffs, debuffs and control should make execution smoother while the direct-damage slot is sacrificed. Timed Challenge and Arena treatment require separate evaluation; no hidden encounter-health reduction compensates for the selected lineup.

The same dungeon should not arbitrarily lower boss health when a support joins: that hides whether the role works and creates roster-change exploits. Test both groups against the same ordinary encounter. A future difficulty-specific rule requires a separate explicit decision.

Raids need a support contribution and stacking budget for their intended size. No automatic rule such as one support per five players is selected. Challenge leaderboards and Arena formats need published composition and effect policies before support is enabled competitively; do not assume a new role is already normalized fairly.

## A support toolkit that remains useful

| Toolkit area | Active decision | Limits and boss treatment |
| --- | --- | --- |
| Control | Which threat to interrupt, slow, disorient or hold? | Respect immunities and diminishing returns; provide non-control uses in boss encounters |
| Protection | Who needs a brief prepared shelter or interception window? | Bounded prevention; not a second full tank or an unlisted healing throughput role |
| Position and access | Where should the group regroup or gain a short movement opportunity? | No encounter-wall bypass, indefinite kiting or removal of every positioning mechanic |
| Dispel and countermeasure | Save a response or spend it on a present threat? | Alternate class/tool solutions; no encounter requiring one new specialization |
| Resource efficiency | Help a teammate through a short shortage or prepare the next phase? | No infinite mana/energy loop, mandatory external battery or free permanent stat increase |
| Group preparation | Which limited benefit fits the next pull or phase? | Active choices and visible expiry; avoid a passive buff character parked outside the instance |

These are design spaces, not a promise that every support gets every tool. A Bard may organize timing and morale; Summoner/Sporekeeper prepares living zones and releases. Their actual decisions must differ.

A useful boss test removes ordinary crowd control from the target. The support still needs meaningful protection, countermeasure, positioning or resource decisions. It must not become a low-output spectator, nor should it gain permission to stun a boss simply to justify its slot.

## Feedback, credit and leveling

Display useful effects: prevented damage under clear accounting rules, successful interrupts, meaningful control, valid dispels and objective contributions. Do not rank support solely by damage or raw healing. Attribute summon/device contributions to the owner and deduplicate reward claims; four devices do not create four player participation shares.

A support must have a practical leveling path, a training introduction and a way to complete ordinary interactions. The group-first philosophy can reward cooperative progress without making a solo quest enemy impossible. Choose the leveling approach and baseline offensive tool in the prototype; do not silently assume a permanent leveling partner or paid respecs.

Inputs need clear target priorities and a readable interface. Avoid requiring a voice command for every ability or a meter that claims all teammates' damage as the support's own achievement. Group effectiveness should be measured through matched encounter outcomes, resource pressure and execution, as well as personal output.

## What constitutes a specialization

A talent tree changes resource decisions, role or delivery enough to sustain a coherent build. A different color of the same attack is a visual variant. Each of the eighteen candidate classes now has **three tree specifications**, with ranks/depths and hybrid allocation still requiring validation under the [implementation standard](implementation-standard.md). The thirteen mechanical studies have primary homes in the [coverage audit](mechanic-coverage.md).

The selected Summoner direction contains **Swarmcaller, Soulbinder and Sporekeeper**. They share accumulating and commanding small beings, but their damage timing and utility choices must differ. The Artificer's Puppet Warden is a tank; a separate Artillery branch cannot retain full tank capability alongside full DPS.

## Questions for the next design review

### Decisions recorded from the author

| Topic | Recorded direction |
| --- | --- |
| New races and factions | Every new playable people begins with an introduction and then permits choosing Alliance or Horde |
| Armor presentation | Visible anatomy-specific adaptations that preserve recognizable item identity |
| Naming | English archetype names |
| Group roles | Study pure support as a distinct responsibility; defer bruiser |
| Five-player groups | Support can replace one DPS; traditional and support compositions both remain viable |
| Artificer tank | Stationary, repairable, movable dummies with threat, taunt and talent-dependent equipment |
| Artificer movement | Hammer/kick positioning; ordinary dummies do not autonomously chase enemies |
| Artificer capstone | A powerful temporary autonomous puppet, extra to the dummies, with its own balance budget and cooldown |
| Swarm beings | Follow the caster and attack on orders; not individually selectable and have no HP |
| Swarm counterplay | Attack, control or interrupt the caster; no hidden AoE health bars |
| Summoner branches | Swarmcaller and Soulbinder are DPS; Sporekeeper is pure support, in the same class |
| Construct health | Separate HP for each dummy; only the Artificer repairs it; ordinary healers heal the player |
| Class structure | Three talent trees for each of the eighteen candidate classes |
| Two-form predator | Automatic internal combat cycle, independent of world day/night; manual form selection is not the core mechanic |
| Talent reference | 51 points at level 60, capstone at 31; full allocation and hybrid builds require review |
| Support trade-off | Slightly slower ordinary group play with more control and safety; both lineups remain viable |
| Last dummy lost | Short owner emergency defense and reconstruction at a real cost; numerical behavior open |

### Open choices to resolve through examples

1. Which protection, control and countermeasure actions make Sporekeeper useful against bosses without becoming a healer or a compulsory pick?
2. What repair throughput, construction cost and external prevention policy sustain independent dummy HP without free rebuild loops? See the [tank dossier](classes/artificer.md#defense-and-healer-interaction).
3. Should the first dummy cap be three or four, and how much deployment/repositioning should a normal pull require?
4. What duration, cooldown and failure behavior make the extra autonomous puppet powerful without being required for every ordinary tank check?
5. What maximum swarm size and generation pace feel good without a mandatory pre-pull wait? Start with a small tested cap; no exact number is selected.
6. What happens to committed swarm units on target death, range loss or a phase transition? The recommended recovery policy is in the [Summoner dossier](classes/summoner.md#orders-recovery-and-target-changes).
7. Which two or three race bodies should receive the first wardrobe mockups, and which class families deserve a complete kit after Artificer and Summoner?
8. What support leveling path, raid stacking limits and competitive formats preserve a clear role without compulsory composition?

These are continuing design questions, not approval gates for keeping the documentation current. Numerical suggestions remain prototypes until tested and discussed.

## Class identity and alternative solutions

The author selected multiple valid group solutions, without requiring a specific class for an encounter. This does not give every class every tool. See [concrete examples](group-tools-and-class-identity.md).
