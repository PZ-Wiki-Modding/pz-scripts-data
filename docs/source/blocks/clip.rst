.. _clip:

clip
====

Defines a clip to be used in a `sound script <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/sound.html>`_\ , which is a single sound file with properties that determine how it is played in the game.

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

- :ref:`sound`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _clip_distancemax:

**distanceMax**
   Type: ``integer``

   No description

.. _clip_distancemin:

**distanceMin**
   Type: ``integer``

   No description

.. _clip_event:

**event**
   Type: ``string``

   No description

.. _clip_file:

**file**
   Type: ``string``

   No description

.. _clip_pitch:

**pitch**
   Type: ``float``

   No description

.. _clip_reverbfactor:

**reverbFactor**
   Type: ``float``

   No description

.. _clip_reverbmaxrange:

**reverbMaxRange**
   Type: ``float``

   No description

.. _clip_stopimmediate:

**stopImmediate**
   Type: ``Any``

   No description

.. _clip_volume:

**volume**
   Type: ``float``

   No description

