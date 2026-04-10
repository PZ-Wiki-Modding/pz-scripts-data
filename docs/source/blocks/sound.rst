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

.. _sound-alarm:

**alarm** `🔗 <#sound-alarm>`_
   Type: ``array``

   No description

.. _sound-alarmloop:

**alarmLoop** `🔗 <#sound-alarmloop>`_
   Type: ``Any``

   No description

.. _sound-backsignal:

**backSignal** `🔗 <#sound-backsignal>`_
   Type: ``string``

   No description

.. _sound-category:

**category** `🔗 <#sound-category>`_
   Type: ``string``

   No description

.. _sound-engine:

**engine** `🔗 <#sound-engine>`_
   Type: ``string``

   No description

.. _sound-enginestart:

**engineStart** `🔗 <#sound-enginestart>`_
   Type: ``string``

   No description

.. _sound-engineturnoff:

**engineTurnOff** `🔗 <#sound-engineturnoff>`_
   Type: ``string``

   No description

.. _sound-handbrake:

**handBrake** `🔗 <#sound-handbrake>`_
   Type: ``string``

   No description

.. _sound-horn:

**horn** `🔗 <#sound-horn>`_
   Type: ``string``

   No description

.. _sound-ignitionfail:

**ignitionFail** `🔗 <#sound-ignitionfail>`_
   Type: ``Any``

   No description

.. _sound-ignitionfailnopower:

**ignitionFailNoPower** `🔗 <#sound-ignitionfailnopower>`_
   Type: ``string``

   No description

.. _sound-is3d:

**is3D** `🔗 <#sound-is3d>`_
   Type: ``string``

   This parameter looks unused.

.. _sound-loop:

**loop** `🔗 <#sound-loop>`_
   Type: ``boolean``

   Whether the sound should loop or not. The sound plays until turned off or the emitter is destroyed.

.. _sound-master:

**master** `🔗 <#sound-master>`_
   Type: ``string``

   Links the sound to a master sound category, which controls the volume of all sounds linked to it.

   Allowed values:

   - ``Primary``
   - ``Ambient``
   - ``Music``
   - ``VehicleEngine``

.. _sound-maxinstancesperemitter:

**maxInstancesPerEmitter** `🔗 <#sound-maxinstancesperemitter>`_
   Type: ``integer``

   No description

