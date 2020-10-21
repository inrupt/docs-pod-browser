=================
Inrupt PodBrowser
=================

The `Inrupt PodBrowser <https://podbrowser.inrupt.com>`_ is an
application for managing individual Solid Pods.

Features
========

With `Inrupt PodBrowser`_, you can

- Navigate the contents of your Pod.

- Upload/Delete files.

- Create/Delete folders.

- Manage access controls to your data.

Browser Support
===============

You can use `PodBrowser <https://podbrowser.inrupt.com>`_ with the
following supported browsers:

.. list-table::
   :header-rows: 1


   * - Browser
     - Version(s)

   * - Google Chrome
     - 86+ 
   
   * - Mozilla Firefox
     - 82+
     
   * - Microsoft Edge
     - 86+

   * - Apple Safari
     - 14+

Prerequisites
=============

You must provide `PodBrowser <https://podbrowser.inrupt.com>`_
with ``Read``, ``Write``, ``Append``, and ``Control`` access to manage
your Solid Pod. 

For example, if your Pod's URL is ``https://docs-example.inrupt.net/``:

a. Open the URL in a browser and follow the :guilabel:`Log in` flow.

#. Once logged in, go to the :guilabel:`Preferences` tab.

#. In the :guilabel:`Manage your trusted applications` section, add
   PodBrowser to the table:

   .. list-table::

      * - Application URL

        - Access modes

      * - ``https://podbrowser.inrupt.com``

        - ``Read``, ``Write``, ``Append``, and ``Control``

Once you provide PodBrowser with access, log into `PodBrowser`_ to
manage your Pod.

Issues & Help
=============

.. list-table::


   * - Bugs and Feature Requests (Product)
          For public feedback, bug reports, and feature requests,
          please file an issue via `GitHub
          <https://github.com/inrupt/pod-browser>`__.

          For non-public feedback or support inquiries, please use the
          `Inrupt Service Desk
          <https://inrupt.atlassian.net/servicedesk>`_.

   * - Bugs and Feature Requests (Documentation)
           To report a documentation bug or make a documentation
           request, please use the feedback
           widget to create a ticket.

   * - Solid Community Forum
          If you have questions about working with Solid or just
          want to share what you're working on, visit the `Solid forum
          <https://forum.solidproject.org>`_. The Solid forum is a
          good place to meet the rest of the community.


.. toctree::
   :titlesonly:
   :hidden:

   /faq
