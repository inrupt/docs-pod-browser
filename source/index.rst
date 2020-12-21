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

Login and Authorization
=======================

To access your Pod via `PodBrowser`_, go to
https://podbrowser.inrupt.com/login and log in with your Solid Identity
Provider. For example, if your Pod is hosted on

.. tabs::

   .. tab:: ``pod.inrupt.com``
   
      #. For the Solid ID Provider, enter ``https://broker.pod.inrupt.com``.
  
      #. Enter your :guilabel:`Username` and :guilabel:`Password` and login.
 
      #. If you have not accepted the Inrupt Terms and Conditions and
         authorized PodBrowser, the consent screen appears. To continue,
         click :guilabel:`Authorize`.

      ➢ To sign up for a Pod on ``https://pod.inrupt.com``, go to
      https://signup.pod.inrupt.com/.

   .. tab:: ``pod-compat.inrupt.com``
  
      #. For the Solid ID Provider, enter ``https://broker.pod-compat.inrupt.com``.
  
      #. Enter your :guilabel:`Username` and :guilabel:`Password` and login.
 
      #. If you have not accepted the Inrupt Terms and Conditions and
         authorized PodBrowser, the consent screen appears. To continue,
         click :guilabel:`Authorize`.

      ➢ To sign up for a Pod on ``https://pod-compat.inrupt.com``, go to
      https://signup.pod-compat.inrupt.com/.

   .. tab:: ``inrupt.net``

      #. For the Solid ID Provider, enter ``https://inrupt.net``.
  
      #. Enter your :guilabel:`Username` and :guilabel:`Password` and login.
 
      #. If you have not previously authorized PodBrowser to access
         your Pod, you will be asked to authorize "Inrupt PodBrowser".
      
         a. You must select **all** four check boxes. 
       
         #. Click :guilabel:`Authorize`. You are directed back to
            `PodBrowser`_. 
         
         #. Login to `PodBrowser`_.

         If you did not select **all** four required access at this
         time, you can manually grant PodBrowser the required access.
         For details, see :ref:`faq-grant-access-manually`.

       ➢ To sign up for a Pod on ``https://inrupt.net``, go to
       https://inrupt.net.

For information on these Solid Servers, see `Inrupt Pod Spaces
<https://docs.inrupt.com/pod-spaces>`_.

Browser Support
===============

`PodBrowser <https://podbrowser.inrupt.com>`_ supports the latest 2
stable releases of the following browsers:

.. list-table::
   :widths: 45 55
   :stub-columns: 1

   * - Desktop
   
     - | Google Chrome
       | Mozilla Firefox
       | Microsoft Edge
       | Apple Safari

   * - Mobile

     - | iOS/Safari
       | Android/Chrome
       | Android/Samsung Internet

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
