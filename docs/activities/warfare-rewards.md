# Warfare Reputation and Cosmetics

[← Faction Warfare](faction-warfare.md) · [Model Comparison](warfare-models.md) · [Rewards](../11-rewards-and-acquisition.md)

## Selected direction

Base banners, cloaks and mounts remain permanently owned. City crests and themed variants require eligible current service/standing; an ineligible treatment falls back to its neutral base. Neither service nor city cosmetics increase combat statistics or mount speed.

Guilds are trans-city: friends may serve different cities in the same guild. City combat flags are voluntary, activated/deactivated through the NPC for Warfare. Ordinary faction PvP rules remain separate.

## Two city-change routes chosen by the player

At each eligible service change, the NPC presents both routes and their consequences before confirmation. **XP here means the departed city's Warfare standing, not character level, ordinary PvE experience or Honor.** The destination uses its own retained city ledger, or zero if never served.

| Route | Standing cost | Military eligibility |
| --- | --- | --- |
| Social transfer | Preserve accumulated city standing | Political/territorial quarantine: cannot claim conquests or receive conquest-victory credit; can flag, fight and play with friends |
| Immediate military transfer | Lose 50% of the current standing of the city being left | No new quarantine from this transfer; ordinary safe-state/anti-exploit requirements still apply |

The 50% route is multiplicative per applicable departure: 1,000 becomes 500; departing that city again later would halve its then-current balance. It does not reset every city or remove owned base cosmetics. The NPC previews retained standing and inactive treatments.

Quarantine duration is **open**; fourteen days was an example, not adopted tuning. Joining a guild, playing PvE or merely toggling the combat flag does not trigger a service-change penalty. No loss applies to the social transfer route.

## Quarantine boundaries and anti-abuse

Quarantined players may accompany friends, fight and participate in ordinary permitted activities. Their presence cannot award a new city's territorial claim or conquest-victory payout through a proxy. Exact treatment of non-conquest participation XP remains open and must be shown before transfer.

Voting or political victory currencies are not implemented proposal systems merely because they appeared as examples; if added later, quarantine eligibility must cover them explicitly.

Recommended anti-bypass rule: an already active quarantine persists across additional transfers until its original expiry. Choosing a later 50% transfer does not silently clear a restriction already incurred. This requires a visible persistent state and author/implementation review alongside other claim safeguards.

The immediate route is not inherently a complete abuse solution: a character with little standing has little to lose. Both routes still need capture occurrence records, anti-trading checks, role-aware contribution and safe change restrictions. Changing service cannot clear combat, hostile responsibility, an active capture or cooldowns.

## Base ownership and live eligibility

| Element | Permanent ownership | Current-service requirement |
| --- | --- | --- |
| Base banner / cloak / mount | Retained | None for neutral form |
| City crest / themed variant | Acquisition history retained | Eligible current service and standing |
| Warfare standing | Separate city ledgers | Changes only through valid activity or the selected transfer route |
| Combat indication | Follows authoritative current relation | Never inferred solely from a cosmetic crest |

No mathematical below-first-reward reset is assumed. Halving a high standing may leave it above several thresholds; the current-service rule separately controls use of the departed city's treatment. An inactive crest does not remove the underlying mount or item.

## Evaluation

Measure transfer route choices, regrouping with friends, low-standing switching abuses, time to military eligibility, capture trading and understanding of both ledgers. Test transitions during combat, relogging, boundary crossing and repeated NPC interactions. The design balances voluntary social movement with territorial integrity; its durations and thresholds are not validated yet.
