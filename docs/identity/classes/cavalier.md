# Cavalier

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A Cavalier coordinates commitment, position and a companion across mounted and dismounted states. Every talent tree needs a viable indoor form; ordinary dungeon access cannot require redesigning all ceilings and corridors.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Outrider](#outrider) | Melee DPS |
| [Mounted Guardian](#mounted-guardian) | Tank |
| [Beast Rider](#beast-rider) | Melee DPS |

**Equipment proposal:** Medium/heavy armor; reviewed mounted/foot weapons and one companion with a defined recovery policy.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Command is a bounded reserve generated through valid combat actions. Mounted state, companion order and any transferred-damage debt are distinct states. A movement stance is not unrestricted transport speed.

**State progression:** Approach → mounted commitment or foot command → spend Command → regroup → recover. Beast Rider adds a capped temporary damage-debt ledger while dismounted.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Outrider

**Primary role:** Melee DPS. **Design status:** proposed tree specification.

**Decision loop:** Choose an approach lane, commit to a bounded mounted or on-foot assault and regroup before another deliberate engagement.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Set the Approach | Prepare a legal short engagement path and build Command through combat. | No terrain/wall bypass or free transport-speed combat. |
| Committed Charge | Spend Command on a telegraphed close-range engagement. | Navigable path, normal targeting and explicit stop behavior. |
| Dismounted Follow-through | Continue the core attack sequence indoors or after dismount. | Foot play remains a real damage loop rather than a disabled half-kit. |

**Talent anchors to allocate:** Early: safer regrouping or stronger commitment. Middle: charge setup versus sustained foot actions. Capstone: a finite assault sequence with one reviewed movement/output allowance.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Mounted Guardian

**Primary role:** Tank. **Design status:** proposed tree specification.

**Decision loop:** Establish attention, face the threat and use Command to protect through deliberate mounted/foot guard actions.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Guardian Challenge | Generate threat and taunt where permitted. | Normal boss immunity and taunt policy remain effective. |
| Braced Guard | Spend Command on active mitigation with visible facing/coverage. | Viable on foot; no mount-only required mitigation. |
| Guarded Reposition | Move to a legal defensive anchor and maintain controlled attention. | No boss teleport, attack-timer reset or indefinite kiting. |

**Talent anchors to allocate:** Early: mitigation consistency versus movement recovery. Middle: focused guard or limited add coverage. Capstone: a finite defensive commitment whose cooldown and strength compare with other tank tools.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Beast Rider

**Primary role:** Melee DPS. **Design status:** proposed tree specification.

**Decision loop:** Ride to engage with the companion, dismount to coordinate two bodies and manage a bounded transfer of companion damage before regrouping.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Ride Together | Enter the combat stance or use its indoor fallback. | No extra transport speed or free health reset. |
| Separate Orders | Dismount and direct the companion while using foot attacks. | Only a reviewed portion of valid companion damage enters the capped owner debt. |
| Regroup | Rejoin and resolve the debt through the published recovery rule. | Cannot erase unlimited damage by repeatedly mounting; debt persists through state changes. |

**Talent anchors to allocate:** Early: clearer recovery versus longer separated commitment. Middle: coordinated attacks or safer debt management. Capstone: a short partnered sequence with one shared damage/survival budget, not two full characters.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

Mount failure on terrain falls back to a useful on-foot action. Companion loss has a recovery route; dismounting or zoning cannot erase damage debt or reset a cooldown.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Outrider and Beast Rider are melee damage, Mounted Guardian is a tank candidate. The mounted/dismounted damage-transfer study has its primary home here; Beastmaster no longer duplicates a separate Beast Rider proposal.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Complete a low-ceiling dungeon pull with a useful on-foot version of every core tree action.
2. Accumulate companion damage debt, dismount/remount and verify that no free full recovery occurs.
3. Tank a moving boss without geometry exploits, camera obstruction or attack-timer resets.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
