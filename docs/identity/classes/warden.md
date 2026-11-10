# Warden

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

The Warden studies pursuit, defensive interception and deliberate counterattacks. The Moon Predator branch preserves two-form combo combat through an automatic internal combat cycle, independently of race and world time.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Moon Predator](#moon-predator) | Melee DPS |
| [Sentinel](#sentinel) | Tank |
| [Duelist](#duelist) | Melee DPS |

**Equipment proposal:** Medium/heavy armor candidates; weapon/shield access evaluated by tree.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Resolve is bounded across the family. Moon Predator adds a bounded combo reserve and a server-owned two-phase combat clock; Duelist adds owned response seals. These are not permanent Rune progression or prestige resources.

**State progression:** Pursuit/guard preparation → valid engagement → build Resolve → spend on a branch action → recover. Moon Predator automatically alternates Hunt and Rend during valid combat; it cannot manually select a preferred form.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Moon Predator

**Primary role:** Melee DPS. **Design status:** proposed tree specification.

**Decision loop:** During Hunt, prepare position and build a small combo reserve; the internal combat clock shifts to Rend, opening predatory spenders and bounded sustain; rebuild as the cycle returns. The player plans around transitions rather than choosing the form directly.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Hunting Sequence | Use valid close-range attacks to build combo preparation in the current phase. | A three-point cap is a source-inspired prototype option, not validated tuning. |
| Predatory Release | Spend the reserve through the current form's attack. | Each form has a useful spender; movement must not make an entire phase unusable. |
| Cycle Transition | Automatically alternate Hunt/Rend on the server's combat timer. | No world day/night dependency, manual form button or free reset by dropping personal combat. |

**Talent anchors to allocate:** Early: reliable cross-phase resource retention or stronger within-phase commitment. Middle: Hunt preparation versus Rend spending. Capstone: a finite transition interaction that does not replace the selected automatic internal cycle with manual form choice.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Sentinel

**Primary role:** Tank. **Design status:** proposed tree specification.

**Decision loop:** Mark a local threat, establish attention and spend Resolve on deliberate guard/facing responses before repositioning.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Sentinel Challenge | Build threat and request a legal taunt. | Ordinary taunt categories/immunity apply. |
| Guarded Intercept | Spend Resolve for a short controlled mitigation/interception window. | Bounded coverage; does not remove all ally mechanics. |
| Hold the Line | Prepare a local defensive anchor with a viable movement release. | No permanent immovable immunity or boss collision exploit. |

**Talent anchors to allocate:** Early: consistent mitigation versus reposition recovery. Middle: focused guarding or limited add control. Capstone: a finite sentinel defense that has a clear end and ordinary tank recovery afterward.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Duelist

**Primary role:** Melee DPS. **Design status:** proposed tree specification.

**Decision loop:** Prepare a response seal, time a parry/counter where permitted and choose a self-contained follow-up or an opportunistic partner trigger.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Set Response | Place a limited owned seal through a normal weapon action. | Works without a particular second player or class. |
| Measured Riposte | Respond to a legal parry/window or use its lower-advantage ordinary fallback. | No infinite instant parry chain; latency-tolerant timing. |
| Joined Follow-through | Consume the seal through a self action or eligible teammate follow-up. | Same bounded payload either way; partner coordination cannot duplicate it. |

**Talent anchors to allocate:** Early: counter reliability or longer seal retention. Middle: independent follow-through or more flexible partner timing. Capstone: a finite riposte sequence whose value does not require a compulsory duo.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

The combat-cycle start/reset policy follows encounter state, not personal combat toggles. Both forms retain responses to movement mechanics. Boss attacks that cannot be parried still permit a valid non-parry builder.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Moon Predator and Duelist are melee DPS; Sentinel is a tank proposal. The two-form and partnered-follow-up studies have clear homes without a required Worgen race or a mandatory named partner class.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Begin fights at different world times and obtain the same internal-cycle rules and starting state.
2. Temporarily lose personal combat during an active boss without resetting phase or combo resources for free.
3. Play Duelist alone and with different teammates without a mandatory partner or duplicate follow-up payload.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
