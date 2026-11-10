# Ethereals — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** TBC ethereals, including Consortium figures and the Mana-Tombs appearance. See the [historical Ethereal reference](https://warcraft.wiki.gg/wiki/Ethereal).

**Fantasy:** an energy-bound traveler whose wrappings, equipment and controlled luminosity remain recognizable from the early model. The goal is not to turn every item into an unrelated bandage costume.

**Equipment proposal:** retain standard slots. Test chest, leg and robe surfaces against the translucent body, then stable anchors for shoulders, helmets, gloves, boots, weapons and a cloak. A full suit must remain visible without erasing the wrapped-energy silhouette. Lighting and spell effects must not make the character unreadable to opponents.

**Story proposal:** a small expedition or trading delegation establishes local relationships. Its arrival route and membership need writing; this does not assign the whole Consortium to a faction.

**Prototype gate:** show cloth, leather, mail and plate samples while walking, casting and fighting. If only weapons and shoulders work, the equipment requirement has not been met. The body fantasy grants no automatic phasing or collision immunity.

## Scope of the first implementation spike

Wrapped-energy body with recognizable armor, not a permanent bandage outfit.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Body layers | Preserve emissive/transparent body cues beneath opaque earned chest and leg items; verify depth sorting rather than assuming a texture swap works. |
| Head and hands | Create stable helmet, glove and weapon anchors; wrappings must not replace the equipped item. |
| Robes and cloak | Test long garments against energy effects in motion, including overlapping spell particles and the rear attachment. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Casting, dual-wield grips where class-legal, ranged release, kneeling and death must retain a coherent wrapped body; transparency cannot conceal hostile actions.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A small delegation arrives with damaged containment equipment and seeks safe local assistance.
2. The player helps stabilize its camp and negotiates ordinary trade with representatives of both factions.
3. The player chooses one major faction and travels to its services; the wider people remain politically independent.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Wrapping patterns, energy hue and visible face treatment are candidate options. Item colors and target readability take precedence over unrestricted brightness.

Cultural appraisal and trade-record interactions are narrative opportunities; no free teleport, phasing or gold-yield racial is selected.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Render a plate chest over an energetic torso under bright and dark lighting without item/body depth artifacts.
2. Play death, resurrection and mount transitions without leaving unattached wrappings or losing weapons.
3. Compare enemy readability with a baseline caster during dense spell effects.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).
