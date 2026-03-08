character_trait_definition
==========================

Defines a character trait.


Hierarchy
---------

**Valid Parent Blocks:**

- :doc:`module`


Parameters
----------

**IsProfessionTrait**
   Type: ``boolean`` *(required)*

   Defines whenever the trait is a profession trait or not, meaning it will only be available when selecting a profession.

**DisabledInMultiplayer**
   Type: ``boolean`` *(required)*

   If true, this trait will be disabled in multiplayer games.

**Cost**
   Type: ``integer`` *(required)*

   The cost of the trait when selecting a character. Negative values give points, positive values take points.

**CharacterTrait**
   Type: ``string`` *(required)*

   The registries trait definition ID to link to. see the wiki page about [registries](https://pzwiki.net/wiki/Registries) for more information.

**UIName**
   Type: ``string`` *(required)*

   The translation key for the trait's name. The translation key needs to be in the UI translation file. See the wiki page about [translations](https://pzwiki.net/wiki/Translations) for more information.

**UIDescription**
   Type: ``string`` *(required)*

   The translation key for the trait's description. The translation key needs to be in the UI translation file. See the wiki page about [translations](https://pzwiki.net/wiki/Translations) for more information.

**MutuallyExclusiveTraits**
   Type: ``array``

   A list of trait IDs that are mutually exclusive with this trait. If one is selected, the others cannot be selected.

**XPBoosts**
   Type: ``array``

   A list of experience boosts granted by this trait. Each entry should contain a skill name and the corresponding boost amount.

For example:
```cpp
XPBoosts = Axe=1;Blunt=1,
```

**GrantedRecipes**
   Type: ``array``

   A list of [craftRecipe](https://pzwiki.net/wiki/CraftRecipe) IDs that are granted to the character when this trait is selected.

