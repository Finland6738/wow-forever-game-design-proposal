# Archetype and Mechanic Coverage

[← Classes](classes.md) · [Implementation standard](implementation-standard.md) · [Races](races.md)

## Scope and status

This register maps the author's supplied archetype briefs and mechanical studies to the proposed MMO class trees. The latest nine-study attachment covers the first nine rows below; four additional studies were supplied earlier. It records which decisions are preserved, adapted or excluded rather than claiming literal reproduction of another game's characters or rules.

**Specified** means a named dossier/tree now defines the role, resource, loop, actions and evaluation cases. It does not mean those mechanics have been implemented or playtested in the target engine. The [implementation standard](implementation-standard.md) defines the evidence required to advance.

## Nine studies in the latest brief

| ID / supplied mechanical core | Primary dossier / tree | Preserved decision | Adaptation or exclusion | Current evidence |
| --- | --- | --- | --- | --- |
| M01 — Two forms, combo building and spending | [Warden / Moon Predator](classes/warden.md#moon-predator) | Prepare position and a small combo reserve, then spend through the current form | The author selected an **automatic internal combat cycle**. World day/night and manual form choice do not govern it. Exact phase duration and combo cap require tuning | Specified; no engine test |
| M02 — Accumulate small followers and command a release | [Summoner](classes/summoner.md) | Ranged actions gather a reserve; explicit orders commit it to basic attacks, persistent pressure or consumption | Music/rats pairing retired. Swarmcaller uses insects, Soulbinder souls/wisps and Sporekeeper a support colony. Followers are non-selectable with **no HP**; health talents removed | Three selected identities; kits specified, untested |
| M03 — Companion empowers the next action | [Spellblade / Spellguard](classes/spellblade.md#spellguard) | Prime exactly the next eligible offensive or defensive action and choose which one receives the benefit | The companion is a bounded priming mechanism, not a second full pet budget. Tank role; full healer output is not added for free | Specified; exact companion visual/coefficients open |
| M04 — Apply and consume a cold state | [Runemaster / Rime Scholar](classes/runemaster.md#rime-scholar) | Maintain a finite cold damage state, shape threats and choose the consumption window | Damage state and control immunity are separate; bosses need not be slowed to support the loop. Consumption reconciles remaining payload | Specified; untested |
| M05 — Enchanted weapon and limited interventions | [Spellblade / Oath Duelist](classes/spellblade.md#oath-duelist) | Ordinary charge-based weapon combat plus a scarce encounter intervention decision | No wealth/item generation, unlimited resurrection or bypass of encounter failure. Exact aid category and allowance are open | Specified with explicit exclusions |
| M06 — Move versus stationary remote casting | [Bard / Deep Cantor](classes/bard.md#deep-cantor) | Choose a safe anchor, direct a remote focus, then break the channel to move | Owner remains vulnerable; range/line-of-sight and cancellation are explicit. No indefinite invulnerable remote damage | Specified; focus/engine behavior unverified |
| M07 — Build, reposition, repair and rebuild automata | [Artificer / Puppet Warden](classes/artificer.md#puppet-warden) | Placement, repair and physical hammer/kick repositioning form the tank loop | Author-selected stationary dummies have independent HP and only owner repairs. Local threat/taunt; extra autonomous puppet is temporary, additional and cooldown-bound | Selected core; detailed contract and acceptance scenes |
| M08 — Guarded versus risky offensive posture | [Martial Adept / Open Hand](classes/martial-adept.md#open-hand) | Build, find an opening, commit offense and return to safety; deliberate counter decisions | Source double-damage/double-incoming values are not adopted tuning. No infinite parry reset or compulsory healer subsidy | Specified; timing and multipliers open |
| M09 — Blood resource, health substitution and transformation | [Hemomancer](classes/hemomancer.md) | Generate Blood, spend reserves and manage a short transformation/upkeep window | Bounded self-cost and recovery; no infinite drain, involuntary player-health theft or unrestricted flight. Separate healer tree does not add full healing to DPS builds | Three trees specified; untested |

These are adaptations into a persistent group MMO with the selected power and role policies. Visual motifs, protagonist names, exact numerical multipliers and mechanics that break the economy or encounter contract are not treated as requirements to copy.

## Four additional studies from the earlier brief

| ID / mechanical core | Primary dossier / tree | Preserved decision | Adaptation and required test |
| --- | --- | --- | --- |
| M10 — Parries and partnered follow-ups | [Warden / Duelist](classes/warden.md#duelist) | Prepare a response, counter and choose the follow-up moment | No mandatory named partner class. A teammate may trigger the same bounded seal payload; the tree remains viable independently |
| M11 — Ammunition and deliberate precision release | [Gunslinger / Sharpshooter](classes/gunslinger.md#sharpshooter) | Spend ammunition, aim, release and recover through reload/reposition | Latency-tolerant timing; an imperfect release retains useful output. Reload cancellation cannot duplicate ammunition |
| M12 — School choice then an enhanced spell | [Runemaster / Rune Scholar](classes/runemaster.md#rune-scholar) | Choose a school and consume a prepared class-sigil enhancement | Nature/Arcane/Holy palette is proposed for review. No full three-role kit, redundant input requirement or connection to the completion-based Rune milestone record |
| M13 — Mounted/foot companion play with transferred damage | [Cavalier / Beast Rider](classes/cavalier.md#beast-rider) | Decide when to ride, separate and regroup while managing companion risk | Capped damage debt, viable indoor fallback and no free full recovery through mounting. Beastmaster retains pack assignments instead of duplicating this tree |

## Tabletop-style archetype coverage

The supplied archetype names are readable design starting points. The dossiers define their own actions and budgets rather than relying on a reader knowing a tabletop rulebook.

| Supplied archetype / fantasy | Class dossier | Distinct implementation question |
| --- | --- | --- |
| Musical performer | [Bard](classes/bard.md) | Prepared phrases, Tempo and active performance timing across support/healer/anchored DPS |
| Bombs, draughts and mutagens | [Alchemist](classes/alchemist.md) | Small prepared loadout and renewable class reagent, without profession shopping as rotation |
| Summoning as the main loop | [Summoner](classes/summoner.md) | Gather, commit, release and reclaim; three selected kinds of small beings |
| Judgment and investigation | [Inquisitor](classes/inquisitor.md) | Visible observations and Conviction, with damage/support/healer responsibilities |
| Omen and personal burden | [Oracle](classes/oracle.md) | Prediction, trigger and expiry recovery without punishing teammates randomly |
| Linked curses and familiar | [Witch](classes/witch.md) | Sustain, relay and consume hexes without control loops or a free extra full caster |
| Tactical deduction and tools | [Investigator](classes/investigator.md) | Valid observations and limited responses, not secret enemy data |
| Weapon-and-spell / spellblade archetype | [Spellblade](classes/spellblade.md) | Stored charges, next-action priming and finite interventions with explicit ownership |
| Firearm precision and reload | [Gunslinger](classes/gunslinger.md) | Ammo and commitment with network-tolerant timing |
| Mounted companion fighter | [Cavalier](classes/cavalier.md) | Mounted/foot parity, controlled approach and companion debt |
| Martial stance/counter fighter | [Martial Adept](classes/martial-adept.md) | Guard, offense and support timing without importing a later class kit |

The [remaining families](classes.md#class-and-role-matrix)—Necromancer, Artificer, Warden, Dark Ranger, Runemaster, Beastmaster and Hemomancer—also have individual three-tree dossiers. Shared themes do not prove distinct gameplay: overlap remains a review/rejection criterion.

## Handoff gaps that remain explicit

All eighteen families now have a named dossier and three tree specifications. The next evidence is still required: full talent-node allocation/ranks/depths, mixed-tree analysis, actual engine prototypes, numerical tuning, ability/animation costs and activity-profile validation. Races additionally require asset/rig/wardrobe and starting-experience proof.

This register makes coverage reviewable. It cannot turn an untested concept into a production-ready game system merely by marking a table row complete.
