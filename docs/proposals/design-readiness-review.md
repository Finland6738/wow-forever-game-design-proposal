# Design Readiness Review

[← Proposal](../../README.md) · [Evaluation roadmap](../05-roadmap-and-evaluation.md) · [Implementation standard](../identity/implementation-standard.md)

Review date: **10 November 2026**. This review records remaining work and three newly selected working constraints. It does not adopt every proposed class kit or assert engine validation.

## Assessment

Topic coverage is broad: eighteen class dossiers, 54 tree outlines, ten established race dossiers and the main endgame systems have reading paths. Implementation detail remains uneven. Most tree outlines define three baseline actions and talent directions rather than a complete playable toolkit and allocated talent grid.

Some actions still use categories such as a protective response or a countermeasure without selecting a precise effect, target rule, cost and cancellation behavior. These are useful design spaces, but they need concrete ability contracts before implementation. Passing documentation tests establishes navigation and publishing correctness, not combat balance.

## Working constraints selected during this review

| Area | Selected reference | Still open |
| --- | --- | --- |
| Talent allocation | 51 points at level 60; a 31-point capstone; hybrid builds explicitly reviewed | Node counts/ranks, tier gates, prerequisites, individual effects and actual Forever integration |
| Ordinary five-player support | Generally a little slower than three DPS, with more control and safety; both lineups complete the same encounters | Acceptable time difference, useful boss tools, raid stacking and competitive treatment |
| Last Artificer dummy destroyed | Brief emergency defense for the owner and reconstruction at a real cost | Duration, cooldown, input, mitigation, rebuild cost and threat-transition behavior |

The talent numbers are this proposal's working profile, not a verified statement about Forever's current rules. A capstone reached with 31 invested points leaves 20 of 51 for other allocations; two such capstones would require 62. This limits capstone combinations but does not validate every hybrid interaction.

## Prioritized gaps

| Priority | Gap | Why it matters | Next review artifact |
| --- | --- | --- | --- |
| P0 | Full talent allocation and shared base kits | Three trees can combine through talents; three outline actions do not define leveling, control, defense and recovery | One complete class kit, node/rank/depth sheet and hybrid examples |
| P0 | Class/role differentiation | Several families repeat reserve → commitment → release, or protection/control support patterns | Pairwise decision comparison and an explicit unique/non-unique-tool matrix |
| P0 | Support in boss and timed content | Safety can compensate for lost damage in ordinary play; that does not settle timers or competitive value | Same encounter with 3 DPS versus 2 DPS + support, including an immune boss |
| P0 | Artificer collapse and moving encounters | Independent repair-only device HP changes healer load, threat and recovery | A pull with movement, simultaneous device loss, emergency defense and paid reconstruction |
| P0 | Competitive Rune/repertoire policy | Finite earned stats and historical ability ownership can still affect equal competitive access | Explicit Challenge and Arena eligibility/normalization profiles |
| P0 | Mixed-city Warfare capture and aid | Combat permission is described more precisely than mixed-standard claims and support consent | Worked capture with neutral allies, rival allied cities and the opposing faction |
| P1 | Raid entry, loot and historical reward cadence | Equipment access and desirable old abilities create different preparation pressures | New/returning-player journey with actual acquisition steps and a scoped-power example |
| P1 | Race wardrobe and player rig evidence | Existing NPC appearance does not demonstrate arbitrary armor and animation support | Actual Ethereal/Ogre/Gnoll wardrobe and movement spikes before roster approval |
| P1 | Gold/material throughput and event incentives | Finite equipment does not prevent economic dominance, farming loops or profitable engineered failure | Reward/source/sink comparison, repeat rules and successful-defense comparison |
| P1 | Player comprehension and maintenance | Many separate ranks, power channels, flags and owned entities increase learning and support costs | One evening-of-play walkthrough and clear loadout/flag mockups |

P0 means a decision needed before the affected implementation slice can be assessed reliably. It does not mean all unrelated documentation or creative work must stop.

## Differentiation test

| Candidate set | Intended distinguishing decision to prove | Redesign signal |
| --- | --- | --- |
| Summoner / Beastmaster / Necromancer / Witch | Finite untargetable reserve; persistent vulnerable pack assignments; expendable formation/decay; linked hex delivery and familiar relay | The player makes the same commands at the same times despite different visuals |
| Bard / Oracle / Witch support trees | Performance commitment; prediction/trigger timing; linked-effect routing/consumption | Each simply builds a bar and spends it on the same generic guard |
| Artificer / other tank candidates | Stationary independent devices, paid repairs and deliberate physical repositioning | Devices either eliminate normal tank responsibilities or add command burden without decisions |
| Spellblade / Runemaster | Weapon-charge/next-action choices versus prepared arrangement/school/state consumption | Different resource labels conceal identical build-and-spend rotations |

These are intended distinctions requiring proof, not conclusions that all eighteen candidates warrant production. Keep the full candidate library; select a small implementation sample and revise or consolidate weak overlaps through author review.

## Recommended next sequence

1. Complete the Artificer/Puppet Warden base kit and talent allocation using the 51/31 reference. Walk through movement, repair and complete formation failure.
2. Complete Sporekeeper's exact boss-usable utility and compare both selected ordinary group compositions. Treat the selected speed/safety trade-off as a hypothesis to measure.
3. Complete one Summoner damage tree and its reserve/commitment accounting, then compare its decisions with one persistent-pet family.
4. Run the hybrid examples 31/20/0, 30/21/0, 21/21/9 and 17/17/17. Investigate control chains, resource engines, mitigation and output, not only capstone access.
5. Specify competitive profiles and a fully worked Warfare claim before expanding those pilots.
6. Commission asset/wardrobe evidence for a small race sample while the remaining dossiers stay available for comparison.

## Questions for subsequent review rounds

- Which specific effects constitute Sporekeeper's protection and countermeasure kit, and what makes its boss play different from Bard or Oracle support?
- What rebuild resource/cost permits legitimate Artificer recovery without free health cycling or an unavoidable zero-resource dead end?
- How large a time/safety trade-off is acceptable in ordinary dungeons, and how should it be evaluated separately in timed Challenges?
- What is the exact competitive policy for Runes and learned repertoire abilities?
- Who declares the city claim in a mixed assault, and which assistance actions require city combat consent?
- What acquisition path counts as adequate permanent raid preparation for a new or returning character?
- Which race body passes real equipment/animation tests first, and which visual exceptions are acceptable?

These questions are design choices and evidence requests. Unanswered items remain open; they are not silently resolved by a dossier's proposed example.
