# Arenas and Gladiator Standing

[← PvP](pvp.md) · [Recognition](../08-prestige-ranks.md) · [Challenge Dungeons](challenge-dungeons.md)

## Identity and scope

Gladiator is the arena-competition domain, separate from accumulated Honor and time-based dungeon Challenger standings. The selected formats are 1v1, 2v2 and 5v5 with explicit premade topology. Five-player arena combat is not a dungeon composition rule.

## Queue topology

| Queue profile | Team construction | Opponent construction |
| --- | --- | --- |
| Duel | One solo player | One solo player |
| Duo premade | One group of two | One group of two |
| Duo assembled | Two solo players (1+1) | Two solo players (1+1) |
| Full team | One group of five | One group of five |
| Split team | One duo plus one trio (2+3) | One duo plus one trio (2+3) |

Match within the declared profile: do not silently fill a duo against a premade or place 2+3 against a five-stack because a queue is slow. Other topologies, such as five independent solo players, are not selected here. Capacity, party-role constraints and queue availability require population testing; no short queue time is guaranteed.

## Rating and visible progression

**Recommended implementation:** hidden skill MMR for opponent selection, visible tiers/divisions and Arena Points for progression, with separate rating records per queue profile. Use wins/losses, uncertainty and placement calibration rather than accumulated kills, Rune completion or PvE gear ownership. Exact formula, placement count, division thresholds, rank names and seasonal reset policy remain open.

The design reference is the separation of MMR and visible rank described by [Riot's official explanation](https://support.riotgames.com/en-us/league-of-legends/gameplay/mmr-rank-and-lp). The five queue topologies above are this proposal's arena formats, not a claim that Riot operates these modes. Unlike a broad preference for similar premades, our selected topology is an explicit matching boundary.

Preserve match history and earned historical recognition across future rank seasons. Current competitive rank may change with results; it grants no combat statistics. Gladiator title criteria are separate from choosing visible tier labels. Avoid using Challenger as an Arena tier name in this project because it already identifies dungeon competition.

## Matchmaking, integrity and recovery

Match by skill estimate, uncertainty, declared premade profile, compatible latency and any approved role constraints. A mixed duo/trio needs a team-strength model that considers all participants, not only the party leader. Repeated opponent selection, collusion, account abuse, disconnects and abandoned matches need explicit policies and review evidence.

1v1 can expose class/role mismatches and healer stalemates; define duration, draw and allowed-build policy before claiming it balanced. Balance it separately without assuming 2v2/5v5 results prove duel fairness. Do not introduce hidden forced wins/losses or change combat power to hit engagement targets.

## Combat boundaries

Raid-unlocked talents are inactive in every Arena queue and battleground. Rune history grants no numerical power. Ordinary equipment, class talents, racials, consumables and support-role interactions still need a versioned competitive profile. The raid-entry preset is not automatically an Arena template.

Arena participation does not activate city service or the Warfare flag. City standing and conquest eligibility do not affect MMR. Tests must compare compositions and class matchups for each queue independently before rollout.
