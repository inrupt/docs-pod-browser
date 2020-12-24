===
FAQ
===

.. _faq-grant-access-manually:

Why don't I have access to browse my Pod?
=========================================

To manage your Pod hosted by ``https://inrupt.net``, PodBrowser
must be added as a trusted application with ``Read``, ``Write``,
``Append``, and ``Control`` access.

To adjust PodBrowser's access:

#. In a web browser, enter the root URL to you Pod (e.g., https://docs-example.inrupt.net). 

#. The `Solid Data Browser`_ should be opened.

#. Click the :guilabel:`Log In` button to log into your Pod.

#. Go to the :guilabel:`Preferences` tab.

#. In the :guilabel:`Manage your trusted applications` section:

  * If PodBrowser is not listed as a trusted application:
  
    #. At the bottom of the table enter:

        .. list-table::
          :header-rows: 1

          * - Application URL

            - Access modes

          * - ``https://podbrowser.inrupt.com``

            - ``Read``, ``Write``, ``Append``, and ``Control``
    
    #. Click :guilabel:`Add`.

  * If PodBrowser is listed as a trusted application but with the
      wrong access, select all of the access modes and click
      :guilabel:`Update`.

.. _`Solid Data Browser`: https://github.com/solid/userguide#data-browser-user-guide


How do I navigate to another Pod?
=================================

To browse another Pod (or even a different Container in your own Pod), you can navigate there 
directly by entering the Pod (or Container) URI.

#. In PodBrowser, click the current :guilabel:`Pod` identifier link (just below the Account menu).

#. Select :guilabel:`Change Pod` in the menu.

#. In the displayed panel, enter the URI for the Pod (or Container).

#. Press :guilabel:`Enter`, or click the :guilabel:`Go` button.

#. The navigation panel is refreshed and shows the Resources in the entered Pod (or Container).

What do the Resource permissions mean?
======================================

PodBrowser allows you to share Containers and Resources within your
Pod with other Solid users. But what do the available permissions allow the other Solid users to do? 
The table below describes the permissions which can be conbined together:

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
      
.. note:: To allow other Solid users to display the Resource details in PodBrowser, 
  and hence access the Download and Delete options, they must have Read access to the Resource.


What is stored in ``/pb_policies``?
===================================

When you access a Pod stored on an `Enterprise Solid Server`_ (e.g., https://pod.inrupt.com) using PodBrowser, 
a new root Container ``/pb_policies`` is created to store `Access Control Policies`_, or 
permissions, for Resources within the Pod.

.. _Enterprise Solid Server: https://docs.inrupt.com/ess/about/
.. _Access Control Policies: https://github.com/solid/authorization-panel/tree/master/proposals/acp

.. warning:: Do not delete or edit any of the Resources stored in the ``/pb_policies`` Container 
  as this could affect permissions to Resources within the Pod.
