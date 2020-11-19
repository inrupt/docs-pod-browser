=================
Inrupt PodBrowser
=================

The Inrupt `PodBrowser <https://podbrowser.inrupt.com>`_ is an
application for managing individual Solid Pods.

Features
========

With Inrupt `PodBrowser`_, you can

- Manage your data.

- Manage access control.

- Manage contacts.

Browser Support
===============

`PodBrowser <https://podbrowser.inrupt.com>`_ supports the latest 2
stable releases of the following:

Desktop
-------

.. list-table::
   :header-rows: 1

   * - Browser

     - Version

   * - Google Chrome

     - Latest 2 stable releases

   * - Mozilla Firefox

     - Latest 2 stable releases

   * - Microsoft Edge

     - Latest 2 stable releases

   * - Apple Safari

     - Latest 2 stable releases

Mobile
------

.. list-table::
   :header-rows: 1

   * - Browser

     - Version

   * - iOS/Safari

     - Latest 2 stable releases

   * - Android/Chrome

     - Latest 2 stable releases

   * - Android / Samsung Internet

     - Latest 2 stable releases

Login and Authorization
=======================

To login to `PodBrowser`_

If your Pod is hosted on ``https://pod.inrupt.com``,
  #. For the ID Provider, enter ``https://broker.dev-ess.inrupt.com``.
  
  #. Enter your :guilabel:`Username` and :guilabel:`Password` and login.
 
  #. If you have not authorized PodBrowser to
     access your Pod, you will be asked to authorize "Inrupt
     PodBrowser". Click :guilabel:`Authorize`.

If your Pod is hosted on ``https://inrupt.net``
   #. For the ID Provider, enter ``https://inrupt.net``.
  
   #. Enter your :guilabel:`Username` and :guilabel:`Password` and login.
 
   #. If you have not previously authorized PodBrowser to access your
      Pod, you will be asked to authorize "Inrupt PodBrowser".
      
      a. You must select **all** four check boxes. 
      
      #. Click :guilabel:`Authorize`. You are directed back to
         `PodBrowser`_. 
         
      #. Login to `PodBrowser`_.
 
   If you did not select **all** four required access at this time, you
   can manually grant PodBrowser the required access. For details, see
   :ref:`faq-grant-access-manually`.

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
