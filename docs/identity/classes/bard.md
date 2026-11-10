# Bard

[← Class catalog](../classes.md) · [Roles](../class-roles-and-specializations.md) · [Implementation standard](../implementation-standard.md) · [Mechanic coverage](../mechanic-coverage.md)

**Status:** reviewable implementation specification. Three talent trees per class are selected. The named kits below are proposed designs; engine behavior, tuning and final talent allocations still require the evaluation package in the implementation standard.

## Combat identity

A performer makes timing and commitment the central combat decisions. Phrases are prepared through active actions, then resolved as utility, healing or ranged magic according to the chosen talent tree. This is not a passive buff character parked outside the fight.

## Roles and equipment

| Talent tree | Primary responsibility |
| --- | --- |
| [Conductor](#conductor) | Pure support |
| [Cantor](#cantor) | Healer |
| [Deep Cantor](#deep-cantor) | Ranged magical DPS |

**Equipment proposal:** Light armor; instrument focus with a reviewed weapon loadout.

The roles describe different build responsibilities, not three full kits active simultaneously. Armor and weapon eligibility are prototype decisions; they do not establish a stronger equipment budget or exclusive race requirement.

## Shared resource and state model

Tempo is a bounded personal reserve. Valid performances generate it; a phrase commits part of it until release or cancellation. A committed phrase cannot also be spent on another effect.

**State progression:** Mobile preparation → phrase committed → performance released or interrupted → recovery. Deep Cantor adds an anchored remote-focus state while the owner's body remains exposed.

The server accepts one action only after target, range, line of sight, ownership and resource checks. A committed action records its spend once; subsequent hits, visuals and callbacks resolve against that commitment rather than creating new resources or rewards automatically.

## Talent-tree specifications

### Conductor

**Primary role:** Pure support. **Design status:** proposed tree specification.

**Decision loop:** Build Tempo with active cues; choose a prepared protection, control or movement phrase; hold or release it for a visible group window. Its own attack is modest, and utility consumes the same finite reserve.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Opening Cue | A valid ranged cue generates Tempo and identifies a local focus target. | No resource from repeated harmless interactions or friendly target loops. |
| Sheltering Cadence | Commit Tempo to a short, visibly bounded protective area. | Move out, interrupt preparation or force an earlier release; protection has a finite allowance. |
| Marching Signal | Consume a phrase for a brief regrouping/movement opportunity. | Does not cross encounter walls or remove every positioning constraint. |

**Talent anchors to allocate:** Early: improve phrase retention at slower generation. Middle: choose broader coverage or a stronger narrow response. Capstone: release a short coordinated utility sequence that consumes the prepared reserve, not a permanent group damage multiplier.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Cantor

**Primary role:** Healer. **Design status:** proposed tree specification.

**Decision loop:** Generate a measured phrase with direct triage, then spend it on a targeted restorative sequence or a limited group refrain. Decide whether to heal immediately or prepare for the next damage event.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Mending Note | Heal a valid ally and build a bounded phrase resource. | Consumes the healer's normal resource; overhealing cannot create infinite Tempo. |
| Restorative Refrain | Commit the phrase to a limited healing sequence on eligible allies. | Target cap, range and interruption remain explicit. |
| Closing Chord | Spend the remaining phrase for emergency single-target healing. | Sacrifices the prepared group option; cannot heal Artificer constructs. |

**Talent anchors to allocate:** Early: favor efficient single-target preparation or faster emergency response. Middle: choose group coverage versus focused throughput. Capstone: a committed recovery refrain with a visible interruptible window and a reviewed healing budget.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

### Deep Cantor

**Primary role:** Ranged magical DPS. **Design status:** proposed tree specification.

**Decision loop:** Move to a safe position, enter a stationary singing posture and direct a remote wisp/focus. Leave the posture to reposition; the owner remains targetable and must still handle mechanics.

| Baseline action | Trigger / state change | Guard, trade-off and counterplay |
| --- | --- | --- |
| Anchor Focus | Enter the stationary posture and place a bounded remote focus within legal range. | The focus cannot cast through geometry or remove the owner's vulnerability. |
| Tidal Phrase | Channel ranged pressure through the focus, consuming Tempo. | Both owner-to-focus and effect-to-target targeting rules must remain valid. |
| Break the Song | End the channel and recover movement with a limited defensive response. | No invulnerable indefinite remote play or free channel reset. |

**Talent anchors to allocate:** Early: quicker setup versus greater committed efficiency. Middle: a narrower mobile fallback or stronger anchored sequence. Capstone: a finite remote-release window that still ends when the owner must move or is controlled.

These anchors describe node behavior and opportunity costs, not an approved complete point grid. Define ranks, depth, prerequisites and cross-tree interaction before implementing the full tree. The baseline actions constitute the minimum loop to test first.

## Failure, interruption and recovery

An interrupted performance keeps already-paid costs under the published partial-refund rule. Movement cancels an anchored channel rather than teleporting its source; target or line-of-sight loss prevents new deliveries.

Target death, owner death, encounter reset, dispel and reconnect must use published recovery rules. An action that delivered its full benefit cannot also return its entire unused cost. Distinguish a canceled commitment from a spent one, and expose the result in the interface.

## Group and activity integration

Conductor must contribute against a boss immune to ordinary crowd control. Cantor is evaluated as a healer, while Deep Cantor is evaluated as ranged DPS; mixing talents does not retain all three full outputs.

Apply permanent equipment, milestone Rune unlocks and the one-slot Adventurer Repertoire through the same effective-power review. Normal/Veteran contextual bonuses stay in scope. Owned effects inherit the approved normalized profile, and valid control/protection/objective contribution receives owner-level credit without multiplying player shares.

## Implementation parameters and interface

Before an engine prototype, fill the parameter sheet with resource cap/start state, generation events and rate, action costs, cooldowns, target caps, range/line-of-sight rules, durations, coefficients, control categories and refund/return fractions. The behaviors above constrain those values; none permits an unlimited default.

Display the shared reserve, committed state, selected target and the tree's next important window. Inputs must work at ordinary network latency and without an addon explaining hidden enemy state. Talent respec or equipment swaps cannot preserve mutually exclusive active benefits or reset encounter allowances.

## Acceptance scenes

1. Cancel an anchored performance during a movement mechanic and resume without an invulnerability or cooldown exploit.
2. Complete the same ordinary boss with and without Conductor, using both accepted five-player compositions.
3. Interrupt a prepared heal and verify clear cost, recovery and contribution feedback.
4. Exercise death, reconnect, target loss and encounter reset with no duplicate spend, proc, reward or free cooldown reset.
5. Compare baseline and normalized profiles, including representative Rune/repertoire interactions and any contextual raid bonuses.
6. Allocate mixed-tree builds at the approved level-60 talent budget; verify they do not combine full role outputs or bypass a capstone's intended opportunity cost.

## Implementation handoff and open decisions

The first deliverable is the shared resource/state loop plus the three baseline actions for one tree. Demonstrate it in a single-target scene, a multi-target pull, movement, failure recovery and counterplay, then expand the other trees against the same contribution contract.

The final point grid, coefficients, equipment restrictions, animation/effect costs, race/class matrix and competitive policies remain open. Review measured output, survival, resource pressure, input load, readability and group access before promoting this specification to a validated implementation candidate. The [standard](../implementation-standard.md) defines the evidence gate.

## Shared progression boundary

These are ordinary class talent-tree abilities, usable according to their own combat rules. The separate final-boss Adventurer Repertoire reward slot works only in matching-difficulty raids (Normal to Normal, Veteran to Veteran), never in dungeons, open world or PvP. Rune milestone records grant no cumulative combat statistics. Apply the [shared implementation standard](../implementation-standard.md) to this kit and its hybrids.
