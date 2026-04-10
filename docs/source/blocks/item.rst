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

**AcceptItemFunction** `🔗 <#item-acceptitemfunction>`_
   Type: ``Any``

   No description

   Item types: container

.. _item-acceptmediatype:

**AcceptMediaType** `🔗 <#item-acceptmediatype>`_
   Type: ``integer``

   No description

   Default: ``-1``

   Item types: radio

.. _item-activateditem:

**ActivatedItem** `🔗 <#item-activateditem>`_
   Type: ``Any``

   No description

   Item types: clothing, drainable, weaponpart

.. _item-aimingmod:

**AimingMod** `🔗 <#item-aimingmod>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-aimingperkcritmodifier:

**AimingPerkCritModifier** `🔗 <#item-aimingperkcritmodifier>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-aimingperkhitchancemodifier:

**AimingPerkHitChanceModifier** `🔗 <#item-aimingperkhitchancemodifier>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-aimingperkminanglemodifier:

**AimingPerkMinAngleModifier** `🔗 <#item-aimingperkminanglemodifier>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-aimingperkrangemodifier:

**AimingPerkRangeModifier** `🔗 <#item-aimingperkrangemodifier>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-aimingtime:

**Aimingtime** `🔗 <#item-aimingtime>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-aimingtimemodifier:

**AimingTimeModifier** `🔗 <#item-aimingtimemodifier>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-aimreleasesound:

**AimReleaseSound** `🔗 <#item-aimreleasesound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-alarmsound:

**AlarmSound** `🔗 <#item-alarmsound>`_
   Type: ``Any``

   No description

   Item types: alarmclock, alarmclockclothing

.. _item-alcoholic:

**Alcoholic** `🔗 <#item-alcoholic>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-alcoholpower:

**AlcoholPower** `🔗 <#item-alcoholpower>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-alwaysknockdown:

**AlwaysKnockdown** `🔗 <#item-alwaysknockdown>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-alwayswelcomegift:

**AlwaysWelcomeGift** `🔗 <#item-alwayswelcomegift>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-ammobox:

**AmmoBox** `🔗 <#item-ammobox>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-ammotype:

**AmmoType** `🔗 <#item-ammotype>`_
   Type: ``Any``

   No description

   Item types: normal, weapon

.. _item-anglefalloff:

**AngleFalloff** `🔗 <#item-anglefalloff>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-animalfeedtype:

**AnimalFeedType** `🔗 <#item-animalfeedtype>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-attachmentreplacement:

**AttachmentReplacement** `🔗 <#item-attachmentreplacement>`_
   Type: ``Any``

   No description

   Item types: container, radio

.. _item-attachmentsprovided:

**AttachmentsProvided** `🔗 <#item-attachmentsprovided>`_
   Type: ``Any``

   No description

   Item types: clothing, container

.. _item-attachmenttype:

**AttachmentType** `🔗 <#item-attachmenttype>`_
   Type: ``Any``

   No description

   Item types: drainable, normal, radio, weapon

.. _item-badcold:

**BadCold** `🔗 <#item-badcold>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-badinmicrowave:

**BadInMicrowave** `🔗 <#item-badinmicrowave>`_
   Type: ``Any``

   Used to set whether this item can cause a fire when put in a microwave, if set to true it will explode.

   Item types: food

.. _item-bandagepower:

**BandagePower** `🔗 <#item-bandagepower>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-basespeed:

**BaseSpeed** `🔗 <#item-basespeed>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-basevolumerange:

**BaseVolumeRange** `🔗 <#item-basevolumerange>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-bitedefense:

**BiteDefense** `🔗 <#item-bitedefense>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-bloodlocation:

**BloodLocation** `🔗 <#item-bloodlocation>`_
   Type: ``array``

   No description

   Item types: clothing, container, normal, radio

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

**BodyLocation** `🔗 <#item-bodylocation>`_
   Type: ``Any``

   Used to define which location on the human character this clothing item can be worn.

   Item types: alarmclockclothing, clothing, container, normal

.. _item-book_subject:

**book_subject** `🔗 <#item-book_subject>`_
   Type: ``Any``

   No description

   Item types: container, literature

.. _item-boredomchange:

**BoredomChange** `🔗 <#item-boredomchange>`_
   Type: ``Any``

   No description

   Item types: food, literature

.. _item-brakeforce:

**brakeForce** `🔗 <#item-brakeforce>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-breaksound:

**BreakSound** `🔗 <#item-breaksound>`_
   Type: ``Any``

   No description

   Item types: clothing, normal, weapon

.. _item-bringtobearsound:

**BringToBearSound** `🔗 <#item-bringtobearsound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-bulletdefense:

**BulletDefense** `🔗 <#item-bulletdefense>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-bullethitarmoursound:

**BulletHitArmourSound** `🔗 <#item-bullethitarmoursound>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-calories:

**Calories** `🔗 <#item-calories>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-canattach:

**CanAttach** `🔗 <#item-canattach>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-canbandage:

**CanBandage** `🔗 <#item-canbandage>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-canbarricade:

**CanBarricade** `🔗 <#item-canbarricade>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-canbeequipped:

**CanBeEquipped** `🔗 <#item-canbeequipped>`_
   Type: ``Any``

   No description

   Item types: container, radio

.. _item-canbeplaced:

**CanBePlaced** `🔗 <#item-canbeplaced>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-canberemote:

**CanBeRemote** `🔗 <#item-canberemote>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-canbereused:

**CanBeReused** `🔗 <#item-canbereused>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-canbewrite:

**CanBeWrite** `🔗 <#item-canbewrite>`_
   Type: ``Any``

   No description

   Item types: literature

.. _item-candetach:

**CanDetach** `🔗 <#item-candetach>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-canhaveholes:

**CanHaveHoles** `🔗 <#item-canhaveholes>`_
   Type: ``boolean``

   Used to define whenever this item can get holes in it.

   Default: ``True``

   Item types: clothing, container, normal

.. _item-cannedfood:

**CannedFood** `🔗 <#item-cannedfood>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-canstack:

**CanStack** `🔗 <#item-canstack>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-canstorewater:

**CanStoreWater** `🔗 <#item-canstorewater>`_
   Type: ``Any``

   No description

   Item types: drainable, normal, weapon

.. _item-cantattackwithlowestendurance:

**CantAttackWithLowestEndurance** `🔗 <#item-cantattackwithlowestendurance>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-cantbeconsolided:

**cantBeConsolided** `🔗 <#item-cantbeconsolided>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-cantbefrozen:

**CantBeFrozen** `🔗 <#item-cantbefrozen>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-canteat:

**CantEat** `🔗 <#item-canteat>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-capacity:

**Capacity** `🔗 <#item-capacity>`_
   Type: ``integer``

   No description

   Default: ``-1``

   Item types: container

.. _item-carbohydrates:

**Carbohydrates** `🔗 <#item-carbohydrates>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-categories:

**Categories** `🔗 <#item-categories>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-chancetofall:

**ChanceToFall** `🔗 <#item-chancetofall>`_
   Type: ``Any``

   No description

   Item types: clothing, normal

.. _item-chancetospawndamaged:

**ChanceToSpawnDamaged** `🔗 <#item-chancetospawndamaged>`_
   Type: ``Any``

   No description

   Item types: drainable, normal

.. _item-clicksound:

**ClickSound** `🔗 <#item-clicksound>`_
   Type: ``string``

   No description

   Default: ``Stormy9mmClick``

   Item types: weapon

.. _item-clipsize:

**ClipSize** `🔗 <#item-clipsize>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-closekillmove:

**CloseKillMove** `🔗 <#item-closekillmove>`_
   Type: ``Any``

   Used to whenever this weapon can be used to do a close kill move, like knives to assassinate in the back.

   Item types: weapon

.. _item-closesound:

**CloseSound** `🔗 <#item-closesound>`_
   Type: ``Any``

   No description

   Item types: container

.. _item-clothingextrasubmenu:

**ClothingExtraSubmenu** `🔗 <#item-clothingextrasubmenu>`_
   Type: ``Any``

   ``ClothingItem`` references the clothing defined inside the `clothing.xml <https://pzwiki.net/wiki/Clothing.xml>`_ file. ``ClothingExtraSubmenu`` will define the name of the context menu option to equip the clothing item.
   
   ``ClothingItemExtra`` and ``ClothingItemExtraOption`` are used to define additional clothing equip options, they reference another item script block.

   Item types: alarmclockclothing, clothing, container

.. _item-clothingitem:

**ClothingItem** `🔗 <#item-clothingitem>`_
   Type: ``Any``

   ``ClothingItem`` references the clothing defined inside the `clothing.xml <https://pzwiki.net/wiki/Clothing.xml>`_ file. ``ClothingExtraSubmenu`` will define the name of the context menu option to equip the clothing item.
   
   ``ClothingItemExtra`` and ``ClothingItemExtraOption`` are used to define additional clothing equip options, they reference another item script block.

   Item types: alarmclockclothing, clothing, container, radio

.. _item-clothingitemextra:

**ClothingItemExtra** `🔗 <#item-clothingitemextra>`_
   Type: ``Any``

   ``ClothingItem`` references the clothing defined inside the `clothing.xml <https://pzwiki.net/wiki/Clothing.xml>`_ file. ``ClothingExtraSubmenu`` will define the name of the context menu option to equip the clothing item.
   
   ``ClothingItemExtra`` and ``ClothingItemExtraOption`` are used to define additional clothing equip options, they reference another item script block.

   Item types: alarmclockclothing, clothing, container

.. _item-clothingitemextraoption:

**ClothingItemExtraOption** `🔗 <#item-clothingitemextraoption>`_
   Type: ``Any``

   ``ClothingItem`` references the clothing defined inside the `clothing.xml <https://pzwiki.net/wiki/Clothing.xml>`_ file. ``ClothingExtraSubmenu`` will define the name of the context menu option to equip the clothing item.
   
   ``ClothingItemExtra`` and ``ClothingItemExtraOption`` are used to define additional clothing equip options, they reference another item script block.

   Item types: alarmclockclothing, clothing, container

.. _item-colorblue:

**ColorBlue** `🔗 <#item-colorblue>`_
   Type: ``integer``

   No description

   Default: ``255``

   Item types: clothing, food, literature, normal, weapon

.. _item-colorgreen:

**ColorGreen** `🔗 <#item-colorgreen>`_
   Type: ``integer``

   No description

   Default: ``255``

   Item types: clothing, food, literature, normal, weapon

.. _item-colorred:

**ColorRed** `🔗 <#item-colorred>`_
   Type: ``integer``

   No description

   Default: ``255``

   Item types: clothing, food, literature, normal, weapon

.. _item-combatspeedmodifier:

**CombatSpeedModifier** `🔗 <#item-combatspeedmodifier>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: clothing, container

.. _item-conditionaffectscapacity:

**ConditionAffectsCapacity** `🔗 <#item-conditionaffectscapacity>`_
   Type: ``Any``

   Set whenever condition of the item can impact the capacity value of the container.

   Item types: normal

.. _item-conditionlowerchanceonein:

**ConditionLowerChanceOneIn** `🔗 <#item-conditionlowerchanceonein>`_
   Type: ``integer``

   The chance impact to reduce the durability of the item, the value is used to calculate the chance by doing $chance = 1/ConditionLowerChanceOneIn$, which means increasing this parameter value will reduce the chance to damage the item.

   Default: ``10``

   Item types: clothing, normal, weapon

.. _item-conditionloweroffroad:

**ConditionLowerOffroad** `🔗 <#item-conditionloweroffroad>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-conditionlowerstandard:

**ConditionLowerStandard** `🔗 <#item-conditionlowerstandard>`_
   Type: ``Any``

   No description

   Item types: drainable, normal

.. _item-conditionmax:

**ConditionMax** `🔗 <#item-conditionmax>`_
   Type: ``integer``

   No description

   Default: ``10``

   Item types: clothing, container, drainable, food, normal, radio, weapon

.. _item-consolidateoption:

**ConsolidateOption** `🔗 <#item-consolidateoption>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-cookingsound:

**CookingSound** `🔗 <#item-cookingsound>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-corpsesicknessdefense:

**CorpseSicknessDefense** `🔗 <#item-corpsesicknessdefense>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-cosmetic:

**Cosmetic** `🔗 <#item-cosmetic>`_
   Type: ``Any``

   No description

   Item types: alarmclockclothing, clothing

.. _item-count:

**count** `🔗 <#item-count>`_
   Type: ``integer``

   No description

   Default: ``1``

   Item types: normal

.. _item-critdmgmultiplier:

**CritDmgMultiplier** `🔗 <#item-critdmgmultiplier>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-criticalchance:

**CriticalChance** `🔗 <#item-criticalchance>`_
   Type: ``float``

   No description

   Default: ``20.0``

   Item types: weapon

.. _item-customcontextmenu:

**CustomContextMenu** `🔗 <#item-customcontextmenu>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-customeatsound:

**CustomEatSound** `🔗 <#item-customeatsound>`_
   Type: ``Any``

   Custom sound to play when eating or drinking this item, refers to the ID of a sound script. Set to an empty string to disable any sound from playing.

   Can be empty: ✓

   Item types: drainable, food, normal

.. _item-cyclicratemultiplier:

**CyclicRateMultiplier** `🔗 <#item-cyclicratemultiplier>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-damagecategory:

**DamageCategory** `🔗 <#item-damagecategory>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-damagemakehole:

**DamageMakeHole** `🔗 <#item-damagemakehole>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-dangerousuncooked:

**DangerousUncooked** `🔗 <#item-dangerousuncooked>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-daysfresh:

**DaysFresh** `🔗 <#item-daysfresh>`_
   Type: ``Any``

   How many days this food item will stay fresh with default sandbox settings.

   Item types: food

.. _item-daystotallyrotten:

**DaysTotallyRotten** `🔗 <#item-daystotallyrotten>`_
   Type: ``Any``

   How many days this food item will take to rot.

   Item types: food

.. _item-digitalpadlock:

**DigitalPadlock** `🔗 <#item-digitalpadlock>`_
   Type: ``Any``

   No description

   Item types: key

.. _item-digtype:

**DigType** `🔗 <#item-digtype>`_
   Type: ``Any``

   No description

   Item types: normal, weapon

.. _item-disappearonuse:

**DisappearOnUse** `🔗 <#item-disappearonuse>`_
   Type: ``boolean``

   No description

   Default: ``True``

   Item types: drainable, radio, weaponpart

.. _item-discomfortmodifier:

**DiscomfortModifier** `🔗 <#item-discomfortmodifier>`_
   Type: ``Any``

   No description

   Item types: clothing, container

.. _item-displaycategory:

**DisplayCategory** `🔗 <#item-displaycategory>`_
   Type: ``Any``

   No description

.. _item-displayname:

**DisplayName** `🔗 <#item-displayname>`_
   Type: ``Any``

   Sets the name of the item which will be displayed in-game. It's recommended to use a translation entry for this parameter to allow localization of the item name.

   .. warning::

      **Deprecated** (since version 42.13.0)

      Naming an item should be done with a translation entry. See the `wiki <https://pzwiki.net/wiki/DisplayName>`_ page for more information.

.. _item-doordamage:

**DoorDamage** `🔗 <#item-doordamage>`_
   Type: ``integer``

   No description

   Default: ``1``

   Item types: weapon

.. _item-doorhitsound:

**DoorHitSound** `🔗 <#item-doorhitsound>`_
   Type: ``string``

   No description

   Default: ``BaseballBatHit``

   Item types: weapon

.. _item-doubleclickrecipe:

**DoubleClickRecipe** `🔗 <#item-doubleclickrecipe>`_
   Type: ``Any``

   No description

   Item types: drainable, food, literature, normal

.. _item-dropsound:

**DropSound** `🔗 <#item-dropsound>`_
   Type: ``Any``

   No description

   Item types: normal, weapon

.. _item-eattime:

**Eattime** `🔗 <#item-eattime>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-eattype:

**EatType** `🔗 <#item-eattype>`_
   Type: ``Any``

   No description

   Item types: clothing, drainable, food, normal, weapon

.. _item-ejectammosound:

**EjectAmmoSound** `🔗 <#item-ejectammosound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-ejectammostartsound:

**EjectAmmoStartSound** `🔗 <#item-ejectammostartsound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-ejectammostopsound:

**EjectAmmoStopSound** `🔗 <#item-ejectammostopsound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-endurancechange:

**enduranceChange** `🔗 <#item-endurancechange>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-endurancemod:

**EnduranceMod** `🔗 <#item-endurancemod>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-engineloudness:

**engineLoudness** `🔗 <#item-engineloudness>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-equippednosprint:

**EquippedNoSprint** `🔗 <#item-equippednosprint>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-equipsound:

**EquipSound** `🔗 <#item-equipsound>`_
   Type: ``Any``

   No description

   Item types: container, drainable, weapon

.. _item-evolvedrecipe:

**EvolvedRecipe** `🔗 <#item-evolvedrecipe>`_
   Type: ``Any``

   List of evolved recipes this item can be used in.

   Item types: drainable, food

.. _item-evolvedrecipename:

**EvolvedRecipeName** `🔗 <#item-evolvedrecipename>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-explosionduration:

**ExplosionDuration** `🔗 <#item-explosionduration>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-explosionpower:

**ExplosionPower** `🔗 <#item-explosionpower>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-explosionrange:

**ExplosionRange** `🔗 <#item-explosionrange>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-explosionsound:

**ExplosionSound** `🔗 <#item-explosionsound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-explosiontimer:

**ExplosionTimer** `🔗 <#item-explosiontimer>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-fabrictype:

**FabricType** `🔗 <#item-fabrictype>`_
   Type: ``Any``

   No description

   Item types: clothing, normal

.. _item-fatiguechange:

**fatigueChange** `🔗 <#item-fatiguechange>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-fillfromdispensersound:

**FillFromDispenserSound** `🔗 <#item-fillfromdispensersound>`_
   Type: ``Any``

   No description

   Item types: drainable, normal

.. _item-fillfromlakesound:

**FillFromLakeSound** `🔗 <#item-fillfromlakesound>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-fillfromtapsound:

**FillFromTapSound** `🔗 <#item-fillfromtapsound>`_
   Type: ``Any``

   No description

   Item types: drainable, normal

.. _item-fillfromtoiletsound:

**FillFromToiletSound** `🔗 <#item-fillfromtoiletsound>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-firefuelratio:

**FireFuelRatio** `🔗 <#item-firefuelratio>`_
   Type: ``Any``

   No description

   Item types: drainable, moveable, normal, weapon

.. _item-firemode:

**FireMode** `🔗 <#item-firemode>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-firemodepossibilities:

**FireModePossibilities** `🔗 <#item-firemodepossibilities>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-firerange:

**FireRange** `🔗 <#item-firerange>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-firestartingchance:

**FireStartingChance** `🔗 <#item-firestartingchance>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-firestartingenergy:

**FireStartingEnergy** `🔗 <#item-firestartingenergy>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-fishinglure:

**FishingLure** `🔗 <#item-fishinglure>`_
   Type: ``Any``

   No description

   Item types: food, normal

.. _item-flureduction:

**fluReduction** `🔗 <#item-flureduction>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-foodsicknesschange:

**FoodSicknessChange** `🔗 <#item-foodsicknesschange>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-foodtype:

**FoodType** `🔗 <#item-foodtype>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-goodhot:

**GoodHot** `🔗 <#item-goodhot>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-guntype:

**GunType** `🔗 <#item-guntype>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-havechamber:

**HaveChamber** `🔗 <#item-havechamber>`_
   Type: ``boolean``

   Whether the weapon has a chamber that can hold a round in addition to its magazine.

   Default: ``True``

   Item types: weapon

.. _item-headcondition:

**HeadCondition** `🔗 <#item-headcondition>`_
   Type: ``Any``

   No description

   Item types: normal, weapon

.. _item-headconditionlowerchancemultiplier:

**HeadConditionLowerChanceMultiplier** `🔗 <#item-headconditionlowerchancemultiplier>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: normal, weapon

.. _item-headconditionmax:

**HeadConditionMax** `🔗 <#item-headconditionmax>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-hearingmodifier:

**HearingModifier** `🔗 <#item-hearingmodifier>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: clothing

.. _item-herbalisttype:

**HerbalistType** `🔗 <#item-herbalisttype>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-hidden:

**Hidden** `🔗 <#item-hidden>`_
   Type: ``Any``

   No description

.. _item-hitanglemod:

**HitAngleMod** `🔗 <#item-hitanglemod>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-hitchance:

**HitChance** `🔗 <#item-hitchance>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-hitchancemodifier:

**HitChanceModifier** `🔗 <#item-hitchancemodifier>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-hitfloorsound:

**HitFloorSound** `🔗 <#item-hitfloorsound>`_
   Type: ``string``

   No description

   Default: ``BatOnFloor``

   Item types: weapon

.. _item-hitsound:

**HitSound** `🔗 <#item-hitsound>`_
   Type: ``string``

   No description

   Default: ``BaseballBatHit``

   Item types: weapon

.. _item-hungerchange:

**HungerChange** `🔗 <#item-hungerchange>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-icon:

**Icon** `🔗 <#item-icon>`_
   Type: ``string``

   No description

   Default: ``None``

.. _item-iconcolormask:

**IconColorMask** `🔗 <#item-iconcolormask>`_
   Type: ``Any``

   No description

   Item types: drainable, literature, normal, weapon

.. _item-iconfluidmask:

**IconFluidMask** `🔗 <#item-iconfluidmask>`_
   Type: ``Any``

   No description

   Item types: normal, weapon

.. _item-iconsfortexture:

**IconsForTexture** `🔗 <#item-iconsfortexture>`_
   Type: ``array``

   No description

   Item types: clothing, container, food, key, literature, normal, weapon

.. _item-idleanim:

**IdleAnim** `🔗 <#item-idleanim>`_
   Type: ``string``

   No description

   Default: ``Idle``

   Item types: weapon

.. _item-impactsound:

**ImpactSound** `🔗 <#item-impactsound>`_
   Type: ``string``

   No description

   Default: ``BaseballBatHit``

   Item types: weapon

.. _item-insertallbulletsreload:

**InsertAllBulletsReload** `🔗 <#item-insertallbulletsreload>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-insertammosound:

**InsertAmmoSound** `🔗 <#item-insertammosound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-insertammostartsound:

**InsertAmmoStartSound** `🔗 <#item-insertammostartsound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-insertammostopsound:

**InsertAmmoStopSound** `🔗 <#item-insertammostopsound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-insulation:

**Insulation** `🔗 <#item-insulation>`_
   Type: ``Any``

   No description

   Item types: clothing, normal

.. _item-inversecoughprobability:

**InverseCoughProbability** `🔗 <#item-inversecoughprobability>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-inversecoughprobabilitysmoker:

**InverseCoughProbabilitySmoker** `🔗 <#item-inversecoughprobabilitysmoker>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-isaimedfirearm:

**IsAimedFirearm** `🔗 <#item-isaimedfirearm>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-isaimedhandweapon:

**IsAimedHandWeapon** `🔗 <#item-isaimedhandweapon>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-iscookable:

**IsCookable** `🔗 <#item-iscookable>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal, weapon

.. _item-isdung:

**IsDung** `🔗 <#item-isdung>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-ishightier:

**IsHighTier** `🔗 <#item-ishightier>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-isportable:

**IsPortable** `🔗 <#item-isportable>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-istelevision:

**IsTelevision** `🔗 <#item-istelevision>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-iswatersource:

**IsWaterSource** `🔗 <#item-iswatersource>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-itemaftercleaning:

**ItemAfterCleaning** `🔗 <#item-itemaftercleaning>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-itemtype:

**ItemType** `🔗 <#item-itemtype>`_
   Type: ``string`` *(required)*

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

**ItemWhenDry** `🔗 <#item-itemwhendry>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-jamgunchance:

**JamGunChance** `🔗 <#item-jamgunchance>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-keepondeplete:

**KeepOnDeplete** `🔗 <#item-keepondeplete>`_
   Type: ``Any``

   No description

   Item types: clothing, drainable

.. _item-knockbackonnodeath:

**KnockBackOnNoDeath** `🔗 <#item-knockbackonnodeath>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-knockdownmod:

**KnockdownMod** `🔗 <#item-knockdownmod>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-learnedrecipes:

**LearnedRecipes** `🔗 <#item-learnedrecipes>`_
   Type: ``Any``

   No description

   Item types: literature

.. _item-lightdistance:

**LightDistance** `🔗 <#item-lightdistance>`_
   Type: ``Any``

   No description

   Item types: drainable, weaponpart

.. _item-lightstrength:

**LightStrength** `🔗 <#item-lightstrength>`_
   Type: ``Any``

   No description

   Item types: drainable, weaponpart

.. _item-lipids:

**Lipids** `🔗 <#item-lipids>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-lowlightbonus:

**LowLightBonus** `🔗 <#item-lowlightbonus>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-lvlskilltrained:

**LvlSkillTrained** `🔗 <#item-lvlskilltrained>`_
   Type: ``integer``

   No description

   Default: ``-1``

   Item types: literature

.. _item-magazine_subject:

**magazine_subject** `🔗 <#item-magazine_subject>`_
   Type: ``Any``

   No description

   Item types: literature

.. _item-magazinetype:

**MagazineType** `🔗 <#item-magazinetype>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-makeuptype:

**MakeUpType** `🔗 <#item-makeuptype>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-manuallyremovespentrounds:

**ManuallyRemoveSpentRounds** `🔗 <#item-manuallyremovespentrounds>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-map:

**Map** `🔗 <#item-map>`_
   Type: ``Any``

   No description

   Item types: map

.. _item-maxammo:

**MaxAmmo** `🔗 <#item-maxammo>`_
   Type: ``Any``

   No description

   Item types: normal, weapon

.. _item-maxcapacity:

**MaxCapacity** `🔗 <#item-maxcapacity>`_
   Type: ``integer``

   No description

   Default: ``-1``

   Item types: normal

.. _item-maxchannel:

**MaxChannel** `🔗 <#item-maxchannel>`_
   Type: ``integer``

   No description

   Default: ``108000``

   Item types: radio

.. _item-maxdamage:

**MaxDamage** `🔗 <#item-maxdamage>`_
   Type: ``float``

   No description

   Default: ``1.5``

   Item types: weapon

.. _item-maxhitcount:

**MaxHitcount** `🔗 <#item-maxhitcount>`_
   Type: ``integer``

   No description

   Default: ``1000``

   Item types: weapon

.. _item-maxitemsize:

**MaxItemSize** `🔗 <#item-maxitemsize>`_
   Type: ``Any``

   No description

   Item types: container

.. _item-maxrange:

**MaxRange** `🔗 <#item-maxrange>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-maxrangemodifier:

**MaxRangeModifier** `🔗 <#item-maxrangemodifier>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-maxsightrange:

**MaxSightRange** `🔗 <#item-maxsightrange>`_
   Type: ``Any``

   No description

   Item types: weapon, weaponpart

.. _item-mechanicsitem:

**MechanicsItem** `🔗 <#item-mechanicsitem>`_
   Type: ``Any``

   No description

   Item types: drainable, normal

.. _item-mediacategory:

**MediaCategory** `🔗 <#item-mediacategory>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-medical:

**Medical** `🔗 <#item-medical>`_
   Type: ``Any``

   No description

   Item types: container, drainable, food, normal

.. _item-metalvalue:

**MetalValue** `🔗 <#item-metalvalue>`_
   Type: ``Any``

   No description

   Item types: alarmclock, alarmclockclothing, clothing, container, drainable, key, normal, weapon, weaponpart

.. _item-micrange:

**MicRange** `🔗 <#item-micrange>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-minangle:

**MinAngle** `🔗 <#item-minangle>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-minchannel:

**MinChannel** `🔗 <#item-minchannel>`_
   Type: ``integer``

   No description

   Default: ``88000``

   Item types: radio

.. _item-mindamage:

**MinDamage** `🔗 <#item-mindamage>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-minimumswingtime:

**MinimumSwingtime** `🔗 <#item-minimumswingtime>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-minrange:

**MinRange** `🔗 <#item-minrange>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-minsightrange:

**MinSightRange** `🔗 <#item-minsightrange>`_
   Type: ``Any``

   No description

   Item types: weapon, weaponpart

.. _item-minutestoburn:

**MinutesToBurn** `🔗 <#item-minutestoburn>`_
   Type: ``float``

   How many in-game minutes it takes to burn the food. This value must be higher than ``MinutesToCook``.

   Default: ``120.0``

   Item types: food

.. _item-minutestocook:

**MinutesToCook** `🔗 <#item-minutestocook>`_
   Type: ``float``

   How many in-game minutes it takes to cook the food. This value must be smaller than ``MinutesToBurn``.

   Default: ``60.0``

   Item types: food

.. _item-modelweaponpart:

**ModelWeaponPart** `🔗 <#item-modelweaponpart>`_
   Type: ``Any``

   No description

   Can be duplicated: ✓

   Item types: weapon

.. _item-mounton:

**MountOn** `🔗 <#item-mounton>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-multiplehitconditionaffected:

**MultipleHitConditionAffected** `🔗 <#item-multiplehitconditionaffected>`_
   Type: ``boolean``

   No description

   Default: ``True``

   Item types: weapon

.. _item-muzzleflashmodelkey:

**MuzzleFlashModelKey** `🔗 <#item-muzzleflashmodelkey>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-neckprotectionmodifier:

**NeckProtectionModifier** `🔗 <#item-neckprotectionmodifier>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: clothing

.. _item-needtobeclosedoncereload:

**needtobeclosedoncereload** `🔗 <#item-needtobeclosedoncereload>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-noiseduration:

**NoiseDuration** `🔗 <#item-noiseduration>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-noiserange:

**NoiseRange** `🔗 <#item-noiserange>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-notransmit:

**NoTransmit** `🔗 <#item-notransmit>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-npcsoundboost:

**NPCSoundBoost** `🔗 <#item-npcsoundboost>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-numberofpages:

**NumberOfPages** `🔗 <#item-numberofpages>`_
   Type: ``integer``

   No description

   Default: ``-1``

   Item types: literature

.. _item-numlevelstrained:

**NumLevelsTrained** `🔗 <#item-numlevelstrained>`_
   Type: ``integer``

   No description

   Default: ``1``

   Item types: literature

.. _item-onbreak:

**OnBreak** `🔗 <#item-onbreak>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-oncooked:

**OnCooked** `🔗 <#item-oncooked>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-oncreate:

**OnCreate** `🔗 <#item-oncreate>`_
   Type: ``Any``

   No description

   Item types: clothing, container, drainable, food, literature, moveable, normal, weapon

.. _item-oneat:

**OnEat** `🔗 <#item-oneat>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-openingrecipe:

**OpeningRecipe** `🔗 <#item-openingrecipe>`_
   Type: ``Any``

   No description

   Item types: food, normal

.. _item-opensound:

**OpenSound** `🔗 <#item-opensound>`_
   Type: ``Any``

   No description

   Item types: container

.. _item-originx:

**OriginX** `🔗 <#item-originx>`_
   Type: ``Any``

   No description

   Item types: key

.. _item-originy:

**OriginY** `🔗 <#item-originy>`_
   Type: ``Any``

   No description

   Item types: key

.. _item-originz:

**originZ** `🔗 <#item-originz>`_
   Type: ``Any``

   No description

   Item types: key

.. _item-otherhandrequire:

**OtherHandRequire** `🔗 <#item-otherhandrequire>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-otherhanduse:

**OtherHandUse** `🔗 <#item-otherhanduse>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-packaged:

**Packaged** `🔗 <#item-packaged>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-padlock:

**Padlock** `🔗 <#item-padlock>`_
   Type: ``Any``

   No description

   Item types: key

.. _item-pagetowrite:

**PageToWrite** `🔗 <#item-pagetowrite>`_
   Type: ``Any``

   No description

   Item types: literature

.. _item-painreduction:

**painReduction** `🔗 <#item-painreduction>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-parttype:

**PartType** `🔗 <#item-parttype>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-physicsobject:

**PhysicsObject** `🔗 <#item-physicsobject>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-piercingbullets:

**PiercingBullets** `🔗 <#item-piercingbullets>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-placedsprite:

**PlacedSprite** `🔗 <#item-placedsprite>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-placemultiplesound:

**PlaceMultipleSound** `🔗 <#item-placemultiplesound>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-placeonesound:

**PlaceOneSound** `🔗 <#item-placeonesound>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-poisonpower:

**PoisonPower** `🔗 <#item-poisonpower>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-pourtype:

**PourType** `🔗 <#item-pourtype>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-primaryanimmask:

**primaryAnimMask** `🔗 <#item-primaryanimmask>`_
   Type: ``Any``

   No description

   Item types: drainable, normal, weaponpart

.. _item-projectilecount:

**Projectilecount** `🔗 <#item-projectilecount>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-projectilespread:

**ProjectileSpread** `🔗 <#item-projectilespread>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-projectilespreadmodifier:

**ProjectileSpreadModifier** `🔗 <#item-projectilespreadmodifier>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-projectileweightcenter:

**ProjectileWeightCenter** `🔗 <#item-projectileweightcenter>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-protectfromrainwhenequipped:

**ProtectFromRainWhenEquipped** `🔗 <#item-protectfromrainwhenequipped>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-proteins:

**Proteins** `🔗 <#item-proteins>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-pushbackmod:

**PushBackMod** `🔗 <#item-pushbackmod>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-putinsound:

**PutInSound** `🔗 <#item-putinsound>`_
   Type: ``Any``

   No description

   Item types: container

.. _item-rackaftershoot:

**RackAfterShoot** `🔗 <#item-rackaftershoot>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-racksound:

**RackSound** `🔗 <#item-racksound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-rainfactor:

**RainFactor** `🔗 <#item-rainfactor>`_
   Type: ``Any``

   No description

   Item types: drainable, normal, weapon

.. _item-ranged:

**Ranged** `🔗 <#item-ranged>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-rangefalloff:

**RangeFalloff** `🔗 <#item-rangefalloff>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-readtype:

**ReadType** `🔗 <#item-readtype>`_
   Type: ``Any``

   No description

   Item types: literature

.. _item-recoildelay:

**RecoilDelay** `🔗 <#item-recoildelay>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-recoildelaymodifier:

**RecoilDelayModifier** `🔗 <#item-recoildelaymodifier>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-reduceinfectionpower:

**ReduceInfectionPower** `🔗 <#item-reduceinfectionpower>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-reloadtime:

**Reloadtime** `🔗 <#item-reloadtime>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-reloadtimemodifier:

**ReloadTimeModifier** `🔗 <#item-reloadtimemodifier>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-remotecontroller:

**RemoteController** `🔗 <#item-remotecontroller>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-remoterange:

**RemoteRange** `🔗 <#item-remoterange>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-removenegativeeffectoncooked:

**RemoveNegativeEffectOnCooked** `🔗 <#item-removenegativeeffectoncooked>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-removeonbroken:

**RemoveOnBroken** `🔗 <#item-removeonbroken>`_
   Type: ``boolean``

   No description

   Default: ``True``

   Item types: clothing

.. _item-removeunhappinesswhencooked:

**RemoveUnhappinessWhenCooked** `🔗 <#item-removeunhappinesswhencooked>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-replaceinprimaryhand:

**ReplaceInPrimaryHand** `🔗 <#item-replaceinprimaryhand>`_
   Type: ``Any``

   No description

   Item types: clothing, container, drainable, normal, radio

.. _item-replaceinsecondhand:

**ReplaceInSecondHand** `🔗 <#item-replaceinsecondhand>`_
   Type: ``Any``

   No description

   Item types: clothing, container, drainable, normal, radio

.. _item-replaceoncooked:

**ReplaceOnCooked** `🔗 <#item-replaceoncooked>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-replaceondeplete:

**ReplaceOnDeplete** `🔗 <#item-replaceondeplete>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-replaceonextinguish:

**ReplaceOnExtinguish** `🔗 <#item-replaceonextinguish>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-replaceonrotten:

**ReplaceOnRotten** `🔗 <#item-replaceonrotten>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-replaceonuse:

**ReplaceOnUse** `🔗 <#item-replaceonuse>`_
   Type: ``Any``

   No description

   Item types: food, normal

.. _item-requireinhandorinventory:

**RequireInHandOrInventory** `🔗 <#item-requireinhandorinventory>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-requiresequippedbothhands:

**RequiresEquippedBothHands** `🔗 <#item-requiresequippedbothhands>`_
   Type: ``Any``

   No description

   Item types: moveable, normal, weapon

.. _item-researchablerecipes:

**Researchablerecipes** `🔗 <#item-researchablerecipes>`_
   Type: ``array``

   No description

   Item types: clothing, container, drainable, food, moveable, normal, radio, weapon

.. _item-runanim:

**RunAnim** `🔗 <#item-runanim>`_
   Type: ``string``

   No description

   Default: ``Run``

   Item types: weapon

.. _item-runspeedmodifier:

**RunSpeedModifier** `🔗 <#item-runspeedmodifier>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: clothing, container, radio

.. _item-scaleworldicon:

**ScaleWorldIcon** `🔗 <#item-scaleworldicon>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: drainable

.. _item-scratchdefense:

**ScratchDefense** `🔗 <#item-scratchdefense>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-secondaryanimmask:

**secondaryAnimMask** `🔗 <#item-secondaryanimmask>`_
   Type: ``Any``

   No description

   Item types: drainable, normal, weaponpart

.. _item-sensorrange:

**SensorRange** `🔗 <#item-sensorrange>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-sharpness:

**Sharpness** `🔗 <#item-sharpness>`_
   Type: ``Any``

   No description

   Item types: normal, weapon

.. _item-shellfallsound:

**ShellFallSound** `🔗 <#item-shellfallsound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-shoutmultiplier:

**ShoutMultiplier** `🔗 <#item-shoutmultiplier>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: clothing, normal

.. _item-shouttype:

**ShoutType** `🔗 <#item-shouttype>`_
   Type: ``Any``

   No description

   Item types: clothing, normal

.. _item-skilltrained:

**SkillTrained** `🔗 <#item-skilltrained>`_
   Type: ``string``

   No description

   Item types: literature

.. _item-smokerange:

**SmokeRange** `🔗 <#item-smokerange>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-soundgain:

**SoundGain** `🔗 <#item-soundgain>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-soundmap:

**SoundMap** `🔗 <#item-soundmap>`_
   Type: ``Any``

   No description

   Can be duplicated: ✓

   Item types: drainable, food, weapon, weaponpart

.. _item-soundparameter:

**SoundParameter** `🔗 <#item-soundparameter>`_
   Type: ``Any``

   No description

   Item types: container

.. _item-soundradius:

**SoundRadius** `🔗 <#item-soundradius>`_
   Type: ``Any``

   No description

   Item types: alarmclock, alarmclockclothing, normal, weapon

.. _item-soundvolume:

**SoundVolume** `🔗 <#item-soundvolume>`_
   Type: ``Any``

   No description

   Item types: normal, weapon

.. _item-spawnwith:

**SpawnWith** `🔗 <#item-spawnwith>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-spice:

**Spice** `🔗 <#item-spice>`_
   Type: ``Any``

   No description

   Item types: drainable, food

.. _item-splatbloodonnodeath:

**SplatBloodOnNoDeath** `🔗 <#item-splatbloodonnodeath>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-splatnumber:

**SplatNumber** `🔗 <#item-splatnumber>`_
   Type: ``integer``

   No description

   Default: ``2``

   Item types: weapon

.. _item-splatsize:

**SplatSize** `🔗 <#item-splatsize>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-staticmodel:

**StaticModel** `🔗 <#item-staticmodel>`_
   Type: ``Any``

   No description

   Item types: clothing, container, drainable, food, literature, map, moveable, normal, radio, weaponpart

.. _item-staticmodelsbyindex:

**StaticModelsByIndex** `🔗 <#item-staticmodelsbyindex>`_
   Type: ``array``

   No description

   Item types: food, literature, normal

.. _item-stomppower:

**StompPower** `🔗 <#item-stomppower>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: clothing

.. _item-stoppower:

**StopPower** `🔗 <#item-stoppower>`_
   Type: ``float``

   No description

   Default: ``5.0``

   Item types: weapon

.. _item-stresschange:

**StressChange** `🔗 <#item-stresschange>`_
   Type: ``Any``

   No description

   Item types: drainable, food, literature

.. _item-subcategory:

**SubCategory** `🔗 <#item-subcategory>`_
   Type: ``string``

   No description

   Item types: weapon

.. _item-survivalgear:

**SurvivalGear** `🔗 <#item-survivalgear>`_
   Type: ``Any``

   No description

   Item types: container, drainable, food, map, normal, weapon

.. _item-suspensioncompression:

**suspensionCompression** `🔗 <#item-suspensioncompression>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-suspensiondamping:

**suspensionDamping** `🔗 <#item-suspensiondamping>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-swingamountbeforeimpact:

**SwingAmountBeforeImpact** `🔗 <#item-swingamountbeforeimpact>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-swinganim:

**SwingAnim** `🔗 <#item-swinganim>`_
   Type: ``string``

   No description

   Default: ``Rifle``

   Item types: weapon

.. _item-swingsound:

**SwingSound** `🔗 <#item-swingsound>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-swingtime:

**Swingtime** `🔗 <#item-swingtime>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-tags:

**Tags** `🔗 <#item-tags>`_
   Type: ``array``

   No description

   Item types: alarmclock, alarmclockclothing, clothing, container, drainable, food, key, literature, map, moveable, normal, radio, weapon, weaponpart

.. _item-thirstchange:

**ThirstChange** `🔗 <#item-thirstchange>`_
   Type: ``Any``

   No description

   Item types: food

.. _item-ticksperequipuse:

**ticksPerEquipUse** `🔗 <#item-ticksperequipuse>`_
   Type: ``integer``

   No description

   Default: ``30``

   Item types: drainable

.. _item-tohitmodifier:

**ToHitModifier** `🔗 <#item-tohitmodifier>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-tooltip:

**Tooltip** `🔗 <#item-tooltip>`_
   Type: ``Any``

   No description

   Item types: clothing, container, drainable, food, key, literature, moveable, normal, radio, weapon, weaponpart

.. _item-torchcone:

**TorchCone** `🔗 <#item-torchcone>`_
   Type: ``Any``

   No description

   Item types: drainable, weaponpart

.. _item-torchdot:

**TorchDot** `🔗 <#item-torchdot>`_
   Type: ``float``

   No description

   Default: ``0.96``

   Item types: drainable, weaponpart

.. _item-transmitrange:

**TransmitRange** `🔗 <#item-transmitrange>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-trap:

**Trap** `🔗 <#item-trap>`_
   Type: ``boolean``

   No description

   Default: ``False``

   Item types: normal

.. _item-treedamage:

**TreeDamage** `🔗 <#item-treedamage>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-triggerexplosiontimer:

**triggerExplosionTimer** `🔗 <#item-triggerexplosiontimer>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-twohandweapon:

**TwoHandWeapon** `🔗 <#item-twohandweapon>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-twoway:

**TwoWay** `🔗 <#item-twoway>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-type:

**Type** `🔗 <#item-type>`_
   Type: ``Any``

   Used to set the class of the item, which will influence parameters available.

   .. warning::

      **Deprecated** (since version 42.13.0)

      Use :ref:`itemtype` instead.

.. _item-unequipsound:

**UnequipSound** `🔗 <#item-unequipsound>`_
   Type: ``Any``

   No description

   Item types: drainable, normal, weapon

.. _item-unhappychange:

**UnhappyChange** `🔗 <#item-unhappychange>`_
   Type: ``Any``

   No description

   Item types: drainable, food, literature

.. _item-usedelta:

**UseDelta** `🔗 <#item-usedelta>`_
   Type: ``float``

   No description

   Default: ``0.03125``

   Item types: drainable, food, radio, weaponpart

.. _item-useendurance:

**UseEndurance** `🔗 <#item-useendurance>`_
   Type: ``boolean``

   No description

   Default: ``True``

   Item types: weapon

.. _item-usesbattery:

**UsesBattery** `🔗 <#item-usesbattery>`_
   Type: ``Any``

   No description

   Item types: radio

.. _item-useself:

**UseSelf** `🔗 <#item-useself>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-usewhileequipped:

**UseWhileEquipped** `🔗 <#item-usewhileequipped>`_
   Type: ``boolean``

   No description

   Default: ``True``

   Item types: drainable, food, normal, radio

.. _item-usewhileunequipped:

**UseWhileUnequipped** `🔗 <#item-usewhileunequipped>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-useworlditem:

**UseWorldItem** `🔗 <#item-useworlditem>`_
   Type: ``Any``

   No description

   Item types: drainable

.. _item-vehiclepartmodel:

**VehiclePartModel** `🔗 <#item-vehiclepartmodel>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-vehicletype:

**VehicleType** `🔗 <#item-vehicletype>`_
   Type: ``Any``

   No description

   Item types: drainable, normal

.. _item-visionmodifier:

**VisionModifier** `🔗 <#item-visionmodifier>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: clothing

.. _item-visualaid:

**VisualAid** `🔗 <#item-visualaid>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-waterresistance:

**WaterResistance** `🔗 <#item-waterresistance>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-weaponhitarmoursound:

**WeaponHitArmourSound** `🔗 <#item-weaponhitarmoursound>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-weaponlength:

**WeaponLength** `🔗 <#item-weaponlength>`_
   Type: ``float``

   No description

   Default: ``0.4``

   Item types: weapon

.. _item-weaponreloadtype:

**WeaponReloadType** `🔗 <#item-weaponreloadtype>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-weaponsprite:

**WeaponSprite** `🔗 <#item-weaponsprite>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-weaponspritesbyindex:

**WeaponSpritesByIndex** `🔗 <#item-weaponspritesbyindex>`_
   Type: ``Any``

   No description

   Item types: weapon

.. _item-weaponweight:

**WeaponWeight** `🔗 <#item-weaponweight>`_
   Type: ``float``

   No description

   Default: ``1.0``

   Item types: weapon

.. _item-weight:

**Weight** `🔗 <#item-weight>`_
   Type: ``float``

   No description

   Default: ``1.0``

.. _item-weightempty:

**WeightEmpty** `🔗 <#item-weightempty>`_
   Type: ``Any``

   No description

   Item types: drainable, food, normal

.. _item-weightmodifier:

**WeightModifier** `🔗 <#item-weightmodifier>`_
   Type: ``Any``

   No description

   Item types: weaponpart

.. _item-weightreduction:

**WeightReduction** `🔗 <#item-weightreduction>`_
   Type: ``Any``

   No description

   Item types: container

.. _item-wet:

**Wet** `🔗 <#item-wet>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-wetcooldown:

**WetCooldown** `🔗 <#item-wetcooldown>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-wheelfriction:

**wheelFriction** `🔗 <#item-wheelfriction>`_
   Type: ``Any``

   No description

   Item types: normal

.. _item-windresistance:

**WindResistance** `🔗 <#item-windresistance>`_
   Type: ``Any``

   No description

   Item types: clothing, normal

.. _item-withdrainable:

**WithDrainable** `🔗 <#item-withdrainable>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-withoutdrainable:

**WithoutDrainable** `🔗 <#item-withoutdrainable>`_
   Type: ``Any``

   No description

   Item types: clothing

.. _item-worldobjectsprite:

**WorldObjectSprite** `🔗 <#item-worldobjectsprite>`_
   Type: ``Any``

   No description

   Item types: moveable, normal, radio

.. _item-worldstaticmodel:

**WorldStaticModel** `🔗 <#item-worldstaticmodel>`_
   Type: ``Any``

   No description

.. _item-worldstaticmodelsbyindex:

**WorldStaticModelsByIndex** `🔗 <#item-worldstaticmodelsbyindex>`_
   Type: ``array``

   No description

   Item types: container, food, key, literature, normal, weapon

