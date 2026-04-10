.. _option:

option
======

Defines a custom sandbox option for a mod.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`root-sandboxoptions`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _option_default:

**default**
   Type: ``Any``

   No description

.. _option_max:

**max**
   Type: ``float``

   The maximum value the option can have. Only for integer and double types.

.. _option_min:

**min**
   Type: ``float``

   The minimum value the option can have. Only for integer and double types.

.. _option_page:

**page**
   Type: ``string``

   The sandbox option to add the option to. Can be a custom page.

.. _option_translation:

**translation**
   Type: ``string``

   The translation key for the option's name.

.. _option_type:

**type**
   Type: ``string`` *(required)*

   The type of the option.

   Allowed values:

   - ``boolean``
   - ``integer``
   - ``double``
   - ``string``
   - ``enum``

