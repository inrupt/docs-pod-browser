=====
Login
=====

To access your Pod via `PodBrowser <https://podbrowser.inrupt.com/login>`_,

#. Go to https://podbrowser.inrupt.com/login in a Web browser.

#. If your Pod is hosted on ``pod.inrupt.com``, click :guilabel:`Sign
   In`.

   If your Pod is hosted elsewhere (such as ``inrupt.net``), click
   :guilabel:`Sign in with other provider`, enter your Provider, and
   click :guilabel:`Go`.

#. Log in to your Solid Identity Provider.

#. The consent screen appears. To continue, click :guilabel:`Approve`
   to approve access to the requested information.

.. image:: /images/podbrowser-pod-inrupt-com.png
   :alt: PodBrowser Log In Screen
   :width: 400px
   :target: https://podbrowser.inrupt.com/login

Examples
========

.. tabs::

   .. tab:: ``pod.inrupt.com``
   
      #. Click :guilabel:`Sign In`.
  
      #. Enter your :guilabel:`Username` and :guilabel:`Password` and :guilabel:`Sign In`.
 
      #. The consent screen appears. To continue, click
         :guilabel:`Approve` to approve access to the requested information.

      To sign up for a Pod on ``https://pod.inrupt.com``, go to
      https://signup.pod.inrupt.com/.

   .. tab:: ``inrupt.net``

      #. Click :guilabel:`Sign in with other provider`.
      
      #. Select or enter ``https://inrupt.net`` and click :guilabel:`Go`.
  
      #. Enter your :guilabel:`Username` and :guilabel:`Password` and login.
 
      #. If you have not previously authorized PodBrowser to access
         your Pod, you will be asked to authorize "Inrupt PodBrowser".
      
         a. You must select **all** four check boxes. 
       
         #. Click :guilabel:`Authorize`. You are directed back to
            `PodBrowser`_. 

         If you did not select **all** four required access at this
         time, you can manually grant PodBrowser the required access.
         For details, see :ref:`faq-grant-access-manually`.

       To sign up for a Pod on ``https://inrupt.net``, go to
       https://inrupt.net.

For information on these Solid Servers, see `Inrupt Pod Spaces
<https://docs.inrupt.com/pod-spaces>`_.
