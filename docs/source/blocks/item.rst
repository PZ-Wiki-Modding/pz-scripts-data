.. _item:

item
====

Defines an item to register.

This block can be soft overridden in scripts.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`

**Possible Child Blocks:**

- :ref:`component`
- :ref:`component-contextmenuconfig`
- :ref:`component-durability`
- :ref:`component-fluidcontainer`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _item-acceptitemfunction:

AcceptItemFunction
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-acceptmediatype:

AcceptMediaType
^^^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``-1``

.. _item-activateditem:

ActivatedItem
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-aimingmod:

AimingMod
^^^^^^^^^

   Type: ``Any``

No description

.. _item-aimingperkcritmodifier:

AimingPerkCritModifier
^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

See :ref:`item-criticalchance` for more details.

.. _item-aimingperkhitchancemodifier:

AimingPerkHitChanceModifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

See :ref:`item-hitchance` for more details.

.. _item-aimingperkminanglemodifier:

AimingPerkMinAngleModifier
^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-aimingperkrangemodifier:

AimingPerkRangeModifier
^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-aimingtime:

Aimingtime
^^^^^^^^^^

   Type: ``{'main': 'integer'}``

`Aimingtime <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-aimingtime>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `AimingTimeModifier <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-aimingtimemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_. The attachments directly add or subtract their `AimingTimeModifier <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-aimingtimemodifier>`_ to the aiming delay.

It controls the aim-settling delay, the aiming delay counter that must tick down to 0 before the weapon is "settled". Lower values means faster target reacquisition after each shots. The primary "how snappy does this gun feel" lever for semi-automatic guns. It tick down the aiming via the following formula:

.. code-block:: java

   rate = 0.625 x gameSpeed x (1 + 0.05 x AimingLevel + (Marksman ? 0.1 : 0))

The `marksman <https://pzwiki.net/wiki/Marksman>`_ trait being no longer accessible in the recent versions of the game, the condition involving it will never be reached.

..

   Note:
   This formula might not be fully accurate as `time deltas <https://github.com/demiurgeQuantified/PZModdingGuides/blob/main/guides/GameTime.md>`_ don't appear in the formula.


While ``aimingDelay > 0``\ , both `hit chance <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-hitchance>`_ and `critical chance <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-criticalchance>`_ take an aim-delay penalty proportional to the remaining delay. The countdown only starts after ``recoilDelay`` has recovered, so high `RecoilDelay <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-recoildelay>`_ directly delays when ``AimingTime`` begins ticking.

On each shots or equip, the aiming delay will be increased or reduced, being impacted by aiming while in a `vehicle <https://pzwiki.net/wiki/Vehicle>`_\ , being reduced by the trait `Dextrous <https://pzwiki.net/wiki/Dextrous>`_ or increased by `All Thumbs <https://pzwiki.net/wiki/All_Thumbs>`_. The following formula is used:

.. code-block:: java

   aimingDelay = AimingTime
           * (Dextrous ? 0.8 : AllThumbs ? 1.2 : 1.0)
           * (in vehicle ? 1.5 : 1.0)

.. _item-aimingtimemodifier:

AimingTimeModifier
^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

See :ref:`item-aimingtime` for more details.

.. _item-aimreleasesound:

AimReleaseSound
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-alarmsound:

AlarmSound
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-alcoholic:

Alcoholic
^^^^^^^^^

   Type: ``Any``

No description

.. _item-alcoholpower:

AlcoholPower
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-alwaysknockdown:

AlwaysKnockdown
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-alwayswelcomegift:

AlwaysWelcomeGift
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-ammobox:

AmmoBox
^^^^^^^

   Type: ``Any``

No description

.. _item-ammotype:

AmmoType
^^^^^^^^

   Type: ``Any``

No description

.. _item-anglefalloff:

AngleFalloff
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-animalfeedtype:

AnimalFeedType
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-attachmentreplacement:

AttachmentReplacement
^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-attachmentsprovided:

AttachmentsProvided
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-attachmenttype:

AttachmentType
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-badcold:

BadCold
^^^^^^^

   Type: ``Any``

No description

.. _item-badinmicrowave:

BadInMicrowave
^^^^^^^^^^^^^^

   Type: ``Any``

Used to set whether this item can cause a fire when put in a microwave, if set to true it will explode.

.. _item-bandagepower:

BandagePower
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-basespeed:

BaseSpeed
^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-basevolumerange:

BaseVolumeRange
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-bitedefense:

BiteDefense
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-bloodlocation:

BloodLocation
^^^^^^^^^^^^^

   Type: ``{'main': 'array', 'array': {'type': 'string', 'separator': ';'}}``

No description

   Allowed values:

   - ``Apron``
   - ``ShirtNoSleeves``
   - ``JumperNoSleeves``
   - ``Shirt``
   - ``ShirtLongSleeves``
   - ``Jumper``
   - ``Jacket``
   - ``LongJacket``
   - ``ShortsShort``
   - ``Trousers``
   - ``Shoes``
   - ``FullHelmet``
   - ``Bag``
   - ``Hands``
   - ``Head``
   - ``Neck``
   - ``Groin``
   - ``UpperBody``
   - ``LowerBody``
   - ``LowerLegs``
   - ``UpperLegs``
   - ``LowerArms``
   - ``UpperArms``
   - ``Hand_L``
   - ``Hand_R``
   - ``ForeArm_L``
   - ``ForeArm_R``
   - ``UpperArm_L``
   - ``UpperArm_R``
   - ``UpperLeg_L``
   - ``UpperLeg_R``
   - ``LowerLeg_L``
   - ``LowerLeg_R``
   - ``Foot_L``
   - ``Foot_R``

.. _item-bodylocation:

BodyLocation
^^^^^^^^^^^^

   Type: ``Any``

Used to define which location on the human character this clothing item can be worn.

.. _item-book_subject:

book_subject
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-boredomchange:

BoredomChange
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-brakeforce:

brakeForce
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-breaksound:

BreakSound
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-bringtobearsound:

BringToBearSound
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-bulletdefense:

BulletDefense
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-bullethitarmoursound:

BulletHitArmourSound
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-calories:

Calories
^^^^^^^^

   Type: ``Any``

No description

.. _item-canattach:

CanAttach
^^^^^^^^^

   Type: ``Any``

No description

.. _item-canbandage:

CanBandage
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-canbarricade:

CanBarricade
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-canbeequipped:

CanBeEquipped
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-canbeplaced:

CanBePlaced
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-canberemote:

CanBeRemote
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-canbereused:

CanBeReused
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-canbewrite:

CanBeWrite
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-candetach:

CanDetach
^^^^^^^^^

   Type: ``Any``

No description

.. _item-canhaveholes:

CanHaveHoles
^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

Used to define whenever this item can get holes in it.

   Default: ``True``

.. _item-cannedfood:

CannedFood
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-canstack:

CanStack
^^^^^^^^

   Type: ``Any``

No description

.. _item-canstorewater:

CanStoreWater
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-cantattackwithlowestendurance:

CantAttackWithLowestEndurance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-cantbeconsolided:

cantBeConsolided
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-cantbefrozen:

CantBeFrozen
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-canteat:

CantEat
^^^^^^^

   Type: ``Any``

No description

.. _item-capacity:

Capacity
^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``-1``

.. _item-carbohydrates:

Carbohydrates
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-categories:

Categories
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-chancetofall:

ChanceToFall
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-chancetospawndamaged:

ChanceToSpawnDamaged
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-clicksound:

ClickSound
^^^^^^^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``Stormy9mmClick``

.. _item-clipsize:

ClipSize
^^^^^^^^

   Type: ``Any``

No description

.. _item-closekillmove:

CloseKillMove
^^^^^^^^^^^^^

   Type: ``Any``

Used to whenever this weapon can be used to do a close kill move, like knives to assassinate in the back.

.. _item-closesound:

CloseSound
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-clothingextrasubmenu:

ClothingExtraSubmenu
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

See :ref:`item-clothingitem` for more details.

.. _item-clothingitem:

ClothingItem
^^^^^^^^^^^^

   Type: ``Any``

``ClothingItem`` references the clothing defined inside the `clothing.xml <https://pzwiki.net/wiki/Clothing.xml>`_ file. ``ClothingExtraSubmenu`` will define the name of the context menu option to equip the clothing item.

``ClothingItemExtra`` and ``ClothingItemExtraOption`` are used to define additional clothing equip options, they reference another item script block.

.. _item-clothingitemextra:

ClothingItemExtra
^^^^^^^^^^^^^^^^^

   Type: ``Any``

See :ref:`item-clothingitem` for more details.

.. _item-clothingitemextraoption:

ClothingItemExtraOption
^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

See :ref:`item-clothingitem` for more details.

.. _item-colorblue:

ColorBlue
^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``255``

.. _item-colorgreen:

ColorGreen
^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``255``

.. _item-colorred:

ColorRed
^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``255``

.. _item-combatspeedmodifier:

CombatSpeedModifier
^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-conditionaffectscapacity:

ConditionAffectsCapacity
^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

Set whenever condition of the item can impact the capacity value of the container.

.. _item-conditionlowerchanceonein:

ConditionLowerChanceOneIn
^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

The chance impact to reduce the durability of the item, the value is used to calculate the chance by doing $chance = 1/ConditionLowerChanceOneIn$, which means increasing this parameter value will reduce the chance to damage the item.

   Default: ``10``

.. _item-conditionloweroffroad:

ConditionLowerOffroad
^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-conditionlowerstandard:

ConditionLowerStandard
^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-conditionmax:

ConditionMax
^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``10``

.. _item-consolidateoption:

ConsolidateOption
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-cookingsound:

CookingSound
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-corpsesicknessdefense:

CorpseSicknessDefense
^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-cosmetic:

Cosmetic
^^^^^^^^

   Type: ``Any``

No description

.. _item-count:

count
^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``1``

.. _item-critdmgmultiplier:

CritDmgMultiplier
^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

Multiplier applied to the damage of a hit if it is a critical hit, applied inside `IsoGameCharacter.Hit() <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/IsoGameCharacter.html#Hit(zombie.inventory.types.HandWeapon,zombie.characters.IsoGameCharacter,float,boolean,float,boolean>`_\ ). Two types of crits can trigger:


* A normal crit: ``damage *= max(2.0, CritDmgMultiplier)``
* Aim-at-floor stomp (melee only): ``damage *= max(5.0, CritDmgMultiplier)``

The default value of the ``HandWeapon`` class is ``2.0``. Values of ``3.0`` to ``5.0`` visibly spike crit damage while values above ``5.0`` also start boosting stomps.

   Default: ``2.0``

.. _item-criticalchance:

CriticalChance
^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

`CriticalChance <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-criticalchance>`_ sets the base critical hit chance of the weapon. The final ``CriticalChance`` value after all applied bonuses and penalties have been applied is compared on a 0-100 roll.

Below is a table listing the different elements which can influence the critical hit chance of a weapon:

.. list-table::
   :header-rows: 1

   * - Element
     - Type
     - Description
     - Formula
   * - `AimingPerkCritModifier <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-aimingperkcritmodifier>`_ and `aiming skill <https://pzwiki.net/wiki/Aiming>`_ of the character
     - Weapon parameter
     - The aiming level of the character impacts the player's critical hit chance by adding the following to the ``CriticalChance`` value.
     - ``CriticalChance += AimingPerkCritModifier * Aiming level``
   * - Sight bonus / penalty
     - Weapon parameter
     - In the formula, ``sightWindowBonus`` refers to the bonus from `MinSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-maxsightrange>`_. ``sightlessBonus`` on the other hand is a simpler parameter which uses a distance falloff when there is not active sight. The best path is used for the better result. The aim delay penalty depends on `Aimingtime <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-aimingtime>`_
     - ``CriticalChance += max(sightlessBonus - sightlessAimDelayPenalty, sightWindowBonus - sightWindowAimDelayPenalty)``
   * - Moodles penalty
     - Player condition
     - Being panicked, stressed, tired, drunk or lacking endurance will all negatively impact the ``CriticalChance``.
     - ``CriticalChance -= moodlesPenalty``
   * - Weather penalty
     - Environment
     - Wind, rain, fog, low-light will all negatively impact the ``CriticalChance``.
     - ``CriticalChance -= weatherPenalty``
   * - Movement penalty
     - Player condition
     - The shooter speed and the distance will negatively impact the ``CriticalChance``.
     - ``CriticalChance -= movementPenalty``
   * - `Marksman trait <https://pzwiki.net/wiki/Marksman>`_
     - Player condition
     - This condition can never be reached as the Marksman trait no longer exists.
     - ``CriticalChance += 10``


For PvP targets, the entire formula is bypassed and `StopPower <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-stoppower>`_ is used instead.

``CriticalChance`` sets the floor for unskilled players while ``AimingPerkCritModifier`` rewards more or less the character ability to aim. High modified and low base chance means the weapon is a skill-gated crit machine, making the weapon a sort of "experts" weapon.

   Default: ``20.0``

.. _item-customcontextmenu:

CustomContextMenu
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-customeatsound:

CustomEatSound
^^^^^^^^^^^^^^

   Type: ``Any``

Custom sound to play when eating or drinking this item, refers to the ID of a sound script. Set to an empty string to disable any sound from playing.

   Can be empty: ✓

.. _item-cyclicratemultiplier:

CyclicRateMultiplier
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-damagecategory:

DamageCategory
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-damagemakehole:

DamageMakeHole
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-dangerousuncooked:

DangerousUncooked
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-daysfresh:

DaysFresh
^^^^^^^^^

   Type: ``Any``

How many days this food item will stay fresh with default sandbox settings.

.. _item-daystotallyrotten:

DaysTotallyRotten
^^^^^^^^^^^^^^^^^

   Type: ``Any``

How many days this food item will take to rot.

.. _item-digitalpadlock:

DigitalPadlock
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-digtype:

DigType
^^^^^^^

   Type: ``Any``

No description

.. _item-disappearonuse:

DisappearOnUse
^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

No description

   Default: ``True``

.. _item-discomfortmodifier:

DiscomfortModifier
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-displaycategory:

DisplayCategory
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-displayname:

DisplayName
^^^^^^^^^^^

   Type: ``Any``

Sets the name of the item which will be displayed in-game. It's recommended to use a translation entry for this parameter to allow localization of the item name.

.. warning::

   **Deprecated** (since version 42.13.0)

   Naming an item should be done with a translation entry. See the `wiki <https://pzwiki.net/wiki/DisplayName>`_ page for more information.

.. _item-doordamage:

DoorDamage
^^^^^^^^^^

   Type: ``{'main': 'integer'}``

Damage dealt to doors, windows, barricades and some vehicle/object hits.

   Default: ``1``

.. _item-doorhitsound:

DoorHitSound
^^^^^^^^^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``BaseballBatHit``

.. _item-doubleclickrecipe:

DoubleClickRecipe
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-dropsound:

DropSound
^^^^^^^^^

   Type: ``Any``

No description

.. _item-eattime:

Eattime
^^^^^^^

   Type: ``Any``

No description

.. _item-eattype:

EatType
^^^^^^^

   Type: ``Any``

No description

.. _item-ejectammosound:

EjectAmmoSound
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-ejectammostartsound:

EjectAmmoStartSound
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-ejectammostopsound:

EjectAmmoStopSound
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-endurancechange:

enduranceChange
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-endurancemod:

EnduranceMod
^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-engineloudness:

engineLoudness
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-equippednosprint:

EquippedNoSprint
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-equipsound:

EquipSound
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-evolvedrecipe:

EvolvedRecipe
^^^^^^^^^^^^^

   Type: ``Any``

List of evolved recipes this item can be used in.

.. _item-evolvedrecipename:

EvolvedRecipeName
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-explosionduration:

ExplosionDuration
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-explosionpower:

ExplosionPower
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-explosionrange:

ExplosionRange
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-explosionsound:

ExplosionSound
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-explosiontimer:

ExplosionTimer
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-fabrictype:

FabricType
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-fatiguechange:

fatigueChange
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-fillfromdispensersound:

FillFromDispenserSound
^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-fillfromlakesound:

FillFromLakeSound
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-fillfromtapsound:

FillFromTapSound
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-fillfromtoiletsound:

FillFromToiletSound
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-firefuelratio:

FireFuelRatio
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-firemode:

FireMode
^^^^^^^^

   Type: ``Any``

No description

.. _item-firemodepossibilities:

FireModePossibilities
^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-firerange:

FireRange
^^^^^^^^^

   Type: ``Any``

No description

.. _item-firestartingchance:

FireStartingChance
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-firestartingenergy:

FireStartingEnergy
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-fishinglure:

FishingLure
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-flureduction:

fluReduction
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-foodsicknesschange:

FoodSicknessChange
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-foodtype:

FoodType
^^^^^^^^

   Type: ``Any``

No description

.. _item-goodhot:

GoodHot
^^^^^^^

   Type: ``Any``

No description

.. _item-guntype:

GunType
^^^^^^^

   Type: ``Any``

No description

.. _item-havechamber:

HaveChamber
^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

Whether the weapon has a chamber that can hold a round in addition to its magazine.

   Default: ``True``

.. _item-headcondition:

HeadCondition
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-headconditionlowerchancemultiplier:

HeadConditionLowerChanceMultiplier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-headconditionmax:

HeadConditionMax
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-hearingmodifier:

HearingModifier
^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-herbalisttype:

HerbalistType
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-hidden:

Hidden
^^^^^^

   Type: ``Any``

No description

.. _item-hitanglemod:

HitAngleMod
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-hitchance:

HitChance
^^^^^^^^^

   Type: ``{'main': 'integer'}``

`HitChance <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-hitchance>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `HitChanceModified <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-hitchancemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_.

The initial hitchance is determined by the following configuration:

.. code-block::

   HitChance = min(HitChance, CombatConfigKey.MAXIMUM_START_TO_HIT_CHANCE)

`MAXIMUM_START_TO_HIT_CHANCE <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/combat/CombatConfigKey.html#MAXIMUM_START_TO_HIT_CHANCE>`_ is a configuration of the combat system of Project Zomboid. In this case, the default value is ``95.0``\ , which means the initial HitChance cannot be above ``95.0``.

Below is a table listing the different elements which can influence the hit chance of a weapon:

.. list-table::
   :header-rows: 1

   * - Element
     - Type
     - Description
     - Formula
   * - `AimingPerkHitChanceModifier <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-aimingperkhitchancemodifier>`_ and `aiming skill <https://pzwiki.net/wiki/Aiming>`_ of the character
     - Weapon parameter
     - The aiming level of the character impacts the player's hit chance.
     - ``HitChance += AimingPerkHitChanceModifier * Aiming level``
   * - Sight bonus / penalty
     - Weapon parameter
     - In the formula, ``sightWindowBonus`` refers to the bonus from `MinSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-maxsightrange>`_. ``sightlessBonus`` on the other hand is a simpler parameter which uses a distance falloff when there is not active sight. The best path is used for the better result.
     - ``HitChance += max(sightlessBonus - sightlessAimDelayPenalty, sightWindowBonus - sightWindowAimDelayPenalty)``
   * - Moodles penalty
     - Player condition
     - Being panicked, stressed, tired, drunk or lacking endurance will all negatively impact the ``HitChance``.
     - ``HitChance -= moodlesPenalty``
   * - Weather penalty
     - Environment
     - Wind, rain, fog, low-light will all negatively impact the ``HitChance``.
     - ``HitChance -= weatherPenalty``
   * - Movement penalty
     - Player condition
     - The shooter speed and the distance will negatively impact the ``HitChance``.
     - ``HitChance -= movementPenalty``
   * - Arm pain penalty
     - Player condition
     - The character's level of `pain <https://pzwiki.net/wiki/Pain>`_ will impact its aiming.
     - ``HitChance -= armPainPenalty``
   * - Headgear vision penalty
     - Player condition
     - Headgear will impact aiming, if the relevant sandbox option is enabled.
     - ``HitChance -= headgearVisionPenalty``


The final obtained value of ``HitChance`` is clamped against the `MINIMUM_TO_HIT_CHANCE <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/combat/CombatConfigKey.html#MINIMUM_TO_HIT_CHANCE>`_ and `MAXIMUM_TO_HIT_CHANCE <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/combat/CombatConfigKey.html#MAXIMUM_TO_HIT_CHANCE>`_\ , both respectively equal to ``5.0`` and ``100.0`` by default.

At point-blank range, all combined penalties are scaled toward zero, so close shots are always more forgiving. The `HitChance <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-hitchance>`_ parameter will set the floor for all players while `AimingPerkHitChanceModifier <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-aimingperkhitchancemodifier>`_ will increase accuracy with the level of aiming of the player. Low base and high modifier makes the gun terrible while unskilled but excellent with investment in aiming.

.. _item-hitchancemodifier:

HitChanceModifier
^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

See :ref:`item-hitchance` for more details.

.. _item-hitfloorsound:

HitFloorSound
^^^^^^^^^^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``BatOnFloor``

.. _item-hitsound:

HitSound
^^^^^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``BaseballBatHit``

.. _item-hungerchange:

HungerChange
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-icon:

Icon
^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``None``

.. _item-iconcolormask:

IconColorMask
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-iconfluidmask:

IconFluidMask
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-iconsfortexture:

IconsForTexture
^^^^^^^^^^^^^^^

   Type: ``{'main': 'array', 'array': {'type': 'string', 'separator': ';'}}``

No description

.. _item-idleanim:

IdleAnim
^^^^^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``Idle``

.. _item-impactsound:

ImpactSound
^^^^^^^^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``BaseballBatHit``

.. _item-insertallbulletsreload:

InsertAllBulletsReload
^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-insertammosound:

InsertAmmoSound
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-insertammostartsound:

InsertAmmoStartSound
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-insertammostopsound:

InsertAmmoStopSound
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-insulation:

Insulation
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-inversecoughprobability:

InverseCoughProbability
^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-inversecoughprobabilitysmoker:

InverseCoughProbabilitySmoker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-isaimedfirearm:

IsAimedFirearm
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-isaimedhandweapon:

IsAimedHandWeapon
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-iscookable:

IsCookable
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-isdung:

IsDung
^^^^^^

   Type: ``Any``

No description

.. _item-ishightier:

IsHighTier
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-isportable:

IsPortable
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-istelevision:

IsTelevision
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-iswatersource:

IsWaterSource
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-itemaftercleaning:

ItemAfterCleaning
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-itemtype:

ItemType
^^^^^^^^

   Type: ``{'main': 'string'}`` *(required)*

Defines the class of the item which will impact which parameters the item can take and its properties as well as how it is used by the player. Clothing for instance will handle differently their texture and model in comparison to the other type of items, containers can hold items and weapons can be used by the player to attack and deal damage. You cannot use a custom class of item and only the ones accepted by the game.

   Allowed values:

   - ``base:alarmclock``
   - ``base:alarmclockclothing``
   - ``base:animal``
   - ``base:clothing``
   - ``base:container``
   - ``base:drainable``
   - ``base:food``
   - ``base:key``
   - ``base:literature``
   - ``base:map``
   - ``base:moveable``
   - ``base:normal``
   - ``base:radio``
   - ``base:weapon``
   - ``base:weaponpart``

.. _item-itemwhendry:

ItemWhenDry
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-jamgunchance:

JamGunChance
^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-keepondeplete:

KeepOnDeplete
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-knockbackonnodeath:

KnockBackOnNoDeath
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-knockdownmod:

KnockdownMod
^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-learnedrecipes:

LearnedRecipes
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-lightdistance:

LightDistance
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-lightstrength:

LightStrength
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-lipids:

Lipids
^^^^^^

   Type: ``Any``

No description

.. _item-lowlightbonus:

LowLightBonus
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-lvlskilltrained:

LvlSkillTrained
^^^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``-1``

.. _item-magazine_subject:

magazine_subject
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-magazinetype:

MagazineType
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-makeuptype:

MakeUpType
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-manuallyremovespentrounds:

ManuallyRemoveSpentRounds
^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-map:

Map
^^^

   Type: ``Any``

No description

.. _item-maxammo:

MaxAmmo
^^^^^^^

   Type: ``Any``

No description

.. _item-maxcapacity:

MaxCapacity
^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``-1``

.. _item-maxchannel:

MaxChannel
^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``108000``

.. _item-maxdamage:

MaxDamage
^^^^^^^^^

   Type: ``{'main': 'float'}``

Rolls the hit damage of the weapon between ``MinDamage`` and ``MaxDamage``.

   Default: ``1.5``

.. _item-maxhitcount:

MaxHitcount
^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``1000``

.. _item-maxitemsize:

MaxItemSize
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-maxrange:

MaxRange
^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-maxrangemodifier:

MaxRangeModifier
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-maxsightrange:

MaxSightRange
^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

`MinSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-maxsightrange>`_ define the optimal sight window, to be more specific, the distance band where hits and critical hits bonuses peak.

The `aiming skill <https://pzwiki.net/wiki/Aiming>`_ and `eagle eyed <https://pzwiki.net/wiki/Eagle_Eyed>`_ will impact these values:

.. code-block::

   effectiveMin = MinSightRange x (1 - AimingLevel / 30)
   effectiveMax = MaxSightRange x (1 + AimingLevel / 30) x (EagleEyed ? 1.2 : 1.0)

At aiming 10, the minimum shrinks by 33% and the max grows by 33%, which widens the window significantly. When the trait `Short Sighted <https://pzwiki.net/wiki/Short_Sighted>`_ is present and the character doesn't wear glasses, the ``effectiveMax`` equals ``effectiveMin``\ , making the entire bonus window disappear.

Inside the the ``effectiveMin`` and ``effectiveMax`` window, the bonus follows a `Gaussian <https://en.wikipedia.org/wiki/Bell-shaped_function>`_ with the bonus peaking at the midpoint. Aim-delay penalty is also reduced inside the window.

Below ``effectiveMin``\ , a small linear penalty is applied as the gun is not suited for point-blank. Above ``effectiveMax``\ , a growing quadratic penalty is applied, the bonus degrades rapidly past the edge.

A CQC gun should have a low `MaxSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-maxsightrange>`_ while a marksman riffle should have a high `MinSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-minsightrange>`_ with a wide window.

.. _item-mechanicsitem:

MechanicsItem
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-mediacategory:

MediaCategory
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-medical:

Medical
^^^^^^^

   Type: ``Any``

No description

.. _item-metalvalue:

MetalValue
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-micrange:

MicRange
^^^^^^^^

   Type: ``Any``

No description

.. _item-minangle:

MinAngle
^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-minchannel:

MinChannel
^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``88000``

.. _item-mindamage:

MinDamage
^^^^^^^^^

   Type: ``{'main': 'float'}``

See :ref:`item-maxdamage` for more details.

.. _item-minimumswingtime:

MinimumSwingtime
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-minrange:

MinRange
^^^^^^^^

   Type: ``{'main': 'float'}``

Hard minimum attack distance. If the target is closer than ``MinRange``\ , the ballistics controller does not register the shot and the game may force a melee swap. This is a binary threshold, not a penalty band. Separate from `MinSightRange <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-minsightrange>`_.

Long rifles should be hard to use in tight spaces. ``0.2`` to ``0.35`` is a small gap but ``0.61`` is noticeably limiting indoors.

.. _item-minsightrange:

MinSightRange
^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

See :ref:`item-maxsightrange` for more details.

.. _item-minutestoburn:

MinutesToBurn
^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

How many in-game minutes it takes to burn the food. This value must be higher than ``MinutesToCook``.

   Default: ``120.0``

.. _item-minutestocook:

MinutesToCook
^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

How many in-game minutes it takes to cook the food. This value must be smaller than ``MinutesToBurn``.

   Default: ``60.0``

.. _item-modelweaponpart:

ModelWeaponPart
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

   Can be duplicated: ✓

.. _item-mounton:

MountOn
^^^^^^^

   Type: ``Any``

No description

.. _item-multiplehitconditionaffected:

MultipleHitConditionAffected
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

No description

   Default: ``True``

.. _item-muzzleflashmodelkey:

MuzzleFlashModelKey
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-neckprotectionmodifier:

NeckProtectionModifier
^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-needtobeclosedoncereload:

needtobeclosedoncereload
^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-noiseduration:

NoiseDuration
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-noiserange:

NoiseRange
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-notransmit:

NoTransmit
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-npcsoundboost:

NPCSoundBoost
^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-numberofpages:

NumberOfPages
^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``-1``

.. _item-numlevelstrained:

NumLevelsTrained
^^^^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``1``

.. _item-onbreak:

OnBreak
^^^^^^^

   Type: ``Any``

No description

.. _item-oncooked:

OnCooked
^^^^^^^^

   Type: ``Any``

No description

.. _item-oncreate:

OnCreate
^^^^^^^^

   Type: ``Any``

No description

.. _item-oneat:

OnEat
^^^^^

   Type: ``Any``

No description

.. _item-openingrecipe:

OpeningRecipe
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-opensound:

OpenSound
^^^^^^^^^

   Type: ``Any``

No description

.. _item-originx:

OriginX
^^^^^^^

   Type: ``Any``

No description

.. _item-originy:

OriginY
^^^^^^^

   Type: ``Any``

No description

.. _item-originz:

originZ
^^^^^^^

   Type: ``Any``

No description

.. _item-otherhandrequire:

OtherHandRequire
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-otherhanduse:

OtherHandUse
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-packaged:

Packaged
^^^^^^^^

   Type: ``Any``

No description

.. _item-padlock:

Padlock
^^^^^^^

   Type: ``Any``

No description

.. _item-pagetowrite:

PageToWrite
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-painreduction:

painReduction
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-parttype:

PartType
^^^^^^^^

   Type: ``Any``

No description

.. _item-physicsobject:

PhysicsObject
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-piercingbullets:

PiercingBullets
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-placedsprite:

PlacedSprite
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-placemultiplesound:

PlaceMultipleSound
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-placeonesound:

PlaceOneSound
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-poisonpower:

PoisonPower
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-pourtype:

PourType
^^^^^^^^

   Type: ``Any``

No description

.. _item-primaryanimmask:

primaryAnimMask
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-projectilecount:

Projectilecount
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-projectilespread:

ProjectileSpread
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-projectilespreadmodifier:

ProjectileSpreadModifier
^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-projectileweightcenter:

ProjectileWeightCenter
^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-protectfromrainwhenequipped:

ProtectFromRainWhenEquipped
^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-proteins:

Proteins
^^^^^^^^

   Type: ``Any``

No description

.. _item-pushbackmod:

PushBackMod
^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-putinsound:

PutInSound
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-rackaftershoot:

RackAfterShoot
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-racksound:

RackSound
^^^^^^^^^

   Type: ``Any``

No description

.. _item-rainfactor:

RainFactor
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-ranged:

Ranged
^^^^^^

   Type: ``Any``

No description

.. _item-rangefalloff:

RangeFalloff
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-readtype:

ReadType
^^^^^^^^

   Type: ``Any``

No description

.. _item-recoildelay:

RecoilDelay
^^^^^^^^^^^

   Type: ``Any``

`RecoilDelay <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-recoildelay>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `AimingTimeModifier <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-recoildelaymodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_. Weapon attachments will add or subtract from `RecoilDelay <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/item.html#item-recoildelay>`_ directly.

Controls how long post-shot recovery takes before aim settling can begin. High values means the gun has a huge kick and forces a pause. Lower values is a flat, fast and snappy gun. `Strength <https://pzwiki.net/wiki/Strength>`_ and `aiming <https://pzwiki.net/wiki/Aiming>`_ will both reduce the recoil delay. Holding the gun one-handed will negatively impact the recoil handling. The following formula is used:

.. code-block:: java

   effectiveDelay = RecoilDelay
                 * (1 - AimingLevel / 40)
                 * (1 - (StrengthLevel * 2 - 10) / 40)
                 * (one-handed penalty: * 1.3 if primary hand only, secondary empty)

Aim countdown starts when the recoil delay counter is less than ``effectiveDelay * AimingLevel / 30``. Higher aiming also lets aim recovery start earlier in the recoil window.

.. _item-recoildelaymodifier:

RecoilDelayModifier
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

See :ref:`item-recoildelay` for more details.

.. _item-reduceinfectionpower:

ReduceInfectionPower
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-reloadtime:

Reloadtime
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-reloadtimemodifier:

ReloadTimeModifier
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-remotecontroller:

RemoteController
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-remoterange:

RemoteRange
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-removenegativeeffectoncooked:

RemoveNegativeEffectOnCooked
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-removeonbroken:

RemoveOnBroken
^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

No description

   Default: ``True``

.. _item-removeunhappinesswhencooked:

RemoveUnhappinessWhenCooked
^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-replaceinprimaryhand:

ReplaceInPrimaryHand
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-replaceinsecondhand:

ReplaceInSecondHand
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-replaceoncooked:

ReplaceOnCooked
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-replaceondeplete:

ReplaceOnDeplete
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-replaceonextinguish:

ReplaceOnExtinguish
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-replaceonrotten:

ReplaceOnRotten
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-replaceonuse:

ReplaceOnUse
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-requireinhandorinventory:

RequireInHandOrInventory
^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-requiresequippedbothhands:

RequiresEquippedBothHands
^^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-researchablerecipes:

Researchablerecipes
^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'array', 'array': {'type': 'string', 'separator': ';'}}``

No description

.. _item-runanim:

RunAnim
^^^^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``Run``

.. _item-runspeedmodifier:

RunSpeedModifier
^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-scaleworldicon:

ScaleWorldIcon
^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-scratchdefense:

ScratchDefense
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-secondaryanimmask:

secondaryAnimMask
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-sensorrange:

SensorRange
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-sharpness:

Sharpness
^^^^^^^^^

   Type: ``Any``

No description

.. _item-shellfallsound:

ShellFallSound
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-shoutmultiplier:

ShoutMultiplier
^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-shouttype:

ShoutType
^^^^^^^^^

   Type: ``Any``

No description

.. _item-skilltrained:

SkillTrained
^^^^^^^^^^^^

   Type: ``{'main': 'string'}``

No description

.. _item-smokerange:

SmokeRange
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-soundgain:

SoundGain
^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-soundmap:

SoundMap
^^^^^^^^

   Type: ``Any``

No description

   Can be duplicated: ✓

.. _item-soundparameter:

SoundParameter
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-soundradius:

SoundRadius
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-soundvolume:

SoundVolume
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-spawnwith:

SpawnWith
^^^^^^^^^

   Type: ``Any``

No description

.. _item-spice:

Spice
^^^^^

   Type: ``Any``

No description

.. _item-splatbloodonnodeath:

SplatBloodOnNoDeath
^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-splatnumber:

SplatNumber
^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``2``

.. _item-splatsize:

SplatSize
^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-staticmodel:

StaticModel
^^^^^^^^^^^

   Type: ``{'main': 'string', 'block': {'name': 'model', 'fullType': True}}``

No description

.. _item-staticmodelsbyindex:

StaticModelsByIndex
^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'array', 'array': {'type': 'string', 'separator': ';'}}``

No description

.. _item-stomppower:

StompPower
^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-stoppower:

StopPower
^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``5.0``

.. _item-stresschange:

StressChange
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-subcategory:

SubCategory
^^^^^^^^^^^

   Type: ``{'main': 'string'}``

No description

.. _item-survivalgear:

SurvivalGear
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-suspensioncompression:

suspensionCompression
^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-suspensiondamping:

suspensionDamping
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-swingamountbeforeimpact:

SwingAmountBeforeImpact
^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-swinganim:

SwingAnim
^^^^^^^^^

   Type: ``{'main': 'string'}``

No description

   Default: ``Rifle``

.. _item-swingsound:

SwingSound
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-swingtime:

Swingtime
^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-tags:

Tags
^^^^

   Type: ``{'main': 'array', 'array': {'type': 'string', 'separator': ';'}}``

No description

.. _item-thirstchange:

ThirstChange
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-ticksperequipuse:

ticksPerEquipUse
^^^^^^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

   Default: ``30``

.. _item-tohitmodifier:

ToHitModifier
^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-tooltip:

Tooltip
^^^^^^^

   Type: ``Any``

No description

.. _item-torchcone:

TorchCone
^^^^^^^^^

   Type: ``Any``

No description

.. _item-torchdot:

TorchDot
^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``0.96``

.. _item-transmitrange:

TransmitRange
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-trap:

Trap
^^^^

   Type: ``{'main': 'boolean'}``

No description

   Default: ``False``

.. _item-treedamage:

TreeDamage
^^^^^^^^^^

   Type: ``Any``

No description

.. _item-triggerexplosiontimer:

triggerExplosionTimer
^^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-twohandweapon:

TwoHandWeapon
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-twoway:

TwoWay
^^^^^^

   Type: ``Any``

No description

.. _item-type:

Type
^^^^

   Type: ``Any``

Used to set the class of the item, which will influence parameters available.

.. warning::

   **Deprecated** (since version 42.13.0)

   Use :ref:`item-itemtype` instead.

.. _item-unequipsound:

UnequipSound
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-unhappychange:

UnhappyChange
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-usedelta:

UseDelta
^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``0.03125``

.. _item-useendurance:

UseEndurance
^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

No description

   Default: ``True``

.. _item-usesbattery:

UsesBattery
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-useself:

UseSelf
^^^^^^^

   Type: ``Any``

No description

.. _item-usewhileequipped:

UseWhileEquipped
^^^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

No description

   Default: ``True``

.. _item-usewhileunequipped:

UseWhileUnequipped
^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-useworlditem:

UseWorldItem
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-vehiclepartmodel:

VehiclePartModel
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-vehicletype:

VehicleType
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-visionmodifier:

VisionModifier
^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-visualaid:

VisualAid
^^^^^^^^^

   Type: ``Any``

No description

.. _item-waterresistance:

WaterResistance
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-weaponhitarmoursound:

WeaponHitArmourSound
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-weaponlength:

WeaponLength
^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``0.4``

.. _item-weaponreloadtype:

WeaponReloadType
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-weaponsprite:

WeaponSprite
^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-weaponspritesbyindex:

WeaponSpritesByIndex
^^^^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-weaponweight:

WeaponWeight
^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-weight:

Weight
^^^^^^

   Type: ``{'main': 'float'}``

No description

   Default: ``1.0``

.. _item-weightempty:

WeightEmpty
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-weightmodifier:

WeightModifier
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-weightreduction:

WeightReduction
^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-wet:

Wet
^^^

   Type: ``Any``

No description

.. _item-wetcooldown:

WetCooldown
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-wheelfriction:

wheelFriction
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-windresistance:

WindResistance
^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-withdrainable:

WithDrainable
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-withoutdrainable:

WithoutDrainable
^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-worldobjectsprite:

WorldObjectSprite
^^^^^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-worldrender:

WorldRender
^^^^^^^^^^^

   Type: ``Any``

No description

.. _item-worldstaticmodel:

WorldStaticModel
^^^^^^^^^^^^^^^^

   Type: ``{'main': 'string', 'block': {'name': 'model', 'fullType': True}}``

No description

.. _item-worldstaticmodelsbyindex:

WorldStaticModelsByIndex
^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'array', 'array': {'type': 'string', 'separator': ';'}}``

No description

