# Beastmaster

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A pack leader chooses focus versus distributed companion tasks while remaining an active combatant. Companion jobs and a shared output budget matter more than accumulating an unrestricted number of independent animals.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Packleader](#packleader) | Melee DPS |
| [Wildbond](#wildbond) | Ranged DPS |
| [Trailwarden](#trailwarden) | Pure support |

**Equipment proposal:** Medium armor; branch-specific ranged/melee weapons and a bounded persistent pack.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Command is a bounded class reserve. Each owned companion has an order, legal target, health/recovery state and leash. These ordinary companions do not inherit Summoner's selected no-HP rule.

**State progression:** Pack ready → assign focus/task → commit Command → resolve/recover → regroup. Companion loss reduces a function and opens a defined recovery action rather than demanding another rare tame.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Packleader

**Primary role:** Melee DPS. **Design status:** proposed tree specification.

**Decision loop:** Fight beside a small pack, build Command through melee and choose a shared focus or a limited split assignment.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Pack Strike | Attack in melee and generate Command. | Player and pack share one total damage allowance. |
| Focus the Pack | Commit Command to a priority attack sequence. | Bounded owned units and a single declared target order. |
| Regroup Command | Recall/reposition eligible companions for the next engagement. | No free full health/output reset or threat wipe. |

**Talent anchors to allocate:** Early: command reliability versus a larger commitment. Middle: focused pressure or limited task distribution. Capstone: a finite coordinated pack sequence without adding an uncapped animal count.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Wildbond

**Primary role:** Ranged DPS. **Design status:** proposed tree specification.

**Decision loop:** Use ranged actions while directing complementary companion jobs, then choose which bond receives the next limited enhancement.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Guiding Shot | Deal ranged damage and build Command. | Valid range and no free full melee alternative. |
| Bonded Order | Empower one reviewed companion function. | Enhancement does not create a second full independent character. |
| Redirect Bond | Change an eligible assignment at a resource/recovery cost. | No through-wall delivery or duplicated committed attack. |

**Talent anchors to allocate:** Early: bond retention or faster reorders. Middle: steady ranged pressure versus a stronger planned companion release. Capstone: a finite bonded window with one owner-level proc and output policy.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Trailwarden

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Assign a small number of companions to scouting, local protection or disruption and spend Command on an active group execution window.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Trail Signal | Actively generate support Command and select the next assignment. | No passive outdoor-only benefit as the whole group contribution. |
| Guarding Companion | Commit a bounded protective/interception action. | Does not provide a second main tank or full healer. |
| Disrupting Order | Spend Command on eligible local control or a countermeasure. | Boss immunity remains; guarding utility stays useful when control fails. |

**Talent anchors to allocate:** Early: assignment recovery or retained Command. Middle: protection versus disruption. Capstone: a finite group route/protection sequence with legal movement and a shared support budget.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

Pathing failure cannot supply remote immunity. Target switching and recall preserve costs. A lost companion has an accessible class recovery; baseline viability does not require a contested rare-world creature.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Packleader is melee damage, Wildbond is ranged damage and Trailwarden is pure support. Mounted/dismounted damage transfer is assigned to Cavalier/Beast Rider; this family focuses on pack assignments instead.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Lose a companion in a boss fight and recover through class tools without a required rare tame.
2. Assign several pack jobs without multiplying proc, reward or player-count calculations per animal.
3. Complete indoor and control-immune encounters with the support tree and ordinary class alternatives.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
