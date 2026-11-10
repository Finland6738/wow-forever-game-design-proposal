# Alchemist

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A combat experimenter chooses a small mixture loadout and transforms a renewable class reagent into bombs, restorative compounds or temporary bodily changes. The gameplay resource is not a bill for profession-crafted consumables on every pull.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Bombardier](#bombardier) | Ranged DPS |
| [Combat Medic](#combat-medic) | Healer |
| [Mutagenist](#mutagenist) | Melee DPS |

**Equipment proposal:** Light/medium armor under review; reusable class apparatus and ordinary class weapons.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Reagent is generated through valid class actions up to a fixed cap. Prepared mixture slots select available reactions; consuming or changing a mixture has a declared cost and cannot duplicate a payload.

**State progression:** Loadout prepared → reagent generated → mixture primed → thrown, administered or transformed → residue/recovery. Mutagenist adds a timed altered-body state with a clear exit.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Bombardier

**Primary role:** Ranged DPS. **Design status:** proposed tree specification.

**Decision loop:** Build Reagent, prime a limited reaction and choose immediate impact versus a persistent hazard. Placement and target movement matter more than buying consumables.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Reagent Shot | Attack a legal target to generate the combat reagent reserve. | No farming harmless targets for an uncapped opener. |
| Volatile Flask | Commit a mixture to a visible area explosion. | Finite target cap and travel; enemies can move before impact. |
| Catalytic Field | Spend reagent on a short persistent damage area. | Overlapping fields use an explicit stacking rule and shared total budget. |

**Talent anchors to allocate:** Early: faster generation or larger reserve. Middle: impact burst versus residual pressure. Capstone: combine two reviewed reaction tags at increased cost, without multiplying every ground effect independently.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Combat Medic

**Primary role:** Healer. **Design status:** proposed tree specification.

**Decision loop:** Build a limited preparation reserve while treating allies, then choose direct triage, a delayed restorative compound or an emergency stabilizer.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Field Draught | Restore a valid ally and generate preparation through effective treatment. | No infinite resource from overhealing; invalid constructs cannot be healed. |
| Restorative Compound | Commit reagent to a bounded healing-over-time effect. | Duration, dispel and stacking are explicit. |
| Stabilizing Injection | Spend a larger reserve for an emergency heal or reviewed prevention window. | Competes with sustained treatment and has a clear recovery cost. |

**Talent anchors to allocate:** Early: efficiency versus response time. Middle: single-target triage versus limited group delivery. Capstone: a finite emergency treatment sequence with shared reagent and healer-resource costs.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Mutagenist

**Primary role:** Melee DPS. **Design status:** proposed tree specification.

**Decision loop:** Prepare an altered-body window, engage at close range and spend a limited instability allowance on empowered attacks before returning to a stable form.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Prime Mutagen | Spend reagent to enter the selected timed mutation. | One active mutation; no stacking independent forms. |
| Reactive Strike | Use a melee action that builds controlled Instability. | Requires valid melee position; instability cannot be generated out of combat indefinitely. |
| Purge Reaction | Consume Instability for a finishing attack and end or shorten the form. | Trades future empowered actions for an immediate release. |

**Talent anchors to allocate:** Early: safer instability recovery or greater output at a higher commitment cost. Middle: mobility utility versus a longer stationary damage window. Capstone: a short controlled overreaction with a hard recovery rule, not unlimited self-healing.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

An invalid throw fails before spending; a committed projectile follows the target-death policy. Dispelling a mutagen ends the transformation under a published recovery rule, rather than refunding its full damage window.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Bombardier, Combat Medic and Mutagenist each have their own role budget. A healing mixture does not remain a full healer kit on the damage trees, and profession recipes cannot become required class upgrades.

Apply permanent equipment, finite Runes and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Complete a pull with no profession consumables and no loss of the baseline class rotation.
2. Move enemies out of a catalytic area and verify bounded target and stack behavior.
3. End a mutation through expiry, dispel and death without carrying its advantages into another state.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.
