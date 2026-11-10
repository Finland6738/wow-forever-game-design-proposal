# Oracle

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

The Oracle predicts a visible event and chooses when to spend a prepared response. A personal burden changes timing or resource decisions; it must not impose random unmanageable damage on teammates.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Seer](#seer) | Healer |
| [Omen](#omen) | Pure support |
| [Doomweaver](#doomweaver) | Ranged magical DPS |

**Equipment proposal:** Light armor; staff or caster focus.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Foresight is a bounded reserve committed to an Omen. A prediction records its trigger category, eligible target, expiry and whether it has resolved. An unused prediction has a defined partial recovery path.

**State progression:** Choose an Omen → prepare → trigger occurs or prediction expires → resolve once → recover. A burden modifies this loop through an explicit trade-off.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Seer

**Primary role:** Healer. **Design status:** proposed tree specification.

**Decision loop:** Triage an ally, prepare a forecast for a likely damage event and choose whether to hold it or spend it immediately as a smaller direct recovery.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Mending Vision | Heal a valid ally and gather Foresight. | Ordinary healer resource costs remain effective. |
| Forecast Harm | Commit Foresight to a bounded restorative trigger. | Published trigger and expiry; no automatic immunity. |
| Resolve Vision | Consume the unused forecast for a defined direct-heal fallback. | Lower flexibility/output than perfectly timed use; cannot receive both payouts. |

**Talent anchors to allocate:** Early: safer expired-forecast recovery versus stronger commitment. Middle: individual triage or small-group prediction. Capstone: a prepared recovery sequence with a visible shared allowance.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Omen

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Prepare a protection or countermeasure forecast, read the next phase and release it to help allies execute without supplying full healing or damage.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Read the Turning | Use an active valid cue to build Foresight. | Must work in boss-only phases; no idle resource farm. |
| Shelter Omen | Commit reserve to finite prevention for a defined event window. | Target cap and prevention ceiling remain visible. |
| Unravel Portent | Spend an unused omen on a limited cleanse, control or positioning response. | Choose the response category in the build; not all tools at once. |

**Talent anchors to allocate:** Early: faster preparation versus longer omen retention. Middle: reactive countermeasure or deliberate shelter. Capstone: a finite group forecast that consumes all committed preparation and respects encounter rules.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Doomweaver

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Accept a reviewed personal burden, place an offensive omen and choose a release window before expiry. Predictions reward encounter reading without requiring a target to attack the caster.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Ominous Bolt | Deal ranged damage and build Foresight. | Target and line-of-sight checks apply normally. |
| Doom Forecast | Commit reserve to a visible delayed offensive condition. | No unavoidable infinite-duration trap on players. |
| Fulfill Portent | Consume the valid forecast for a timed damage release. | Cannot also cash out its full unused future payload. |

**Talent anchors to allocate:** Early: reliable expiry fallback or a higher commitment window. Middle: focused release versus bounded spreading. Capstone: a short personal burden/release cycle with a defined exit and no healer-subsidized infinite damage.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

A prediction cannot resolve twice from duplicate damage callbacks. Missed predictions do not make a first encounter unplayable; control immunity does not remove the class's whole support role.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Seer is a healer, Omen is pure support and Doomweaver is ranged damage. Prevention and healing share clear contribution accounting; no hidden healing-role output is added to the support tree.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Miss a forecast during a first boss attempt and recover into a useful normal loop.
2. Replay the same trigger event and grant only one prediction result.
3. Measure Omen contribution on a control-immune boss in the support and traditional group patterns.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
