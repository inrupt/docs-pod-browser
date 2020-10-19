===
FAQ
===

Why don't I have access to browse my Pod?
=========================================

To manage your Pod, PodBrowser must be added as 
a trusted application with ``Read``, ``Write``, ``Append``, and ``Control``
access. 

To adjust PodBrowser's access:

#. In a web browser, enter the root URL to you Pod (e.g., https://docs-example.inrupt.net). 

#. The `Solid Data Browser`_ should be opened.

#. Click the :guilabel:`Log In` button to log into your Pod.

#. Go to the :guilabel:`Preferences` tab.

#. In the :guilabel:`Manage your trusted applications` section:

   * If PodBrowser is not listed as a trusted application:
  
     #. At the bottom of the table enter:

        .. list-table::

           * - Application URL

             - Access modes

           * - ``https://podbrowser.inrupt.com``

             - ``Read``, ``Write``, ``Append``, and ``Control``


      #. Click :guilabel:`Add`.

    * If PodBrowser is listed as a trusted application but with the wrong access, select all of the access modes and click :guilabel:`Update`.

.. _`Solid Data Browser`: https://github.com/solid/userguide#data-browser-user-guide


How do I navigate to another Pod?
=================================

To browse another Pod (or even a different Container in your own Pod), you can navigate there 
directly by entering the Pod (or Container) URI.

#. In PodBrowser, click the current :guilabel:`Pod` identifier link (just below the application logo).

#. In the displayed :guilabel:`Go to Pod` panel, enter the URI for the Pod (or Container).

#. Click :guilabel:`Enter`.

#. The navigation panel is refreshed and shows the Resources in the Pod (or Container).
