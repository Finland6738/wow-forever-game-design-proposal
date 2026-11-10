# Races

[← Main proposal](../../README.md) · [Classes](classes.md) · [Identity review questions](class-roles-and-specializations.md#questions-for-the-next-design-review)

Start with **ten peoples already represented in Vanilla, The Burning Crusade or Wrath of the Lich King**. Their existing NPC appearance is the visual reference, rather than an invented replacement name. Six original concepts remain below as secondary alternatives. None is an announced playable addition.

![Established race candidates and original alternatives pass setting, equipment, animation and balance review alongside class and regional concepts.](../../assets/diagrams/identity-development.svg)

## Selection policy and historical scope

A candidate must add a recognizable silhouette, culture and social identity. Different skin colors or minor variants of an existing playable people are insufficient for this shortlist. This is a preference for this project, not an assessment of other players' tastes.

The reference window is the **original versions of Vanilla, TBC and Wrath**. It does not require importing an expansion's campaign, level cap or later model redesign. TBC/Wrath candidates need an explicit arrival story in a level-60 world; reference-era eligibility does not establish that their assets are available in the current Forever client.

**Classic Worgen are an explicit exception to the preference for never-playable peoples.** The subject is the older Silverpine/Arugal-associated appearance, not the later Cataclysm playable model or its starting campaign. Arugal is the associated mage, not the name of a separate race.

The references below establish historical appearances. Equipment solutions, fitting workload, faction stories and prototype priorities are **our design analysis**. No client files or rigs have been inspected; none of these candidates is verified as fully compatible with player armor.

## Ten established candidates at a glance

The work bands compare expected complexity, not measured time or production estimates. Even a biped may need new UV layouts, attachments and animations. Every candidate requires equipment testing.

| Candidate | Historical visual reference | Distinct identity | Expected fitting work | Recommendation |
| --- | --- | --- | --- | --- |
| [Ethereals](#1-ethereals) — Eterei | TBC; Consortium and Mana-Tombs | Wrapped energy body | Substantial: opacity, body layers, anchors and robes | High creative priority; first equipment proof |
| [Ogres](#2-ogres) | Vanilla; Stonemaul and other clans | Large, heavy-built humanoid | Substantial: scale, belly, shoulders and helmets | Strong candidate; begin with one head |
| [Naga](#3-naga) | Vanilla coasts and Blackfathom Deeps | Serpentine body | Exceptional: tail, leg/foot presentation, mounts and arms | Desirable research candidate; separate feasibility track |
| [Classic Worgen](#4-classic-worgen) | Vanilla Silverpine and Shadowfang Keep | Older feral werewolf silhouette | Substantial: muzzle, posture, claws and animations | Prototype the requested appearance explicitly |
| [Quilboar / Razormane](#5-quilboar-and-the-razormane) | Vanilla Durotar and the Barrens | Bristles, tusks and thornland culture | Substantial: mane, muzzle, torso and back items | Strong candidate with narrative review |
| [Kobolds](#6-kobolds) — Coboldi | Vanilla Elwynn mines | Small underground people | Substantial: stature, posture, muzzle and headgear | Candidate if armor remains readable at scale |
| [Gnolls](#7-gnolls) | Vanilla; Riverpaw and other packs | Hyena-like frontier silhouette | Substantial: muzzle, mane, posture and grips | Strong first-wave candidate |
| [Furbolgs](#8-furbolgs) | Vanilla forests and Timbermaw | Broad bear-like body | Substantial: fur, paws, robes and shoulders | Good cultural candidate; prove armor coverage early |
| [Arakkoa](#9-arakkoa) | TBC; original hunched, flightless appearance | Avian silhouette and ritual identity | Very substantial: beak, talons, feathers and cloak | Distinctive research candidate; no flight assumption |
| [Tuskarr](#10-tuskarr) | Wrath; Kalu'ak settlements | Walrus-like coastal community | Substantial: tusks, broad torso, neck and feet | Strong Wrath-era alternative; arrival story needed |

This is a comparison, not a commitment to ship ten races. Test **Ethereal, Ogre and Gnoll equipment mockups** first: the first tests a requested unusual body, the others test broad and bestial bipeds. This recommendation is a feasibility sample, not a selected release order. Keep Naga locomotion and armor research separate rather than treating it as a cheap follow-up.

## Candidate dossiers

### 1. Ethereals

**Reference:** TBC ethereals, including Consortium figures and the Mana-Tombs appearance. See the [historical Ethereal reference](https://warcraft.wiki.gg/wiki/Ethereal).

**Fantasy:** an energy-bound traveler whose wrappings, equipment and controlled luminosity remain recognizable from the early model. The goal is not to turn every item into an unrelated bandage costume.

**Equipment proposal:** retain standard slots. Test chest, leg and robe surfaces against the translucent body, then stable anchors for shoulders, helmets, gloves, boots, weapons and a cloak. A full suit must remain visible without erasing the wrapped-energy silhouette. Lighting and spell effects must not make the character unreadable to opponents.

**Story proposal:** a small expedition or trading delegation establishes local relationships. Its arrival route and membership need writing; this does not assign the whole Consortium to a faction.

**Prototype gate:** show cloth, leather, mail and plate samples while walking, casting and fighting. If only weapons and shoulders work, the equipment requirement has not been met. The body fantasy grants no automatic phasing or collision immunity.

### 2. Ogres

**Reference:** Vanilla ogres, including Stonemaul presence around Brackenwall. See [Classic Dustwallow Marsh](https://warcraft.wiki.gg/wiki/Dustwallow_Marsh_%28Classic%29).

**Fantasy:** a large, powerful body with a social identity beyond a hostile camp. Start with a **single-headed** prototype; two heads add helmet, animation and customization questions and are not assumed to be free variants.

**Equipment proposal:** fit the torso and belly, prevent belts and weapons sinking into the body, and check shoulders, robes, shields, helmets and boots. Keep the recognizable build while testing a practical playable scale. An NPC's fixed costume does not prove arbitrary item support.

**Story proposal:** a particular clan or delegation needs agency and obligations. A Stonemaul connection can inform local relationships, but the playable origin must also support an individual's Alliance choice after the introduction.

**Prototype gate:** doors, lifts, ceilings, tank camera and crowded melee. Large appearance must not grant extra reach or an unfair attack footprint. Any scale adjustment needs review before it destroys the intended fantasy.

### 3. Naga

**Reference:** Vanilla coasts and Blackfathom Deeps; see the [Blackfathom reference](https://warcraft.wiki.gg/wiki/Blackfathom).

**Fantasy:** a visibly serpentine character. Replacing the tail with ordinary legs removes the main reason for selecting this candidate.

**Equipment proposal:** retain leg and foot item statistics, enchantments, set identity and loot eligibility. A proposed adaptation maps leg armor to tail plating and foot armor to a recognizable lower-tail treatment. This is **pending the equipment-presentation decision**, not permission to hide boots silently. Helmets, fins, cloaks and different arm configurations need separate tests. Extra visible arms do not add weapon slots or attacks.

**Story proposal:** introduce a specific independent group and its reason to cooperate; do not assume all Naga renounce existing allegiances.

**Prototype gate:** slopes, stairs, jumps, swimming, transport seats, mount presentation, camera and combat positioning. This is the highest-risk anatomy in the shortlist and may be deferred even if it remains desirable. Aquatic origins do not grant unreviewed encounter advantages.

### 4. Classic Worgen

**Reference:** the original Silverpine/Shadowfang appearance, exemplified by [Sons of Arugal](https://warcraft.wiki.gg/wiki/Son_of_Arugal). Distinguish it from the [later playable Worgen race](https://worldofwarcraft.blizzard.com/en-gb/game/races/worgen).

**Fantasy:** the older feral werewolf profile, with its original proportions and mood. A playable conversion may require a rebuilt rig and missing animations while preserving that appearance; the unmodified NPC mesh is not promised to support all player actions.

**Equipment proposal:** recognizable helmets around the muzzle and ears, chest/robe fitting on the hunched torso, weapon grips with claws, shoulders and foot treatments. A permanent bare-claw outfit does not fulfill the gear-visibility goal.

**Story proposal:** explain retained intelligence, communication and social acceptance through a local story. Neither a mandatory human form nor automatic real-world day/night transformation is selected.

**Prototype gate:** casting, ranged weapons, shields, sitting, mounts, emotes and customization. Racial appearance is separate from class transformations; Worgen membership must not be the only way to access a shapeshifting specialization.

### 5. Quilboar and the Razormane

**Reference:** Quilboar are the people; **Razormane is a tribe**, not a separate species. The [Razormane reference](https://warcraft.wiki.gg/wiki/Razormane) places them in Durotar and the Barrens.

**Fantasy:** bristled, tusked thornland inhabitants with a serious cultural identity. Architecture, spirituality and materials should support more than a joke or recolor.

**Equipment proposal:** preserve the mane and tusks while fitting helmets, shoulder plates, back items, robes and belts. Decide which bristles deform or need clearance. Different earned items should remain distinguishable on this body.

**Story proposal:** existing conflict with neighbors requires reconciliation, a splinter group or a negotiated relationship. Proximity to a capital is insufficient, and not every hostile clan becomes friendly.

**Prototype gate:** a complete armored caster and melee character using the older visual language. Test whether its anatomy supports the equipment range without losing identity, then develop customization. Introductory diplomacy and racial powers remain open; either-faction choice is selected.

### 6. Kobolds

**Reference:** Vanilla mine-dwellers such as [Kobold Tunnelers in Elwynn](https://warcraft.wiki.gg/wiki/Kobold_Tunneler). Use the earlier appearance rather than assuming a later redesign.

**Fantasy:** a small underground people with craft, superstition, domestic life and territorial concerns. Mining and candles inform the culture without becoming its entire personality or a compulsory head item.

**Equipment proposal:** keep helmets and weapons readable at small scale. A candle can be optional customization, compatible with adapted headgear. Fit muzzle, curved back, hands, robes and boots without making all items look alike.

**Story proposal:** a community negotiates trade, protection or settlement rights. Give characters motives beyond compulsory mining; an existing profession must not become an exclusive racial function.

**Prototype gate:** camera height, target selection, large weapons, casting, mount seating and ground indicators. Small appearance must not confer special targeting/collision advantages, but enlarging the model into an ordinary humanoid would lose its appeal.

### 7. Gnolls

**Reference:** Vanilla packs including the [Riverpaw in Elwynn](https://warcraft.wiki.gg/wiki/Gnoll), with their early bestial design as the baseline.

**Fantasy:** a hyena-like frontier people with pack relationships, scavenged equipment and individual agency. A playable group needs more depth than a generic enemy faction.

**Equipment proposal:** helmets around muzzle and mane, shoulders on a hunched back, torso armor, weapon/shield grips, robes, boots and cloak attachment. Existing NPC weapons provide a visual starting point, not proof of the whole item system.

**Story proposal:** a specific group's cooperation is earned through events. Existing hostility toward settlements needs consequences and cannot be resolved solely by changing a reaction flag.

**Prototype gate:** compare the same equipment set on a Gnoll and a baseline race, then test melee, ranged and casting actions. This is a useful bestial-biped comparison with the Ogre study, not a certified cheaper conversion. No mandatory pack damage aura is selected.

### 8. Furbolgs

**Reference:** Vanilla forest peoples and [Timbermaw communities](https://warcraft.wiki.gg/wiki/Timbermaw_furbolg).

**Fantasy:** a broad forest-dwelling people with spiritual and communal life. Preserve bear-like proportions and the older forest aesthetic.

**Equipment proposal:** define fur compression under armor, shoulder placement, weapon grips with paws, and fitting for robes, belts, boots and helmets. Fur volume is a problem to solve, not a reason to hide the torso indefinitely.

**Story proposal:** protecting or restoring a community could support a starting experience. Existing Timbermaw neutrality can inform the origin; the individual chooses either major faction after the introduction.

**Prototype gate:** armored readability in a raid, kneeling, sitting, casting, mount fit and grips. Forest spirituality must not force every class toward one nature kit, and racial utility cannot become an exclusive raid requirement.

### 9. Arakkoa

**Reference:** the original TBC **hunched, flightless** appearance. Blizzard distinguishes these familiar Arakkoa from the later winged treatment in its [Spires of Arak preview](https://worldofwarcraft.blizzard.com/en-gb/news/15108050/warlords-of-draenor-zone-preview-spires-of-arak).

**Fantasy:** avian body language, feathered ritual clothing and a recognizable beaked silhouette. The first concept includes neither unrestricted flight nor a required later upright model.

**Equipment proposal:** test helmets around beak and crest, shoulder/feather overlap, hand grips, taloned feet, robes and a cloak attachment on the hunched back. Permanent species clothing with hidden items would not fulfill the equipment goal.

**Story proposal:** a traveler or small group needs a credible arrival route. The early visual reference does not automatically adopt later stories or political allegiances.

**Prototype gate:** cloth and heavy-armor presentations, weapons and traversal. If fitting arbitrary armor erases the feathered identity, reconsider the approach. Existing NPC appeal can justify research without proving a low-cost playable conversion.

### 10. Tuskarr

**Reference:** Wrath-era Kalu'ak and coastal settlements. Blizzard's [Wrath zone guide](https://news.blizzard.com/en-gb/article/23816544/wrath-classic-zone-guide-borean-tundra-and-howling-fjord) describes their Northrend presence and contact with both factions.

**Fantasy:** a walrus-like seafaring people with communal craft and harsh-coast stories. Retain the older proportions and materials.

**Equipment proposal:** helmets around tusks, chest and robe fitting over the broad torso, shoulders, gloves, boots, shields and cloak movement. Fishing tools and fixed garments do not prove arbitrary weapons or armor work.

**Story proposal:** a visiting crew, rescued settlement or trade mission could introduce them. Wrath-era eligibility does not require importing the full Northrend campaign or its level cap. The origin must support either major-faction choice.

**Prototype gate:** playable scale, indoor movement, mounts, varied equipment and full cast/melee actions. Keep the body recognizable under gear. Coastal identity cannot make fishing or water access an exclusive source of necessary progression.

## Equipment contract for every candidate

**Selected:** players see their earned equipment through recognizable anatomy-specific adaptations. Naga leg/foot armor can become tail treatments; beaks, tusks, claws and energetic bodies need their own fitting rules. Preserve the item's identity, statistics and slots. Exact mappings still require prototypes; invisible equipment is not the default solution.

| Layer | Required behavior | Evidence before approval |
| --- | --- | --- |
| Item ownership and power | Same slots, eligibility, enchants and budget; no anatomy bonus slots | Equip/unequip and set-effect checks across eligible classes |
| Visible armor | Recognizable head, shoulders, chest/robe, wrists, hands, waist, legs, feet and back where those slots normally have a visible presentation | Cloth/leather/mail/plate samples and an explicit exception list |
| Normally invisible slots | Rings, neck and trinkets use the ordinary item system | UI and power parity; no invented visual requirement for every trinket |
| Weapons | Correct grips, sheathing, ranged use and shield poses | One/two-handed, class-legal dual-wield, ranged and caster samples |
| Anatomy adaptations | Preserve item identity; show unresolved cases | Tail, claw, tusk, feather and Ethereal-layering mockups |
| Character creation | Intentional customization and body/presentation choices | Armor tests for every supported body option |
| Player actions | Combat, casting, movement, death, recovery, emotes, sitting and interaction | Animation coverage in a working prototype |
| World interaction | Doors, stairs, lifts, transports, mounts, camera and combat positioning | Small interiors, crowded combat and traversal scene |

Use a test wardrobe: close/open helmets, large shoulders, chest-and-leg armor, long robe, cape, gloves, boots, shield, staff, two-handed and ranged weapons. Repeat for relevant armor types and body presentations. Any hidden or adapted item needs an explicit decision; do not advertise complete compatibility from a dressed NPC screenshot.

No automatic flight, extra weapon attacks, phasing or encounter immunity comes from a model. Racial abilities use the same permanent budget and competitive policies as the existing roster.

## Six original alternatives

These are **secondary invented concepts**, not disguised names for the established peoples above. If a concept merely approximates an Ogre, Naga or Ethereal, develop the established candidate instead. Retain an original only if culture and mechanics earn a separate identity.

| Original concept | Independent opportunity | Decision needed |
| --- | --- | --- |
| Gravemarch | Broad-built stone-country clans | Does it add enough beyond other broad bodies? |
| Brineveil | A separate serpentine coastal society | Merge or archive if it duplicates Naga |
| Stonewake | Mountain people shaped by regional mythology | Distinguish from scaled-up humanoids and solve playable size |
| Thornmaw | A distinct bestial frontier culture | Merge or archive if it merely substitutes for Gnolls |
| Briarhide | Thornland communities with their own traditions | Distinguish from the existing Quilboar direction |
| Veilbound | Shrouded magical people with a separate origin | Merge or archive if it merely substitutes for Ethereals |

## Neutral origins and faction choice

**Selected for every new playable people:** start in a race-appropriate introductory experience, then choose **Alliance or Horde**. Friends should not have to abandon their preferred new race to join the same faction. Neutral origin does not mean the character remains mechanically neutral after that choice.

Use a specific community or delegation with reasons to negotiate with both sides. Existing NPC tribes can remain hostile, friendly or independent. An individual player's choice does not rewrite the allegiance of the whole species or automatically resolve old conflicts.

The introduction must explain communication, travel to the chosen faction, trainers, baseline services and how joining affects local relationships. Completing that introduction cannot require a prestige rank or old raid. Whether faction choice can later be changed is a separate policy, not selected here.

Race appearance alone will no longer identify major-faction membership. Nameplates, targeting, guards, party rules and PvP indicators must communicate it reliably. Warfare city selection then follows the character's **chosen major faction**, not ancestry; this does not grant access to opposing-faction city standards.

## Decisions still open

Arrival stories, final shortlist, race/class combinations, precise armor mappings, customization and later faction-change rules remain open. Neutral introduction followed by either-faction choice, and recognizable anatomy-specific armor adaptation, are selected boundaries. No new race is assigned exclusively to one faction in this catalog.

No race requires prestige rank, prior raid completion or territorial victory to become an ordinary player option. A future unlock policy must preserve reasonable leveling entry and keep existing races complete choices.
