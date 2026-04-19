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

.. _clip-distancemax:

**distanceMax** `🔗 <#clip-distancemax>`_
   Type: ``{'main': 'integer'}``

   No description

.. _clip-distancemin:

**distanceMin** `🔗 <#clip-distancemin>`_
   Type: ``{'main': 'integer'}``

   No description

.. _clip-event:

**event** `🔗 <#clip-event>`_
   Type: ``{'main': 'string'}``

   No description

.. _clip-file:

**file** `🔗 <#clip-file>`_
   Type: ``{'main': 'string'}``

   No description

.. _clip-pitch:

**pitch** `🔗 <#clip-pitch>`_
   Type: ``{'main': 'float'}``

   No description

.. _clip-reverbfactor:

**reverbFactor** `🔗 <#clip-reverbfactor>`_
   Type: ``{'main': 'float'}``

   No description

.. _clip-reverbmaxrange:

**reverbMaxRange** `🔗 <#clip-reverbmaxrange>`_
   Type: ``{'main': 'float'}``

   No description

.. _clip-stopimmediate:

**stopImmediate** `🔗 <#clip-stopimmediate>`_
   Type: ``Any``

   No description

.. _clip-volume:

**volume** `🔗 <#clip-volume>`_
   Type: ``{'main': 'float'}``

   No description

