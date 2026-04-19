.. _vehicle:

vehicle
=======

Defines a vehicle.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`

**Possible Child Blocks:**

- :ref:`area`
- :ref:`attachment`
- :ref:`lightbar`
- :ref:`model`
- :ref:`part`
- :ref:`passenger`
- :ref:`physics`
- :ref:`skin`
- :ref:`sound`
- :ref:`wheel`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _vehicle-animaltrailersize:

**animalTrailerSize** `🔗 <#vehicle-animaltrailersize>`_
   Type: ``float``

   Sets the maximum total encumbrance from animals in the animal trailer. The horsebox and livestock trailers both use 500.

.. _vehicle-area:

**area** `🔗 <#vehicle-area>`_
   Type: ``Any``

   No description

.. _vehicle-attachment:

**attachment** `🔗 <#vehicle-attachment>`_
   Type: ``Any``

   No description

.. _vehicle-brakingforce:

**brakingForce** `🔗 <#vehicle-brakingforce>`_
   Type: ``Any``

   No description

.. _vehicle-carmechanicsoverlay:

**carMechanicsOverlay** `🔗 <#vehicle-carmechanicsoverlay>`_
   Type: ``string``

   No description

.. _vehicle-carmodelname:

**carModelName** `🔗 <#vehicle-carmodelname>`_
   Type: ``string``

   Set the `translation <https://pzwiki.net/wiki/Translation>`_ key for the car name. The translation entry needs to be stored inside the IG_UI translation file and have ``IGUI_VehicleName`` as a prefix. 
   
   For example:
   
   .. code-block:: cpp
   
      carModelName = YourCar,
   
   With the translation entry inside ``IG_UI.json``\ :
   
   .. code-block:: json
   
      {
        "IGUI_VehicleNameYourCar": "Your car model",
      }

.. _vehicle-centerofmassoffset:

**centerOfMassOffset** `🔗 <#vehicle-centerofmassoffset>`_
   Type: ``Any``

   No description

.. _vehicle-engineforce:

**engineForce** `🔗 <#vehicle-engineforce>`_
   Type: ``float``

   No description

   Default: ``3000``

.. _vehicle-engineidlespeed:

**engineIdleSpeed** `🔗 <#vehicle-engineidlespeed>`_
   Type: ``float``

   No description

   Default: ``750.0``

.. _vehicle-engineloudness:

**engineLoudness** `🔗 <#vehicle-engineloudness>`_
   Type: ``integer``

   No description

   Default: ``100``

.. _vehicle-enginequality:

**engineQuality** `🔗 <#vehicle-enginequality>`_
   Type: ``integer``

   No description

   Default: ``100``

.. _vehicle-enginerepairlevel:

**engineRepairLevel** `🔗 <#vehicle-enginerepairlevel>`_
   Type: ``integer``

   Required `mechanics skill <https://pzwiki.net/wiki/Mechanics>`_ level for repearing the vehicle's engine.

.. _vehicle-enginerpmtype:

**engineRPMType** `🔗 <#vehicle-enginerpmtype>`_
   Type: ``string``

   Sets the engine to a RPM type (\ `See vehicleEngineRPM block <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicleenginerpm.html>`_\ ).

   Default: ``jeep``

.. _vehicle-extents:

**extents** `🔗 <#vehicle-extents>`_
   Type: ``Any``

   No description

.. _vehicle-extentsoffset:

**extentsOffset** `🔗 <#vehicle-extentsoffset>`_
   Type: ``Any``

   No description

.. _vehicle-forcedcolor:

**forcedColor** `🔗 <#vehicle-forcedcolor>`_
   Type: ``array``

   Sets a forced HSV color on the vehicle. The value needs to be of format ``hue sat val``.

   Default: ``-1 -1 -1``

.. _vehicle-frontenddurability:

**frontEndDurability** `🔗 <#vehicle-frontenddurability>`_
   Type: ``integer``

   It is unclear what that parameter does but as of 42.16.3, the game uses ``frontEndHealth`` which is a mistake.

   Default: ``100``

.. _vehicle-frontendhealth:

**frontEndHealth** `🔗 <#vehicle-frontendhealth>`_
   Type: ``Any``

   No description

   .. warning::

      **Deprecated**

      Use :ref:`frontenddurability` instead.

      While that parameter is present in vanilla scripts as of 42.16.3, it actually does nothing because it is not parsed as ``frontEndHealth`` but as ``frontEndDurability``.

.. _vehicle-gearratio1:

**gearRatio1** `🔗 <#vehicle-gearratio1>`_
   Type: ``float``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

   Default: ``6.44``

.. _vehicle-gearratio2:

**gearRatio2** `🔗 <#vehicle-gearratio2>`_
   Type: ``Any``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

   Default: ``4.1``

.. _vehicle-gearratio3:

**gearRatio3** `🔗 <#vehicle-gearratio3>`_
   Type: ``Any``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

   Default: ``2.29``

.. _vehicle-gearratio4:

**gearRatio4** `🔗 <#vehicle-gearratio4>`_
   Type: ``Any``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

   Default: ``1.47``

.. _vehicle-gearratio5:

**gearRatio5** `🔗 <#vehicle-gearratio5>`_
   Type: ``Any``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

   Default: ``1.0``

.. _vehicle-gearratio6:

**gearRatio6** `🔗 <#vehicle-gearratio6>`_
   Type: ``Any``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

.. _vehicle-gearratio7:

**gearRatio7** `🔗 <#vehicle-gearratio7>`_
   Type: ``Any``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

.. _vehicle-gearratio8:

**gearRatio8** `🔗 <#vehicle-gearratio8>`_
   Type: ``Any``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

.. _vehicle-gearratiocount:

**gearRatioCount** `🔗 <#vehicle-gearratiocount>`_
   Type: ``integer``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

   Default: ``4``

.. _vehicle-gearratior:

**gearRatioR** `🔗 <#vehicle-gearratior>`_
   Type: ``float``

   `gearRatioCount <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 
   
   A maximum of 9 ratios can be set with the parameters:
   
   
   * `gearRatioR <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
   * `gearRatio1 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio1>`_
   * `gearRatio2 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio2>`_
   * `gearRatio3 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio3>`_
   * `gearRatio4 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio4>`_
   * `gearRatio5 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio5>`_
   * `gearRatio6 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio6>`_
   * `gearRatio7 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio7>`_
   * `gearRatio8 <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-gearratio8>`_
   
   Those ratios take floats

   Default: ``7.09``

.. _vehicle-haslighter:

**hasLighter** `🔗 <#vehicle-haslighter>`_
   Type: ``boolean``

   Sets whenever this car has a lighter to light a cigarette.

   Default: ``True``

.. _vehicle-hassiren:

**hasSiren** `🔗 <#vehicle-hassiren>`_
   Type: ``boolean``

   No description

.. _vehicle-issmallvehicle:

**isSmallVehicle** `🔗 <#vehicle-issmallvehicle>`_
   Type: ``boolean``

   No description

   Default: ``True``

.. _vehicle-lightbar:

**lightbar** `🔗 <#vehicle-lightbar>`_
   Type: ``Any``

   No description

.. _vehicle-mass:

**mass** `🔗 <#vehicle-mass>`_
   Type: ``float``

   Sets the mass of the vehicle which will notably be used for various physic calculations. 
   
   By default is equal to 800. As a reference, a car has a mass of around 800, pickup trucks have around 1100, a simple trailer around 200, a burnt vehicle 400 or 500. See the game scripts for more examples.

   Default: ``800``

.. _vehicle-maxspeed:

**maxSpeed** `🔗 <#vehicle-maxspeed>`_
   Type: ``float``

   No description

   Default: ``20.0``

.. _vehicle-maxspeedreverse:

**maxSpeedReverse** `🔗 <#vehicle-maxspeedreverse>`_
   Type: ``float``

   No description

   Default: ``40.0``

.. _vehicle-maxsuspensiontravelcm:

**maxSuspensionTravelCm** `🔗 <#vehicle-maxsuspensiontravelcm>`_
   Type: ``float``

   No description

   Default: ``500.0``

.. _vehicle-mechanictype:

**mechanicType** `🔗 <#vehicle-mechanictype>`_
   Type: ``integer``

   Defines what class the vehicle is, that is 1 for standard, 2 for heavy-duty and 3 for performance.

   Allowed values:

   - ``1``
   - ``2``
   - ``3``

.. _vehicle-model:

**model** `🔗 <#vehicle-model>`_
   Type: ``Any``

   No description

.. _vehicle-neverspawnkey:

**neverSpawnKey** `🔗 <#vehicle-neverspawnkey>`_
   Type: ``boolean``

   Sets whenever this vehicle will never have a key spawning in buildings or on zombies spawning around the vehicle.

.. _vehicle-notkillcrops:

**notKillCrops** `🔗 <#vehicle-notkillcrops>`_
   Type: ``boolean``

   Sets whenever the vehicle will destroy crops it is driving on.

.. _vehicle-offroadefficiency:

**offRoadEfficiency** `🔗 <#vehicle-offroadefficiency>`_
   Type: ``float``

   No description

   Default: ``1.0``

.. _vehicle-part:

**part** `🔗 <#vehicle-part>`_
   Type: ``Any``

   No description

.. _vehicle-passenger:

**passenger** `🔗 <#vehicle-passenger>`_
   Type: ``Any``

   No description

.. _vehicle-physics:

**physics** `🔗 <#vehicle-physics>`_
   Type: ``Any``

   No description

.. _vehicle-physicschassisshape:

**physicsChassisShape** `🔗 <#vehicle-physicschassisshape>`_
   Type: ``array``

   Defines the hitbox of the vehicle. The value should be three numbers defining the dimensions of a box:
   
   .. code-block::
   
      physicsChassisShape = height width length,
   
   For example:
   
   .. code-block::
   
      physicsChassisShape = height width length,
   
   When setting `useChassisPhysicsCollision <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-usechassisphysicscollision>`_ to ``false``\ , it will instead use `physics <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/physics.html>`_ for the hitbox of the vehicle.

.. _vehicle-playerdamageprotection:

**playerDamageProtection** `🔗 <#vehicle-playerdamageprotection>`_
   Type: ``float``

   Multiplier applied to the amount of damage the player takes when crashing in the car. A value of 1 doesn't change the damage, but a lower value reduces it and a higher value increases it.

.. _vehicle-rearenddurability:

**rearEndDurability** `🔗 <#vehicle-rearenddurability>`_
   Type: ``integer``

   It is unclear what that parameter does but as of 42.16.3, the game uses ``rearEndHealth`` which is a mistake.

   Default: ``100``

.. _vehicle-rearendhealth:

**rearEndHealth** `🔗 <#vehicle-rearendhealth>`_
   Type: ``Any``

   No description

   .. warning::

      **Deprecated**

      Use :ref:`rearenddurability` instead.

      While that parameter is present in vanilla scripts as of 42.16.3, it actually does nothing because it is not parsed as ``rearEndHealth`` but as ``rearEndDurability``.

.. _vehicle-rollinfluence:

**rollInfluence** `🔗 <#vehicle-rollinfluence>`_
   Type: ``float``

   No description

   Default: ``0.1``

.. _vehicle-seatnumber:

**seatNumber** `🔗 <#vehicle-seatnumber>`_
   Type: ``Any``

   No description

.. _vehicle-seats:

**seats** `🔗 <#vehicle-seats>`_
   Type: ``integer``

   Sets the number of seats this vehicle can have. A seat `part <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/part.html>`_ needs to be created which will hold a `container <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/container.html#container>`_ block with a parameter `seat <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/container.html#container-seat>`_

   Default: ``2``

.. _vehicle-shadowextents:

**shadowExtents** `🔗 <#vehicle-shadowextents>`_
   Type: ``Any``

   No description

.. _vehicle-shadowoffset:

**shadowOffset** `🔗 <#vehicle-shadowoffset>`_
   Type: ``Any``

   No description

.. _vehicle-skin:

**skin** `🔗 <#vehicle-skin>`_
   Type: ``Any``

   No description

.. _vehicle-sound:

**sound** `🔗 <#vehicle-sound>`_
   Type: ``Any``

   No description

.. _vehicle-spawnoffsety:

**spawnOffsetY** `🔗 <#vehicle-spawnoffsety>`_
   Type: ``Any``

   No description

.. _vehicle-specialkeyring:

**specialKeyRing** `🔗 <#vehicle-specialkeyring>`_
   Type: ``array``

   ``specialKeyRing`` needs to reference a keyring item to spawn. ``specialKeyRingChance`` is used to set the chance to spawn this keyring.

.. _vehicle-specialkeyringchance:

**specialKeyRingChance** `🔗 <#vehicle-specialkeyringchance>`_
   Type: ``integer``

   ``specialKeyRing`` needs to reference a keyring item to spawn. ``specialKeyRingChance`` is used to set the chance to spawn this keyring.

.. _vehicle-speciallootchance:

**specialLootChance** `🔗 <#vehicle-speciallootchance>`_
   Type: ``integer``

   No description

   Default: ``8``

.. _vehicle-steeringclamp:

**steeringClamp** `🔗 <#vehicle-steeringclamp>`_
   Type: ``float``

   No description

   Default: ``0.4``

.. _vehicle-steeringincrement:

**steeringIncrement** `🔗 <#vehicle-steeringincrement>`_
   Type: ``float``

   No description

   Default: ``0.04``

.. _vehicle-stoppingmovementforce:

**stoppingMovementForce** `🔗 <#vehicle-stoppingmovementforce>`_
   Type: ``float``

   No description

   Default: ``1.0``

.. _vehicle-storagecapacity:

**storageCapacity** `🔗 <#vehicle-storagecapacity>`_
   Type: ``integer``

   No description

   Default: ``100``

.. _vehicle-suspensioncompression:

**suspensionCompression** `🔗 <#vehicle-suspensioncompression>`_
   Type: ``float``

   No description

   Default: ``4.4``

.. _vehicle-suspensiondamping:

**suspensionDamping** `🔗 <#vehicle-suspensiondamping>`_
   Type: ``float``

   No description

   Default: ``2.3``

.. _vehicle-suspensionrestlength:

**suspensionRestLength** `🔗 <#vehicle-suspensionrestlength>`_
   Type: ``float``

   No description

   Default: ``0.6``

.. _vehicle-suspensionstiffness:

**suspensionStiffness** `🔗 <#vehicle-suspensionstiffness>`_
   Type: ``float``

   No description

   Default: ``20.0``

.. _vehicle-template:

**template** `🔗 <#vehicle-template>`_
   Type: ``Any``

   Uses a template script data for this vehicle.

   Can be duplicated: ✓

.. _vehicle-template!:

**template!** `🔗 <#vehicle-template!>`_
   Type: ``Any``

   No description

   Can be duplicated: ✓

.. _vehicle-texturedamage1overlay:

**textureDamage1Overlay** `🔗 <#vehicle-texturedamage1overlay>`_
   Type: ``string``

   No description

.. _vehicle-texturedamage1shell:

**textureDamage1Shell** `🔗 <#vehicle-texturedamage1shell>`_
   Type: ``string``

   No description

.. _vehicle-texturedamage2overlay:

**textureDamage2Overlay** `🔗 <#vehicle-texturedamage2overlay>`_
   Type: ``string``

   No description

.. _vehicle-texturedamage2shell:

**textureDamage2Shell** `🔗 <#vehicle-texturedamage2shell>`_
   Type: ``string``

   No description

.. _vehicle-texturelights:

**textureLights** `🔗 <#vehicle-texturelights>`_
   Type: ``string``

   No description

.. _vehicle-texturemask:

**textureMask** `🔗 <#vehicle-texturemask>`_
   Type: ``string``

   No description

.. _vehicle-texturemaskenable:

**textureMaskEnable** `🔗 <#vehicle-texturemaskenable>`_
   Type: ``boolean``

   No description

.. _vehicle-texturerust:

**textureRust** `🔗 <#vehicle-texturerust>`_
   Type: ``string``

   No description

.. _vehicle-textureshadow:

**textureShadow** `🔗 <#vehicle-textureshadow>`_
   Type: ``string``

   No description

.. _vehicle-usechassisphysicscollision:

**useChassisPhysicsCollision** `🔗 <#vehicle-usechassisphysicscollision>`_
   Type: ``boolean``

   By default ``true`` which makes the vehicle use the `physicsChassisShape <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/vehicle.html#vehicle-physicschassisshape>`_ for its hitbox. If set to false, it will instead use the `physics <https://sirdoggyjvla.github.io/pz-scripts-data/blocks/physics.html>`_ blocks as the hitbox of the vehicle.

   Default: ``True``

.. _vehicle-wheel:

**wheel** `🔗 <#vehicle-wheel>`_
   Type: ``Any``

   No description

.. _vehicle-wheelfriction:

**wheelFriction** `🔗 <#vehicle-wheelfriction>`_
   Type: ``float``

   No description

   Default: ``800.0``

.. _vehicle-zombietype:

**zombieType** `🔗 <#vehicle-zombietype>`_
   Type: ``array``

   Used to chose what zombie may spawn around the vehicle and is likely to have the key of the vehicle.

