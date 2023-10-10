===
FAQ
===

How do I navigate to another Pod?
=================================

To browse another Pod (or even a different Container in your own Pod), you can navigate there 
directly by entering the Pod (or Container) URI.

#. In PodBrowser, click the :guilabel:`Your Pod` dropdown on the top right-hand side.

#. Select :guilabel:`Change Pod` in the menu.

#. In the displayed panel, enter the URI for the Pod (or Container).

#. Press :guilabel:`Enter`, or click the :guilabel:`Go` button.

#. The navigation panel is refreshed and shows the Resources in the entered Pod (or Container).

What do the Resource permissions mean?
======================================

You can share your Pod's Containers and Resources with other Solid users. 
To share, you grant to the other users specific permission(s) for the Containers and Resources. 
The following table describes the permissions; these permissions can be combined:

.. list-table::
  :header-rows: 1
  :widths: 20 80

  * - Permission

    - Other Solid user can...

  * - View

    - View the Resources within a Container, or download a Resource.

  * - Edit

    - Change the contents of or delete a Resource.

  * - Append

    - Add to a Resource, but not change the existing contents.

  * - Control

    - Change the permissions for a Resource.
      
.. note:: To allow other Solid users to display the Resource details 
    (including the Download and Delete options) in PodBrowser, the 
    users must have View access to the Resource.


