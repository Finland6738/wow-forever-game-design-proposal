# Dark Ranger

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A ranged combatant sequences marks and shadow actions, choosing precise consumption, sustained spectral pressure or control-focused support. Darkness is a visual theme; the mechanical identity must come from its mark decisions.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Shade Archer](#shade-archer) | Ranged DPS |
| [Spectral Marks](#spectral-marks) | Ranged magical DPS |
| [Banshee Caller](#banshee-caller) | Pure support |

**Equipment proposal:** Medium armor candidate; bow or another explicitly reviewed ranged weapon.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Quiver/mark charges form a bounded personal reserve. Each mark has a target, remaining duration and consumption state. A spectral action draws from the owner budget rather than creating an uncapped helper system.

**State progression:** Aim/mark → generate or commit charge → sustain or consume → recover. Support prepares a limited spectral signal instead of receiving full mark damage for free.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Shade Archer

**Primary role:** Ranged DPS. **Design status:** proposed tree specification.

**Decision loop:** Prepare one priority mark, build charges through deliberate shots and consume it for focused shadow/weapon damage.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Shadowed Shot | Deal a valid ranged hit and generate a charge. | Normal range/line-of-sight and resource cap. |
| Pursuit Mark | Commit a bounded owned mark to a target. | No permanent player tracking or stealth reveal by default. |
| Piercing Shade | Consume mark and charges for a focused release. | One payload per commitment; no visual-hit proc multiplication. |

**Talent anchors to allocate:** Early: reliable charge generation or longer mark retention. Middle: sustained precision versus earlier release. Capstone: a finite marked-target window rather than permanent vulnerability.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Spectral Marks

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Maintain a small set of spectral marks, decide how to divide pressure and consume a selected mark when a target or phase becomes important.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Spectral Arrow | Build the bounded mark resource through ranged play. | No reserve from harmless repeated targets. |
| Haunting Mark | Apply finite persistent pressure to an eligible target. | Owned target cap and clear dispel category. |
| Echo Release | Consume selected remaining mark potential for a reviewed release. | Prevents full future DoT plus free full burst. |

**Talent anchors to allocate:** Early: retention versus active generation. Middle: focused haunting or bounded spreading. Capstone: a finite spectral sequence sharing one total damage allowance.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Banshee Caller

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Gather a limited spectral readiness through active actions, prepare a cry and choose enemy disruption or a protective group response.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Gather the Echo | Build readiness with a modest active ranged action. | No full DPS rotation remains alongside support output. |
| Disrupting Cry | Spend readiness on reviewed fear/silence-style control. | Categories are selected individually; immunity and diminishing returns apply. |
| Veil of Resolve | Use the prepared echo for finite protection or a recovery opportunity. | Not possession, full healing or encounter immunity; useful on control-immune bosses. |

**Talent anchors to allocate:** Early: readiness pace or retained preparation. Middle: disruption versus protective response. Capstone: a finite echo sequence with one shared support budget.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

Dispel, immunity, stealth and line-of-sight policies remain explicit. A target disappearing cannot duplicate a mark's release or give a full spent-payload refund. No undead racial requirement is selected.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Shade Archer and Spectral Marks are ranged damage trees; Banshee Caller is pure support. A spectral theme does not grant invulnerability, player possession or an automatic extra summon class.

Apply permanent equipment, finite Runes and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Dispel or consume a persistent mark and reconcile its remaining damage exactly once.
2. Lose a marked target to range/stealth/phase change and retain an understandable recovery rule.
3. Use the support tree against a boss immune to fear without giving it a control-immunity exception.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.
