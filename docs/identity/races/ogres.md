# Ogres — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** Vanilla ogres, including Stonemaul presence around Brackenwall. See [Classic Dustwallow Marsh](https://warcraft.wiki.gg/wiki/Dustwallow_Marsh_%28Classic%29).

**Fantasy:** a large, powerful body with a social identity beyond a hostile camp. Start with a **single-headed** prototype; two heads add helmet, animation and customization questions and are not assumed to be free variants.

**Equipment proposal:** fit the torso and belly, prevent belts and weapons sinking into the body, and check shoulders, robes, shields, helmets and boots. Keep the recognizable build while testing a practical playable scale. An NPC's fixed costume does not prove arbitrary item support.

**Story proposal:** a particular clan or delegation needs agency and obligations. A Stonemaul connection can inform local relationships, but the playable origin must also support an individual's Alliance choice after the introduction.

**Prototype gate:** doors, lifts, ceilings, tank camera and crowded melee. Large appearance must not grant extra reach or an unfair attack footprint. Any scale adjustment needs review before it destroys the intended fantasy.

## Scope of the first implementation spike

A broad single-headed body whose size survives the playable-scale review.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Torso and waist | Fit chest, belts and leg armor over the belly; keep sheathed weapons clear of the body. |
| Head and shoulders | Prove a single-headed helmet solution and both shoulder attachments before researching a two-headed variant. |
| Feet and shields | Demonstrate ordinary foot items, shield facing and large-weapon grips without expanding mechanical reach. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Large motions need readable windup and recovery without slowing actual class inputs. Sitting, swimming, ladders or interaction substitutes, and transport seats require specific tests.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A small clan establishes a refuge whose survival requires cooperation beyond its existing ties.
2. The player handles a shared defense and a diplomatic dispute, showing individual motives beyond brute force.
3. Delegates offer separate Alliance and Horde paths; neither choice changes the allegiance of every Ogre clan.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Faces, body markings, hair and clan adornment can vary. Playable body/presentation options need a real asset plan, not a promise that every NPC variant is free.

Clan ceremonies and communal labor provide cultural hooks. Extra inventory, weapon slots or permanent strength bonuses are not inferred from body size.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Traverse a low doorway, lift and stair turn while armored and carrying a two-handed weapon.
2. Tank with the standard encounter footprint and useful camera clearance.
3. Show chest/robe/waist items at the chosen scale without shrinking away the defining build.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).
