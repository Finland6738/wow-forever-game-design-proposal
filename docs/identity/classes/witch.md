# Witch

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

The Witch prepares linked hexes and chooses whether to sustain, relay or consume them. The familiar changes delivery and positioning rather than adding an unbudgeted second complete character.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Hexkeeper](#hexkeeper) | Ranged magical DPS |
| [Familiar](#familiar) | Ranged magical DPS |
| [Coven](#coven) | Pure support |

**Equipment proposal:** Light armor; focus and one familiar with an explicitly reviewed pet interaction policy.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Thread is generated through valid hex actions up to a cap. Each owned hex records its target, remaining duration, link group and consumption state. A familiar has a separate bounded command/recovery state.

**State progression:** Weave → attach → maintain or relay → consume/unravel → recover. Familiar loss suspends familiar-specific actions and exposes a defined resummon path.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Hexkeeper

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Build Thread, attach a limited linked curse set and choose sustained pressure versus a deliberate consumption on the priority target.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Weaving Bolt | Damage a valid target and generate Thread. | No uncapped pre-pull storage. |
| Linked Hex | Attach a bounded-duration damage hex to an eligible target. | Owned target cap and link budget prevent unlimited spreading. |
| Unravel | Consume selected hexes for a reviewed release. | Remaining future damage is converted or canceled; no double payout. |

**Talent anchors to allocate:** Early: longer retention versus faster weaving. Middle: focused hexes or bounded multi-target links. Capstone: a finite unravel sequence whose total payload remains in the class budget.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Familiar

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Maintain one familiar as a relay, choose its safe position and direct a limited curse delivery or retrieval while the caster continues attacking.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Familiar Order | Assign a legal target or relay point to the owned familiar. | Leash, pathing and line-of-sight rules prevent remote immunity. |
| Relay Hex | Commit Thread to deliver a hex through the familiar. | The relay does not grant a second independent proc or full damage copy. |
| Recall Bond | Recover the familiar or a still-unused commitment. | No full refund after a payload has resolved; death/recovery has an explicit cost. |

**Talent anchors to allocate:** Early: safer relay recovery versus stronger commitment. Middle: delivery flexibility or sustained target pressure. Capstone: a short empowered relay window with one owned familiar and a bounded total output.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Coven

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Prepare a small set of protective/control threads, choose which ally or threat to link and release one countermeasure at the right time.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Protective Thread | Build a limited preparation link through an active support action. | No free passive benefit from parking outside the group. |
| Ward Knot | Spend Thread on a finite protective response. | Does not become full healing or a permanent tank shield. |
| Sever Hex | Consume a link for one selected control/dispel response. | Reviewed effect categories and ordinary encounter alternatives are required. |

**Talent anchors to allocate:** Early: link retention or faster active setup. Middle: ally protection versus enemy countermeasure. Capstone: a finite coven pattern that spends its prepared links rather than multiplying every teammate's output.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

Dispel rules distinguish damage effects from control. A removed control hex cannot automatically reapply without cost or diminishing returns. Boss immunity leaves a valid damage or support fallback.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Hexkeeper and Familiar are different ranged damage trees; Coven is pure support. Familiar targetability is not inherited from the Summoner's no-HP beings and requires its own pet rules.

Apply permanent equipment, finite Runes and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Dispel a control hex repeatedly and preserve costs, immunity and diminishing-return rules.
2. Lose the familiar on a boss and recover without immunity or a nonfunctional full fight.
3. Consume linked DoTs and verify remaining-payload accounting across several owned targets.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.
