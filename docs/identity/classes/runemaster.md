# Runemaster

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A Runemaster prepares a small arrangement of combat sigils, then chooses whether to trigger or reconfigure it. Melee inscription, school selection and application/consumption of a cold state are distinct talent-tree loops.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Runeblade](#runeblade) | Melee magical/weapon DPS |
| [Rune Scholar](#rune-scholar) | Ranged magical DPS |
| [Rime Scholar](#rime-scholar) | Ranged magical DPS with control |

**Equipment proposal:** Branch-reviewed armor; an inscribed weapon or caster focus. Rune Scholar/Rime Scholar begin from a caster profile.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Combat sigils are bounded class charges, entirely separate from completion-based Rune milestones. A prepared arrangement records school, target/state eligibility and whether its next enhancement has been consumed.

**State progression:** Prepare arrangement → generate sigil charges → select school/mark → trigger or reconfigure → recover. Rime damage-state stacks remain distinct from slow/root control flags.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Runeblade

**Primary role:** Melee magical/weapon DPS. **Design status:** proposed tree specification.

**Decision loop:** Prepare a compact inscription, generate charges through weapon actions and choose a triggered strike or a costly reconfiguration.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Inscribe Edge | Select one reviewed arrangement for the current weapon sequence. | One active arrangement; changing it has an explicit cost. |
| Sigil Cut | Use melee attacks to build the bounded class-charge reserve. | No usage-based Rune reward generation or free duplicate procs. |
| Release Inscription | Consume charges through a prepared strike. | A charge enhances one valid action, not every visual component. |

**Talent anchors to allocate:** Early: steadier charging or greater arrangement retention. Middle: sustained inscriptions versus a stronger triggered release. Capstone: a finite inscribed sequence with a reviewed reconfiguration cost.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Rune Scholar

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Generate class sigils, select a school and cast a spell through that school, consuming an enhancement on the next eligible action. The selection is meaningful preparation, not extra button presses for an identical result.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Gather Sigil | Deal a valid ranged action and build class charges. | Fixed cap; no relation to permanent Rune milestone record. |
| Choose School | Select a proposed Nature, Arcane or Holy-themed offensive palette. | Exact schools need setting review; direct bindings can preserve accessibility without changing the decision. |
| Inscribed Spell | Cast the selected school's reviewed action and consume its eligible enhancement. | School choice does not grant full healing and full support alongside ranged DPS. |

**Talent anchors to allocate:** Early: faster preparation or retained charges. Middle: specialize a school or retain broader flexibility at a cost. Capstone: a finite prepared-school sequence with one enhancement ledger.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Rime Scholar

**Primary role:** Ranged magical DPS with control. **Design status:** proposed tree specification.

**Decision loop:** Apply a bounded cold damage state, shape nearby threats where control is legal and choose when to consume the state for a planned area release.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Rime Cast | Apply or build the owned finite Rime state through ranged damage. | Damage-state eligibility is separate from slow immunity. |
| Cold Pattern | Add a reviewed slow/control component to eligible targets. | Respect control caps, immunity and diminishing returns. |
| Shatter Rime | Consume selected owned state potential for bounded damage. | Cannot retain the full state and receive a free full detonation; target cap is explicit. |

**Talent anchors to allocate:** Early: state retention or active application. Middle: focused consumption versus limited area shaping. Capstone: a finite shatter window, with a mobility response that does not become invulnerable sliding.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

A control-immune boss can still receive an eligible damage-state marker. School reconfiguration cannot preserve an enhancement from every school simultaneously. Reconnects restore consumed charges rather than duplicating them.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Runeblade is melee damage; Rune Scholar and Rime Scholar are ranged magical damage. The school-selector and apply/consume-cold studies are fully represented without claiming a second permanent Rune system.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Consume Rime on a slow-immune boss while preserving the correct damage/control separation.
2. Switch schools with a primed enhancement and apply it only once under the declared eligibility rule.
3. Verify that combat sigils never change Rune milestone ownership or reward scope or bypass Challenge normalization.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
