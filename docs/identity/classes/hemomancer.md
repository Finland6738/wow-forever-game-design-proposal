# Hemomancer

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A Hemomancer builds Blood through valid combat or healing actions, spends reserves and may accept a bounded personal health cost. The core decision is reserve timing versus controlled risk, not unlimited conversion of allied healing into damage.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Bloodweaver](#bloodweaver) | Ranged magical DPS |
| [Nightform](#nightform) | Melee magical/weapon DPS |
| [Lifewarden](#lifewarden) | Healer |

**Equipment proposal:** Light armor; caster focus and branch-reviewed close-range weapons for Nightform.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Blood has a fixed cap. Health substitution is optional, limited and cannot pay into unavoidable death. Drains, overhealing and self-arranged damage have explicit generation ceilings and exclusions.

**State progression:** Generate Blood → bank → cast/transform/treat → spend reserve or bounded own health → recover. A form has upkeep and a visible forced-exit condition when its allowance ends.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Bloodweaver

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Generate Blood through ranged pressure, bank it for a planned release and choose whether a limited personal health substitution is worth the timing.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Sanguine Bolt | Deal valid ranged damage and generate Blood. | Reviewed generation; no harmless-target infinite opener. |
| Blood Release | Spend reserve for a focused magical action. | Finite cost and target policy; no free unlimited drain loop. |
| Measured Sacrifice | Permit a bounded own-health substitution when eligible. | Health floor and cooldown/allowance prevent lethal or healer-subsidized spam. |

**Talent anchors to allocate:** Early: safer banking versus stronger timed spend. Middle: stable output or limited sacrifice efficiency. Capstone: a finite release window with an explicit self-cost ceiling.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Nightform

**Primary role:** Melee magical/weapon DPS. **Design status:** proposed tree specification.

**Decision loop:** Build Blood through close-range actions, enter a short winged/swarm-like form and decide how long to maintain its upkeep before returning to ordinary combat.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Bloodfang Strike | Use a legal close-range attack to build Blood. | Melee commitment and owner vulnerability remain. |
| Nightform | Enter the timed/upkeep form with a reviewed movement response. | No unrestricted flight, collision phasing or invulnerable swarm state. |
| Return to Flesh | End the form and preserve remaining resource under the recovery rule. | Cannot reset all cooldowns or heal to full through rapid form cycling. |

**Talent anchors to allocate:** Early: reserve retention or smoother exit. Middle: movement flexibility versus a stronger committed attack window. Capstone: a finite transformation release with bounded upkeep and recovery.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Lifewarden

**Primary role:** Healer. **Design status:** proposed tree specification.

**Decision loop:** Generate a controlled Blood reserve through valid treatment and choose direct recovery, delayed restorative pressure or limited personal sacrifice in an emergency.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Lifeweaving | Heal a valid ally with ordinary healer-resource pressure. | Overhealing and arranged self-damage do not create infinite Blood. |
| Restorative Transfer | Spend owned Blood on an eligible heal or healing-over-time effect. | No involuntary draining of another player's health or Artificer construct healing. |
| Last Reserve | Use a bounded personal-cost emergency response. | Cannot pay into guaranteed death or replace every resource constraint. |

**Talent anchors to allocate:** Early: efficient generation or emergency responsiveness. Middle: direct triage versus delayed treatment. Capstone: a finite recovery sequence with explicit health/resource floors.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

Owner death stops new actions. Overhealing cannot create infinite Blood; enemy immunity does not remove every builder. Zoning, form changes and encounter resets preserve the published resource/cooldown rules.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Bloodweaver is ranged damage, Nightform is close-range damage and Lifewarden is healing. Self-sustain does not make a DPS tree a tank, and healer support cannot become a required damage battery.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Spam overhealing and arranged self-damage without generating an unlimited reserve.
2. Exhaust Blood during Nightform and exit visibly without immunity or a full free reset.
3. Compare a mixed sacrifice build with the intended healer/damage budgets and external-healing burden.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
