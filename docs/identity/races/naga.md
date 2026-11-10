# Naga — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** Vanilla coasts and Blackfathom Deeps; see the [Blackfathom reference](https://warcraft.wiki.gg/wiki/Blackfathom).

**Fantasy:** a visibly serpentine character. Replacing the tail with ordinary legs removes the main reason for selecting this candidate.

**Equipment proposal:** retain leg and foot item statistics, enchantments, set identity and loot eligibility. A proposed adaptation maps leg armor to tail plating and foot armor to a recognizable lower-tail treatment. Recognizable anatomical adaptation is selected; the exact tail mapping still needs a wardrobe prototype. Footwear is not approved to disappear silently. Helmets, fins, cloaks and different arm configurations need separate tests. Extra visible arms do not add weapon slots or attacks.

**Story proposal:** introduce a specific independent group and its reason to cooperate; do not assume all Naga renounce existing allegiances.

**Prototype gate:** slopes, stairs, jumps, swimming, transport seats, mount presentation, camera and combat positioning. This is the highest-risk anatomy in the shortlist and may be deferred even if it remains desirable. Aquatic origins do not grant unreviewed encounter advantages.

## Scope of the first implementation spike

A serpentine playable body with genuine tail locomotion and visible lower-body item adaptation.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Leg slot | Map leg-armor identity to a reviewed tail treatment while preserving its ordinary statistics and set participation. |
| Foot slot | Map boots to a separate recognizable lower-tail treatment; no invisible-by-default shortcut. |
| Arms, fins and head | Test different arm arrangements, helmets, fins, shields and sheathing. Additional visible arms do not create extra weapon slots. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Slithering, stairs, slopes, swimming, jumps, death and mounting need explicit authored behaviors. A tail must not change the combat footprint or permit geometry clipping.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A specific coastal group breaks with a local patron over a survival dispute; its exact politics require lore review.
2. The player cooperates with surface representatives to restore a shared route or refuge.
3. After proving individual agency, the player chooses Alliance or Horde rather than assigning the entire people to one side.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Scale patterns, fin shapes, crests and supported body variants need separate fitting coverage. Do not normalize the body into ordinary legs to reduce cost.

Aquatic culture can shape story and traversal presentation. Breathing or swimming utility, if later proposed, needs accessible encounter alternatives and a reviewed racial budget.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Equip visually distinct boots and leg sets and identify both adapted items on the tail.
2. Navigate stairs, a transport seat and a mounted transition without invalid collision or camera behavior.
3. Use one-handed, shield and ranged/caster actions under the normal slot rules.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).

## Selected silhouette and equipment exception policy

Wrist items, cloaks and gloves may be hidden or anatomically varied where needed; document every exception. Footwear is audited per anatomy and has no blanket invisibility approval. Head and weapon presentation are key audit requirements: preserve readable headgear/weapon identity, casting source and the wider class signals in PvP. Gear silhouette alone cannot prove class recognition, so test poses, effects, movement and authoritative nameplate/faction cues too. These requirements revise any earlier all-items-visible assumption; they do not erase slot effects or item ownership.
