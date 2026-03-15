.. _character_trait_definition:

character_trait_definition
==========================

Defines a character trait.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _isprofessiontrait:

**IsProfessionTrait**
   Type: ``boolean`` *(required)*

   Defines whenever the trait is a profession trait or not, meaning it will only be available when selecting a profession.

.. _disabledinmultiplayer:

**DisabledInMultiplayer**
   Type: ``boolean`` *(required)*

   If true, this trait will be disabled in multiplayer games.

.. _cost:

**Cost**
   Type: ``integer`` *(required)*

   The cost of the trait when selecting a character. Negative values give points, positive values take points.

.. _charactertrait:

**CharacterTrait**
   Type: ``string`` *(required)*

   The registries trait definition ID to link to. see the wiki page about `registries <https://pzwiki.net/wiki/Registries>`_ for more information.

.. _uiname:

**UIName**
   Type: ``string`` *(required)*

   The translation key for the trait's name. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.

.. _uidescription:

**UIDescription**
   Type: ``string`` *(required)*

   The translation key for the trait's description. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.

.. _mutuallyexclusivetraits:

**MutuallyExclusiveTraits**
   Type: ``array``

   A list of trait IDs that are mutually exclusive with this trait. If one is selected, the others cannot be selected.

.. _xpboosts:

**XPBoosts**
   Type: ``array``

   A list of experience boosts granted by this trait. Each entry should contain a skill name and the corresponding boost amount.
   
   For example:
   
   .. code-block:: cpp
   
      XPBoosts = Axe=1;Blunt=1,

.. _grantedrecipes:

**GrantedRecipes**
   Type: ``array``

   A list of `craftRecipe <https://pzwiki.net/wiki/CraftRecipe>`_ IDs that are granted to the character when this trait is selected.

