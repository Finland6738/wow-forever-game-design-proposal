# Necromancer

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A Necromancer converts a class-generated remnant resource into temporary undead formations, decay or protective bone structures. Physical corpses may provide flavor but cannot be required for a boss-only fight.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Legion](#legion) | Ranged magical DPS |
| [Decay](#decay) | Ranged magical DPS |
| [Boneweaver](#boneweaver) | Pure support |

**Equipment proposal:** Light armor; staff/focus and bounded formation controls.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Remnants have a fixed capacity and come from valid class actions. Formation commitments, owned decay effects and prepared bone structures draw from the same reviewed class contribution rather than free extra entities.

**State progression:** Generate Remnants → form or attach an owned effect → command/sustain → expend or recover → rebuild. A destroyed/expired formation follows an explicit replacement cost.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Legion

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Generate Remnants, build a bounded formation and choose whether to reinforce, redirect or expend it while continuing caster actions.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Remnant Bolt | Attack a legal target and build Remnants. | Functional without physical corpses or adds. |
| Raise Formation | Commit reserve to a bounded owned group. | Entity/order cap and output inheritance are explicit. |
| Expend the Line | Consume part of the formation for a planned release. | Consumed entities cannot retain their future attacks or refund full value. |

**Talent anchors to allocate:** Early: replacement recovery or larger commitment. Middle: focused formation versus bounded coverage. Capstone: a finite legion window funded by the tree's full contribution budget.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Decay

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Build a reserve through direct casts, establish limited decay states and choose sustained attrition versus consuming a state for a planned finish.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Withering Cast | Deal direct damage and generate Remnants. | Normal range and line of sight. |
| Measured Decay | Apply an owned finite damage state. | Reviewed target/stack cap; control and damage flags remain separate. |
| Harvest Decay | Consume remaining state potential for a reviewed release. | No full DoT plus full free burst from one commitment. |

**Talent anchors to allocate:** Early: retention versus generation. Middle: focused attrition or a bounded spread. Capstone: a short harvest sequence with transparent remaining-payload accounting.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Boneweaver

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Generate Remnants through active support/caster actions, prepare a small bone pattern and release finite prevention or control where the group needs it.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Gather Fragments | Actively build the support reserve without requiring deaths. | No out-of-combat corpse economy as a raid prerequisite. |
| Bone Shelter | Commit reserve to a finite preventive structure/effect. | No universal collision wall, full tank body or direct healer throughput. |
| Binding Lattice | Spend preparation on bounded local control or a reviewed countermeasure. | Boss immunity remains; the tree retains shelter use on immune targets. |

**Talent anchors to allocate:** Early: preparation efficiency versus retention. Middle: focused protection or limited area control. Capstone: a finite lattice release with a hard shared prevention/control allowance.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

No corpse is available is a normal supported case. Harmless creature farming, repeated resurrection and another player's corpse cannot generate an infinite reserve or duplicate rewards.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Legion and Decay supply ranged damage through different commitment patterns. Boneweaver is pure support with preventive structures, not a full healer and not an army of independent tanks.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Use every tree on a boss with no adds and no physical corpses.
2. Run several formations without multiplying player participation, procs or raid equipment bonuses per decorative unit.
3. Move an encounter out of a bone pattern and resolve its cost, remaining effect and recovery visibly.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
