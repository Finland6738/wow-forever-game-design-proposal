# Kobolds — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** Vanilla mine-dwellers such as [Kobold Tunnelers in Elwynn](https://warcraft.wiki.gg/wiki/Kobold_Tunneler). Use the earlier appearance rather than assuming a later redesign.

**Fantasy:** a small underground people with craft, superstition, domestic life and territorial concerns. Mining and candles inform the culture without becoming its entire personality or a compulsory head item.

**Equipment proposal:** keep helmets and weapons readable at small scale. A candle can be optional customization, compatible with adapted headgear. Fit muzzle, curved back, hands, robes and boots without making all items look alike.

**Story proposal:** a community negotiates trade, protection or settlement rights. Give characters motives beyond compulsory mining; an existing profession must not become an exclusive racial function.

**Prototype gate:** camera height, target selection, large weapons, casting, mount seating and ground indicators. Small appearance must not confer special targeting/collision advantages, but enlarging the model into an ordinary humanoid would lose its appeal.

## Scope of the first implementation spike

A genuinely small mine-dwelling silhouette with readable earned items and full player actions.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Headgear | A candle is optional culture/customization, not a compulsory replacement for the equipped helmet. |
| Scale and grips | Weapons, shields and gloves must read at small scale without enlarging every item into an obstruction. |
| Back and feet | Fit hunched robes, cloaks and boots; preserve the character's body rather than burying it in oversized armor. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Check camera height, ranged aim, casting, emotes, swimming and seats. Small appearance must not make targeting or ground-effect feedback substantially harder for opponents.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A mining community loses safe access to part of its home and needs help beyond compulsory labor.
2. The player negotiates protection and trade while resolving a local dispute through group-capable tasks.
3. Faction representatives offer separate affiliations without forcing a mining profession or exclusive economic role.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Candles, whiskers, facial features, markings and practical clothing are options; every head option needs compatible visible helmet behavior.

Underground rituals and light symbolism can shape quests. Mining skill, gathering yield and special PvP target rules are not automatic racial benefits.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Read a targeted cast and ground marker at ordinary combat zoom.
2. Equip a long robe, large weapon and shield without losing the character silhouette.
3. Mount and use transport/interactions without a camera or reach advantage.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).
