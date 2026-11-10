# Inquisitor

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A disciplined investigator exposes a visible weakness, builds Conviction and chooses a judgment, countermeasure or absolution. Its identity must come from readable preparation and decisions rather than a renamed holy melee rotation.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Judgment](#judgment) | Melee DPS |
| [Interrogator](#interrogator) | Pure support |
| [Absolver](#absolver) | Healer |

**Equipment proposal:** Medium/heavy armor candidates; weapon and judgment focus, with branch-specific restrictions to evaluate.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Conviction is earned by valid class actions against an investigated threat or through the healer/support tree's own valid contribution. A target observation has an owner, duration and consumption state.

**State progression:** Observe → expose a bounded weakness → build Conviction → deliver or reserve judgment → observation expires or is consumed.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Judgment

**Primary role:** Melee DPS. **Design status:** proposed tree specification.

**Decision loop:** Observe a priority threat, build Conviction through weapon actions and choose when to consume its exposure for a focused judgment.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Expose Weakness | Mark a legal target using visible encounter information. | Limited active observations; no secret server-stat requirement. |
| Conviction Strike | Attack the observed target to build the bounded reserve. | Switching targets preserves costs rather than granting a new free reserve. |
| Final Judgment | Consume Conviction and a valid exposure for focused damage. | Missing exposure produces a defined fallback, not an unreported failure. |

**Talent anchors to allocate:** Early: reliable generation versus a larger held judgment. Middle: sustained exposure or earlier consumption. Capstone: a clearly prepared judgment window with a single shared target budget.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Interrogator

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Read a threat, prepare a countermeasure and spend Conviction to create a short group execution opportunity. Direct damage stays low.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Read Intent | Build an observation through a valid visible enemy action. | No requirement that a boss be susceptible to ordinary crowd control. |
| Stay the Advance | Spend Conviction on a bounded control or prevention tool appropriate to the target. | Respect immunity and diminishing returns; non-control protection is separately budgeted. |
| Coordinated Response | Consume an observation to prepare a limited countermeasure for allies. | No permanent vulnerability aura or mandatory new-class mechanic. |

**Talent anchors to allocate:** Early: faster observation or longer preparation. Middle: narrow protection versus control coverage. Capstone: a finite coordinated countermeasure, not full group damage amplification plus full defense.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Absolver

**Primary role:** Healer. **Design status:** proposed tree specification.

**Decision loop:** Build Conviction through valid triage, choose a protected ally and spend the reserve on direct recovery or a reviewed cleansing response.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Measured Absolution | Heal an eligible ally and generate bounded Conviction. | No resource from avoidable self-arranged damage loops. |
| Protective Judgment | Commit reserve to one finite protective response. | Competes with direct healing; does not grant encounter immunity. |
| Release Burden | Spend preparation to heal and, if selected, remove one reviewed effect category. | Not every dispel category at once; other group solutions remain valid. |

**Talent anchors to allocate:** Early: efficient preparation or emergency release. Middle: protection emphasis versus restorative output. Capstone: a limited triage sequence that consumes the reserve and retains healer-resource pressure.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

Bosses and enemies with no hidden information still support the core loop. A failed investigation cannot require external databases; control immunity removes only the invalid control component, not every meaningful action.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Judgment supplies melee damage, Interrogator trades damage for pure utility and Absolver supplies healing. Religious or faction flavor requires a coherent introduction, not a compulsory race or allegiance lock.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Use the full rotation on a boss with no hidden clues and immunity to ordinary control.
2. Run two Inquisitors without stacking permanent group vulnerability beyond the intended allowance.
3. Swap target or lose line of sight during a judgment and verify visible costs and recovery.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
