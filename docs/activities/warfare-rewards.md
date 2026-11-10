# Warfare Reputation and Cosmetics

[← Faction Warfare](faction-warfare.md) · [Model Comparison](warfare-models.md) · [Rewards](../11-rewards-and-acquisition.md)

## Selected direction, conditional on city service

If the city-service layer is retained, **base reward objects remain permanently owned**, while **city crests and variants require eligible current service**. Changing the served city also loses some Warfare reputation with the departed city. The penalty formula, thresholds and city-layer launch model are still open.

This is different from deleting a mount or making an earned base item vanish. A usable neutral form remains when the character is not eligible for the city treatment.

## Base ownership and live eligibility

| Element | Persists | Requires live city eligibility |
| --- | --- | --- |
| Earned base banner, cloak or mount | Yes | No |
| City crest or insignia treatment | Recorded as appropriate collection/history data | Yes, for visible use |
| Distinct city silhouette or themed variant | Base entitlement remains | City version follows its service/standing requirement |
| Current city service reputation | Character ledger, subject to the selected departure penalty | Determines currently eligible city treatments |
| Combat-team indication | Authoritative UI state | Follows the active combat relation, never an old cosmetic alone |

A permanent banner template may show neutral art before the active city's threshold is met. Once that threshold is reached, the relevant city treatment becomes usable. If the character changes service, the old treatment becomes inactive and the base object remains.

Whether returning to an earlier city immediately restores some variants depends on retained reputation and the final thresholds. That consequence must be visible before confirming a switch.

## Switching service is not toggling combat

The city NPC can manage both operations, but they are distinct. Disabling a city combat flag for ordinary play should not erase city reputation or permanently change allegiance. Reputation loss applies to changing the city served, under the selected penalty policy.

The recommendation is to let eligible current-service cosmetics identify the player's chosen city even outside active combat. Combat nameplates/indicators separately show whether rivalry is enabled. Requiring the combat flag solely to wear an earned city crest would pressure players to enter a combat mode for appearance alone; that presentation detail remains to be confirmed.

## A percentage loss does not guarantee a reset below rewards

Using the illustrative examples, 10,000,000 reputation reduced by 50% leaves 5,000,000. If the first reward threshold is 1,000,000, several rewards may still meet their standing requirement.

The live-service rule already makes the departed city's crest inactive: the character no longer serves that city. There is no mathematical need to force reputation below the first threshold merely to hide an inactive crest.

If the intended behavior also requires every return to restart below the first reward, a separate cap or reset rule is necessary. That would be a much stronger penalty than halving and should be a deliberate design choice. No illustrative million-point threshold or percentage is adopted as final tuning.

## Why use a commitment cost carefully?

A departure penalty can make service feel consequential and discourage repeatedly changing to the most profitable city. Too much loss can instead prevent friends from regrouping, lock players into an underpopulated city or turn cosmetic collecting into repeated mandatory grind.

Before selecting a loss amount, compare it with a cooldown-only alternative and a modest bounded loss. Preserve the base object in every candidate. Explain the projected reputation and inactive variants before confirmation, and prohibit a change from clearing active combat, capture responsibility or cooldowns.

## Art and gameplay boundaries

Shared templates and unique city art are compatible: the base entitlement can be permanent while specific treatments differ by city. A cloak could have an ordinary neutral version and an eligible city's distinct back treatment. Exact silhouettes and mount families remain art proposals.

Changing eligibility cannot change combat statistics, grant a faster mount, remove an equipped weapon or duplicate a tradable object. A display transition should wait for a safe state rather than unexpectedly removing a mount during play.

## Evaluation

Measure switch frequency, loss aversion, time to regain variants, service population, group-formation friction and whether neutral forms still feel like owned rewards. A commitment mechanic should create identity, not make the player feel their previous evenings were erased.
