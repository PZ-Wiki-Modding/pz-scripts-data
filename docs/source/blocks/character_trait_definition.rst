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

.. _character_trait_definition-charactertrait:

**CharacterTrait** `🔗 <#character_trait_definition-charactertrait>`_
   Type: ``string`` *(required)*

   The registries trait definition ID to link to. see the wiki page about `registries <https://pzwiki.net/wiki/Registries>`_ for more information.

.. _character_trait_definition-cost:

**Cost** `🔗 <#character_trait_definition-cost>`_
   Type: ``integer`` *(required)*

   The cost of the trait when selecting a character. Negative values give points, positive values take points.

.. _character_trait_definition-disabledinmultiplayer:

**DisabledInMultiplayer** `🔗 <#character_trait_definition-disabledinmultiplayer>`_
   Type: ``boolean`` *(required)*

   If true, this trait will be disabled in multiplayer games.

.. _character_trait_definition-grantedrecipes:

**GrantedRecipes** `🔗 <#character_trait_definition-grantedrecipes>`_
   Type: ``array``

   A list of `craftRecipe <https://pzwiki.net/wiki/CraftRecipe>`_ IDs that are granted to the character when this trait is selected.

.. _character_trait_definition-isprofessiontrait:

**IsProfessionTrait** `🔗 <#character_trait_definition-isprofessiontrait>`_
   Type: ``boolean`` *(required)*

   Defines whenever the trait is a profession trait or not, meaning it will only be available when selecting a profession.

.. _character_trait_definition-mutuallyexclusivetraits:

**MutuallyExclusiveTraits** `🔗 <#character_trait_definition-mutuallyexclusivetraits>`_
   Type: ``array``

   A list of trait IDs that are mutually exclusive with this trait. If one is selected, the others cannot be selected.

.. _character_trait_definition-uidescription:

**UIDescription** `🔗 <#character_trait_definition-uidescription>`_
   Type: ``string`` *(required)*

   The translation key for the trait's description. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.

.. _character_trait_definition-uiname:

**UIName** `🔗 <#character_trait_definition-uiname>`_
   Type: ``string`` *(required)*

   The translation key for the trait's name. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.

.. _character_trait_definition-xpboosts:

**XPBoosts** `🔗 <#character_trait_definition-xpboosts>`_
   Type: ``array``

   A list of experience boosts granted by this trait. Each entry should contain a skill name and the corresponding boost amount.
   
   For example:
   
   .. code-block:: cpp
   
      XPBoosts = Axe=1;Blunt=1,

