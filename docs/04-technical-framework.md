# A conceptual framework for scoped power

[← Main proposal](../README.md) · [Documentation index](README.md) · [Evaluation plan](05-roadmap-and-evaluation.md)

> This is a behavior specification and an illustrative data model. It is not production code, an API contract, a database migration, or a description of Blizzard's internal systems. Exact budgets, performance costs and engine integration need investigation.

## Invariants

1. Releasing new content does not automatically raise the approved permanent equipment-power range.
2. An additional raid effect is eligible only for its approved content group, instance and difficulty.
3. Normal and Veteran do not exchange contextual power, power currency or required combat unlocks.
4. A shared update scope cannot require a previous update and must offer self-contained routes within each sibling raid.
5. Challenge Modes use an explicit, versioned effective-power profile with no external raid or territorial effects.
6. Participation and effect eligibility are authoritative server decisions.
7. Transitioning contexts cannot preserve otherwise ineligible effects or produce duplicate progression/reward claims.

Invariants 1 and 4 include balance and acquisition claims. A validator can enforce identifiers and caps, but cannot prove that an item interaction or a social gearing expectation is acceptable. Those require analysis and playtesting.

## Suggested separation of concerns

| Component | Responsibility |
| --- | --- |
| Permanent item profile | Defines approved base stats, weapon/armor properties and permanent effects |
| Contextual effect definition | Declares scope, difficulty, effect family, budget cost and interaction rules |
| Progression ownership | Records which character earned a local unlock and under what transfer policy |
| Activity policy | Resolves current content group, allowed instances, difficulty and normalization |
| Effect resolver | Produces the server-authoritative effective loadout and derived combat state |
| Reward service | Grants local progression and collections once per valid claim |
| Run validator | Establishes roster, timer, objectives, ruleset and leaderboard eligibility |

These are logical responsibilities. They need not become separate services, tables or new network boundaries.

## Illustrative fields

```yaml
# Fictional identifiers and descriptive budget references; not a proposed engine schema.
item_id: ancient_guardians_breastplate
required_level: 60
permanent_profile_id: plate_tank_sidegrade_01
base_power_budget: level_60_permanent_v1
contextual_effects:
  - context_bonus_id: guardian_resonance
    content_group_id: update_a_raids
    allowed_instance_ids:
      - fallen_observatory
      - vault_of_cinders
    difficulty_id: normal
    effect_family: raid_defensive_choice
    context_budget_id: update_a_normal_v1
    stacking_rule: exclusive_with_same_family
ownership_policy: character_local_progression
```

The `base_power_budget` reference is not a single scalar guaranteed to predict combat performance. Its definition needs role-specific constraints, effect catalogs and empirical validation. The same applies to contextual budgets.

Activity state separately declares the current instance, difficulty, content group, policy version and optional `normalization_profile`. Do not trust a scope identifier supplied by a client or inferred from an item tooltip.

## Effect eligibility and effective power

For a contextual effect, the conceptual predicate is:

```text
eligible = owned_by_character
       AND current_content_group == effect.content_group
       AND current_instance IN effect.allowed_instances
       AND current_difficulty == effect.difficulty
       AND activity_policy.permits_contextual_effects
       AND effect_is_approved_for_current_policy_version
```

Eligibility does not mean every matching effect stacks. The resolver must then enforce family exclusions, ownership, per-slot rules and the context budget. Conflicts need deterministic resolution and a clear player-facing explanation.

The resulting combat state is a policy composition:

```text
effective loadout = resolve(
    approved permanent profile OR activity-normalized replacement,
    permitted contextual choices,
    approved temporary effects,
    role/class and interaction constraints
)
```

This is not a damage formula. Multiplicative synergies, uptime, encounter mechanics and stat breakpoints can defeat a naïve sum-of-stats approach. Test build outcomes, not merely data validity.

## A complete power catalog

| Source | Required review |
| --- | --- |
| Weapons and armor | Damage ranges, speed, armor, primary/secondary stats and unusual scaling |
| Trinkets and item effects | On-use effects, procs, cooldown interactions, proc chains and internal cooldowns |
| Set bonuses and enhancements | Conditional activation, sockets, enchants, crafted modifications and stacking families |
| Consumables and temporary buffs | Potions, food, profession effects, regional buffs and expiration behavior |
| Character/account unlocks | Talents and relevant permanent benefits, including any applicable Legacy effects |
| Pets and summons | Inherited stats, snapshot timing, persistent auras and transferred ownership/context |
| Encounter-created effects | Vehicles, special resources, triggered abilities and encounter-specific objects |

New items or effects must have a reviewed policy. For ranked activities, an unknown effect must not silently remain enabled. Provide an approved substitute or prevent a ranked start until the loadout is valid; explain the remedy.

## Context transitions and snapshots

Recompute effective state when a player enters or exits an activity, changes difficulty, equips an item, changes a relevant build, logs in or reconnects, transfers to another event context, or gains/loses an eligible effect. Cache resolved policy where safe, with invalidation tied to authoritative state changes.

Transition handling needs one consistent lifecycle:

1. Resolve the destination activity and policy version from server-owned state.
2. Rebuild the effective loadout, removing incompatible auras and recalculating dependent stats.
3. Revalidate pets, summons, resource maxima and derived effects.
4. Apply the activity's explicit starting-resource or transition policy without granting a heal, cooldown reset or resource duplication exploit.
5. Update the client explanation and persist only the intended progression/ownership state.

Do not mutate the permanent item to represent temporary scaling. Preserve its identity and restore effective behavior outside normalization. Handle rollback and reconnect so a partially completed transition cannot leave mixed policies active.

Snapshotting is especially dangerous. A pet summoned in Update A Normal cannot carry its empowered stats into Veteran, and an aura triggered before leaving a raid cannot keep its effect in the world. Review persistent ground effects, delayed damage, summons, absorbs and cooldown interactions, rather than only clearing the player's visible buff list.

## Challenge run lifecycle

```text
PREPARING -> READY -> RUNNING -> COMPLETED -> VALIDATED
                            -> INVALIDATED
                            -> ABANDONED
```

At ranked start, atomically bind the run ID, dungeon, server roster, normalization profile, encounter/objective version, relevant balance version and starting-state policy. Record authoritative timestamps and progression through required objectives.

A participant replacement marks the active ranked run ineligible; the party can reform and create a new run without a consumed resource. A reconnect by the same character preserves the run and its timer. Reset requests must be idempotent and rebuild encounters, cooldowns, buffs and eligible resources according to the published policy.

At completion, validate objectives, roster history, encounter integrity and ruleset before granting medals or ranking. A duplicate completion request cannot grant another reward. Keep enough evidence to inspect suspicious records, with a retention policy and no unnecessary public account data.

If balance changes materially alter achievable times, archive the old ranking version. A version label alone does not establish fairness: content designers still need to decide whether a fix creates a new competition context.

## Ownership, collections and reward integrity

Collection unlocks and local combat progression have different transfer policies. Account-wide appearances need not imply account-wide power. Trading, mail, auctions, shared storage, duplicate items and item recovery must not bypass contextual ownership.

For an update shared by multiple raids, record progression against the intended update/difficulty budget. Reward duplication across sibling instances, alts or event copies must not increase that cap. Acquisition cadence and loot locking remain design decisions; any chosen implementation must preserve independent Normal/Veteran progression.

An archive or preset system stores references to owned effects. It should not create extra tradable items, duplicate unique effects or activate archived bonuses outside their scope.

## Acceptance matrix

These are proposed implementation acceptance cases, not tests executed against an existing game.

| Case | Expected behavior |
| --- | --- |
| Update A Normal item used in a sibling Update A Normal raid | Approved permanent profile plus eligible capped contextual effect |
| The same item enters Update A Veteran | Permanent profile remains; Normal contextual effect is absent |
| The same item enters Update B | Permanent profile remains; Update A contextual effect is absent |
| The item is worn in the world or a Heroic dungeon | Permanent profile remains; raid progression effect is absent |
| A ranked Challenge Mode starts | Approved Challenge profile; raid and territorial effects absent |
| An old low-item-level trinket has an unapproved proc | It cannot bypass normalization; substitute or ranked-start rejection |
| An empowered pet or delayed effect crosses contexts | Incompatible inherited/snapshotted power cannot persist |
| A character changes gear or difficulty near an encounter transition | One authoritative policy applies; no mixed-state stacking |
| A player reconnects during a ranked run | Same run and character identity; timer continues; no reset advantage |
| A replacement player joins a ranked run | Current ranking attempt invalidated; immediate fresh attempt available |
| Reset/completion requests are repeated | Idempotent state change and a single legitimate reward claim |
| An alt or duplicate item attempts to funnel local power | Ownership and cap rules prevent unauthorized transfer |
| A World Boss reward is acquired in multiple event copies | Event/reward identity prevents duplicate claims |
| A player skips Updates A and B and prepares for C | Accessible baseline route exists with no required earlier raid item |
| A Veteran-only guild prepares for progression | No Normal-only power, currency or unlock is required |
| One sibling raid is skipped | The other retains a self-contained progression path |
| A contextual effect is inactive in the UI | The destination and reason are understandable without internal IDs |

## Operational questions

Before implementation, investigate validation cost under large events, cache correctness, save compatibility, error recovery and policy rollout. Add structured diagnostics for rejected effects, unexpected power deltas and invalid runs. Do not assume the current engine already supports this architecture or that an effect catalog is cheap to maintain.

Major balance corrections should preserve earned collections and use a communicated migration policy for changed contextual effects. A stable long-term budget can still need correction when a combination exceeds its intent; publish why it changes and how affected players can choose an equivalent option.

The largest unresolved risk is effective-power balancing across classes and encounter types. Numeric ceilings and identifiers provide boundaries, while gameplay evidence determines whether those boundaries deliver the promised experience.
