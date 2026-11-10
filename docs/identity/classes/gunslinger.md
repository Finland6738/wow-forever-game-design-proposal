# Gunslinger

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A deliberate ranged fighter manages ammunition, release timing and reload position. Precision should reward planning within ordinary MMO latency tolerance rather than demand frame-perfect rhythm inputs.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Sharpshooter](#sharpshooter) | Ranged physical DPS |
| [Trickshot](#trickshot) | Ranged physical DPS |
| [Gunmarshal](#gunmarshal) | Pure support |

**Equipment proposal:** Light/medium armor; firearm subtype and dual-pistol asset/itemization support require an explicit decision.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Ammunition is a bounded combat reserve. Reload has a committed state and a known completion/cancellation rule. A precision window is evaluated on the server with a published timing tolerance.

**State progression:** Loaded → aim/fire → ammunition spent → reload or reposition → loaded. A dash or cancel cannot independently reset every state or duplicate a shot.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Sharpshooter

**Primary role:** Ranged physical DPS. **Design status:** proposed tree specification.

**Decision loop:** Manage remaining ammunition, prepare a deliberate shot and choose release timing before moving to a safe reload.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Measured Shot | Spend ammunition on reliable ranged damage. | Valid range/line of sight and one shot event. |
| Precision Release | Commit an aimed shot with a readable, latency-tolerant release window. | Missing the preferred timing has a usable fallback rather than zero ordinary output. |
| Tactical Reload | Restore ammunition through a committed recovery action. | Cancellation cannot preserve completion while gaining free movement. |

**Talent anchors to allocate:** Early: reserve management versus reload efficiency. Middle: deliberate single-target timing or safer fallback. Capstone: a finite precision sequence with bounded ammunition and no perfect-input requirement.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Trickshot

**Primary role:** Ranged physical DPS. **Design status:** proposed tree specification.

**Decision loop:** Spend ammunition on planned angles/short-range patterns, reposition and choose whether to unload the remainder before reloading.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Ricochet Shot | Fire a reviewed bounded multi-target action. | No unlimited chaining or proc multiplication per visual bounce. |
| Evasive Volley | Use a limited movement-and-fire response. | Legal destination and shared ammunition prevent infinite kiting. |
| Quick Reload | Trade a cooldown/resource opportunity for an earlier reload window. | Cannot reset every mobility and burst tool at once. |

**Talent anchors to allocate:** Early: movement tolerance or ammunition retention. Middle: focused trick sequence versus bounded spread. Capstone: a short planned volley that consumes its real ammunition budget.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Gunmarshal

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Build a limited readiness reserve through active ranged cues, prepare suppression or cover and release it to help teammates execute.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Ranging Signal | Use a modest shot/cue to build readiness. | No full DPS rotation remains free alongside support output. |
| Suppressing Pattern | Commit readiness to reviewed local control. | Respect boss immunity and diminishing returns; protection uses a separate valid mode. |
| Covering Signal | Spend the prepared reserve on finite protection or regrouping utility. | Not physical collision walls or permanent group damage amplification. |

**Talent anchors to allocate:** Early: quicker preparation or longer retention. Middle: suppression versus cover emphasis. Capstone: a short coordinated cover window with a finite shared allowance.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

Interrupted reload and movement during aim have clear outcomes. Target death before a committed shot follows the projectile policy. Ammunition is a class resource, not a recurring profession shopping requirement.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Sharpshooter and Trickshot are ranged damage; Gunmarshal is pure support. Support trade-offs must be real, not full gun damage with free group utility.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Release precision shots under representative latency without a frame-perfect success cliff.
2. Interrupt reload, dash and reconnect without duplicated ammunition or cooldown resets.
3. Use Gunmarshal against a control-immune boss while preserving viable traditional group completion.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
