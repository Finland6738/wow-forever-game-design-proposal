# Identity Implementation Specification

[← Classes](classes.md) · [Races](races.md) · [Mechanic coverage](mechanic-coverage.md) · [Roles](class-roles-and-specializations.md)

## Purpose and evidence level

The dossiers specify behaviors that a gameplay or character team can evaluate and turn into a bounded prototype. They separate **author-selected constraints**, **proposed kit decisions** and **unmeasured parameters**. A complete document is not evidence that a model fits armor, a class is balanced or an engine supports a particular interaction.

| Stage | Evidence required | Current claim |
| --- | --- | --- |
| Design specification | Fantasy, responsibility, state model, inputs, outputs, failure behavior and acceptance scenes | The individual dossiers provide this review package |
| Implementation spike | A working representative loop or wardrobe/animation prototype in the target engine | Not performed in this repository |
| Validated implementation candidate | Measured role performance, interaction tests, asset coverage, accessibility and a reviewed content integration plan | Not yet established |
| Production readiness | Approved tuning, complete assets, localization, regression results, support/operations and release review | Not claimed |

The intended handoff is concrete: an implementer should understand what to build and what would constitute success. Remaining tuning belongs to named configuration parameters rather than invented claims of finished balance.

## Class and talent-tree contract

Each of the **eighteen candidate classes has exactly three proposed talent trees**. The three-tree structure is selected; most individual kits are recommendations for author/developer review. Summoner's Swarmcaller, Soulbinder and Sporekeeper identities, and the Artificer tank's core behavior, have already been selected by the author.

These are **Vanilla-style talent trees**, not an assumption of a later specialization interface. The first prototype uses one tree's identity to isolate its loop. Before shipping, validate the working point budget and define unlock depths, prerequisite chains, capstone access and cross-tree combinations. Do not assume a character cannot mix talents simply because the document lists trees separately.

**Selected working profile:** 51 talent points at level 60, with a capstone reached at 31 invested points in one tree. For a one-point capstone, its purchase follows 30 points already invested. This is a proposal reference to validate against the actual Forever system, not a verified current-game rule. Node ranks, tier gates and prerequisites still need allocation.

Evaluate at least 31/20/0, 30/21/0, 21/21/9 and 17/17/17. Two 31-point capstones require 62 points and cannot fit this profile; powerful intermediate combinations still require testing.

Each shared resource needs an owner and a maximum. Each ability specifies a trigger, target rule, cost/commitment, result and recovery/counterplay. Damage, healing, protection and pets all count toward the equipped build's total contribution. A support-oriented tree trades direct output for active utility; mixed talents cannot retain every tree's full output.

The existing role contract remains: tank, healer, DPS and pure support. Physical/magical and melee/ranged are delivery descriptors. Both 1 tank + 1 healer + 3 DPS and 1 tank + 1 healer + 2 DPS + 1 support must remain viable in ordinary five-player content. Bruiser is deferred.

## Runtime behavior contract

| Concern | Required behavior |
| --- | --- |
| Authority | The server validates resources, targets, range, line of sight, ownership and ability state |
| Commit point | Invalid targets fail before spending; an accepted action spends once; delivery and refund policy are explicit |
| Proc accounting | Decorative units, copied hits and repeated callbacks cannot multiply a single entitlement unexpectedly |
| Control and immunity | Crowd-control flags and diminishing returns remain effective; damage-state stacks can be separate from a slow/root |
| Target death/range loss | Cancel, resolve or return unspent commitment under a visible rule; no full refund after full benefit |
| Death and reset | Stop new owned commands; preserve encounter/cooldown integrity; encounter reset has an explicit starting state |
| Movement and pathing | Reject invalid terrain and geometry bypass; show why a placement or command failed |
| Normalization | Owner and owned effects use the approved Challenge/Arena profile; scoped raid bonuses remain scoped |
| Credit | Tanking, healing, control, prevention and objective contribution are attributed to one owner, once |

The dossiers describe **conceptual states**, not existing Blizzard API names, database schemas or client fields. The implementing team maps these behaviors to the actual engine after investigation.

## Parameter and talent handoff

Every kit requires a reviewed parameter sheet: resource capacity/start state, generation, action cost, target cap, duration, range, cooldown, effect magnitude, control category and recovery/refund policy. The documents name the behavior these parameters control. An unset coefficient is an evaluation task, not permission to choose an unlimited value.

Do not announce a full launch talent grid from a handful of concept actions. The required next artifact is a tree allocation sheet: each node's rank count, prerequisite, unlock depth, modified action, output trade-off and cross-tree interaction. Test capstone access and common hybrid builds at the level-60 point budget before claiming that one tree has a complete standalone balance profile.

## Race and equipment handoff

All ten established race candidates have an individual dossier and the same selected boundaries: a neutral introduction, Alliance/Horde choice, recognizable anatomy-specific item fitting and the existing permanent power policy. Historical NPC models are visual references, not certified player rigs.

Each race needs a wardrobe matrix across supported body options and relevant cloth/leather/mail/plate items; weapon grips and sheathing; movement, casting, combat, sitting, death and interaction animations; mount/transport tests; camera, collision and indoor traversal; customization and starting-experience review. Normally invisible slots remain normally invisible.

Keep item identity, slots, set behavior and enchants intact. A tail, extra arm or unusual body does not create free attacks, flight, immunity or additional equipment slots. Race/class combinations and numerical racials remain separate approval decisions.

## Evaluation package

For classes, compare representative baseline builds on a single boss, a control-heavy pack, a moving encounter, a recovery failure and an opponent with counterplay. Repeat with ordinary and normalized profiles and with mixed-tree builds. For support, include a boss immune to ordinary crowd control and compare both selected five-player compositions.

For races, capture the same wardrobe on a baseline playable body and the candidate, document every hidden/adapted item, and test world interaction. Record actual defects rather than substituting cost adjectives for measurements.

Publish the outcome, unresolved defects and the next decision. This makes a dossier a useful implementation handoff while keeping its evidence level honest.
