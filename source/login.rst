=======================
Login and Authorization
=======================

To access your Pod via `PodBrowser <https://podbrowser.inrupt.com>`_,

#. Go to https://podbrowser.inrupt.com/login in a Web browser.

#. Select or enter your Solid Identity Provider and click :guilabel:`Log In`.

#. Log in to your Solid Identity Provider.

.. image:: /images/podbrowser-pod-inrupt-com.png
   :alt: PodBrowser Log In Screen

Examples
========

If your Pod is hosted on one of the `Inrupt Pod Spaces
<https://docs.inrupt.com/pod-spaces>`_, click on the corresponding tab
for an example.

.. tabs::

   .. tab:: ``pod.inrupt.com``
   
      #. For the Solid ID Provider, enter ``https://broker.pod.inrupt.com`` and click :guilabel:`Log In`.
  
      #. Enter your :guilabel:`Username` and :guilabel:`Password` and login.
 
      #. The consent screen appears. To continue,
         click :guilabel:`Authorize` to accept the Inrupt Terms and Conditions and
         authorize PodBrowser.

      ➢ To sign up for a Pod on ``https://pod.inrupt.com``, go to
      https://signup.pod.inrupt.com/.

   .. tab:: ``pod-compat.inrupt.com``
  
      #. For the Solid ID Provider, enter ``https://broker.pod-compat.inrupt.com`` and click :guilabel:`Log In`.
  
      #. Enter your :guilabel:`Username` and :guilabel:`Password` and login.
 
      #. The consent screen appears. To continue,
         click :guilabel:`Authorize` to accept the Inrupt Terms and Conditions and
         authorize PodBrowser.

      ➢ To sign up for a Pod on ``https://pod-compat.inrupt.com``, go to
      https://signup.pod-compat.inrupt.com/.

   .. tab:: ``inrupt.net``

      #. For the Solid ID Provider, enter ``https://inrupt.net`` and click :guilabel:`Log In`.
  
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

For information on these Solid Servers, see `Inrupt Pod Spaces`_.
