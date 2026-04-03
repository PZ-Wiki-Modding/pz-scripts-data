.. _component_fluidcontainer:

component FluidContainer
========================

Adds a fluid container to an item


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`item`
- :ref:`entity`

**Possible Child Blocks:**

- :ref:`fluids`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _capacity:

**Capacity**
   Type: ``float``

   The fluid capacity of the container, the minimum value is ``0.05``.

   Default: ``1.0``

.. _containername:

**ContainerName**
   Type: ``string``

   The name of the fluid container, seems to be unused. The name cannot have whitespaces, the game will sanitize it to remove them and show an error in the console about it.

   Default: ``FluidContainer``

.. _customdrinksound:

**CustomDrinkSound**
   Type: ``string``

   Refers to a `sound block <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/sound.html>`_ to trigger when drinking.

   Default: ``DrinkingFromGeneric``

.. _hiddenamount:

**HiddenAmount**
   Type: ``boolean``

   When true, will hide the fluid quantity from the UI.

   Default: ``False``

.. _initialpercent:

**InitialPercent**
   Type: ``float``

   No description

.. _initialpercentmax:

**InitialPercentMax**
   Type: ``float``

   The minimum amount of fluid which will appear in this container.

   Default: ``1.0``

.. _initialpercentmin:

**InitialPercentMin**
   Type: ``float``

   The maximum amount of fluid which will appear in this container.

   Default: ``0.0``

.. _inputlocked:

**InputLocked**
   Type: ``boolean``

   Unused.

   Default: ``False``

.. _opened:

**Opened**
   Type: ``boolean``

   Unused.

   Default: ``True``

.. _pickrandomfluid:

**PickRandomFluid**
   Type: ``boolean``

   When set to true, the container will pick one of the available fluids in the `Fluids <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/fluids.html>`_ child block at random when filling. If set to false, it will make every fluids appear.

   Default: ``False``

.. _rainfactor:

**RainFactor**
   Type: ``float``

   Defines how much rain contributes to filling the container. A high value increases the rate of filling. A value of ``0.0`` means that rain will not fill the container, which is the default value of the parameter.
   
   If the item is a weapon and ``RainFactor`` is set to a value above the default, when the player aims with the weapon it will empty it.

   Default: ``0.0``

.. _fillswithcleanwater:

**FillsWithCleanWater**
   Type: ``boolean``

   When set to true, the container will fill with clean water instead of tainted water when left outside in the rain.

   Default: ``False``

