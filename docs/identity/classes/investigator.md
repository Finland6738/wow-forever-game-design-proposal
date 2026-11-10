# Investigator

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

An Investigator turns visible combat observations into deductions and tools. Every encounter must expose enough ordinary actions to support the loop; hidden data, addons and a secret weakness database are not requirements.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Field Agent](#field-agent) | Melee DPS |
| [Analyst](#analyst) | Pure support |
| [Saboteur](#saboteur) | Ranged DPS |

**Equipment proposal:** Light/medium armor; field weapons and reusable class tools, with delivery fixed per tree.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Insight is bounded and earned by active class actions or eligible visible events. A deduction is a consumable opportunity with a target and expiry. A tool loadout chooses responses rather than granting every tool simultaneously.

**State progression:** Observe → earn Insight → prepare an opening/tool → exploit or counter → recover. Switching targets does not rebuild a free reserve.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Field Agent

**Primary role:** Melee DPS. **Design status:** proposed tree specification.

**Decision loop:** Establish an observation, build Insight through close-range actions and spend a deduction on a timed opening before disengaging or recommitting.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Measured Strike | Attack in melee and gather bounded Insight. | No full melee output outside the intended range. |
| Find Opening | Commit Insight to an owned target opportunity. | Limited duration and active-target count. |
| Exploit Opening | Consume the deduction for a focused weapon action. | The same opening cannot trigger repeatedly from allies or copied hits. |

**Talent anchors to allocate:** Early: stable Insight versus a larger held opening. Middle: retention or faster consumption. Capstone: a finite sequence of deliberate openings with one reviewed total output.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Analyst

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Observe an event, choose a counter-tool and spend Insight to protect, reposition or disrupt for the group. Its own damage remains modest.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Combat Read | Actively gather a valid observation. | No hidden enemy data or compulsory voice instruction. |
| Countermeasure Kit | Spend Insight on the selected protective/dispel tool. | A limited loadout and shared costs prevent having every answer at once. |
| Coordinate Route | Release a prepared tactical window for local movement or control. | No permanent vulnerability debuff, wall bypass or mandatory new-class route. |

**Talent anchors to allocate:** Early: observation speed or storage. Middle: protection emphasis versus field control. Capstone: a finite tactical plan whose benefits expire and consume preparation.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Saboteur

**Primary role:** Ranged DPS. **Design status:** proposed tree specification.

**Decision loop:** Use ranged actions to gather Insight, place a visible device/trap and trigger a planned reaction when the target enters the intended window.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Survey Shot | Deal ranged damage and build Insight. | Weapon type/range is fixed by the prototype profile. |
| Prepared Charge | Commit a tool to a valid ground location. | Visible placement, finite target cap and no placement through walls. |
| Trigger Reaction | Consume a prepared charge for its reviewed payload. | No free full refund after damage; repeated triggers cannot duplicate it. |

**Talent anchors to allocate:** Early: placement recovery or stronger commitment. Middle: direct impact versus a short residual zone. Capstone: a controlled multi-stage reaction with one shared payload budget.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

An enemy with no special cast still permits basic observation through the kit. Invalid placement fails before a tool is spent. Repeated callbacks for one observed event cannot grant several deductions.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Field Agent is melee damage, Saboteur is ranged damage and Analyst is pure support. Their range and resource trade-offs prevent the same build from being best at every distance.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Play a boss with no special hidden vulnerability and retain a complete useful loop.
2. Observe one event twice through duplicated notifications and grant one Insight entitlement.
3. Move a target out of a prepared charge and resolve the stated cost/refund behavior.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
