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


What is stored in ``/pb_policies``?
===================================

PodBrowser creates a new root Container ``/pb_policies`` within Pods stored on an 
`Enterprise Solid Server`_ (e.g., `https://pod.inrupt.com`_) that uses `Access Control Policies`_. 
The ``/pb_policies`` Container stores the policies (i.e., permissions) for the Resources within the Pod.

.. _Enterprise Solid Server: https://docs.inrupt.com/ess/about/
.. _https://pod.inrupt.com: https://signup.pod.inrupt.com
.. _Access Control Policies: https://github.com/solid/authorization-panel/tree/master/proposals/acp

.. warning:: Do not delete or edit any of the Resources stored in the ``/pb_policies`` Container 
  as this could affect permissions to Resources within the Pod.
