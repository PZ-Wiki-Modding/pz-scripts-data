.. _sound:

sound
=====

Makes one or more sound clips available for use in the game. Multiple clips can be added to a sound script, and the game will randomly select one of them to play when the sound is triggered.

.. code-block:: cpp

   module yourModule {
     sound yourSound {
       category = Animal,
       loop = true,
       is3D = true,
       clip {
         file = media/sound/RideOfTheValkyries.ogg,
         distanceMin = 20,
         distanceMax = 650,
         reverbFactor = 0.1,
         volume = 0.7,
       }
     }
   }


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`
- :ref:`vehicle`
- :ref:`template`

**Possible Child Blocks:**

- :ref:`clip`


ID Properties
-------------

This block should have an ID.

**Incompatible Parents:**

- vehicle
- template


Parameters
----------

.. _sound_alarm:

**alarm**
   Type: ``array``

   No description

.. _sound_alarmloop:

**alarmLoop**
   Type: ``Any``

   No description

.. _sound_backsignal:

**backSignal**
   Type: ``string``

   No description

.. _sound_category:

**category**
   Type: ``string``

   No description

.. _sound_engine:

**engine**
   Type: ``string``

   No description

.. _sound_enginestart:

**engineStart**
   Type: ``string``

   No description

.. _sound_engineturnoff:

**engineTurnOff**
   Type: ``string``

   No description

.. _sound_handbrake:

**handBrake**
   Type: ``string``

   No description

.. _sound_horn:

**horn**
   Type: ``string``

   No description

.. _sound_ignitionfail:

**ignitionFail**
   Type: ``Any``

   No description

.. _sound_ignitionfailnopower:

**ignitionFailNoPower**
   Type: ``string``

   No description

.. _sound_is3d:

**is3D**
   Type: ``string``

   This parameter looks unused.

.. _sound_loop:

**loop**
   Type: ``boolean``

   Whether the sound should loop or not. The sound plays until turned off or the emitter is destroyed.

.. _sound_master:

**master**
   Type: ``string``

   Links the sound to a master sound category, which controls the volume of all sounds linked to it.

   Allowed values:

   - ``Primary``
   - ``Ambient``
   - ``Music``
   - ``VehicleEngine``

.. _sound_maxinstancesperemitter:

**maxInstancesPerEmitter**
   Type: ``integer``

   No description

