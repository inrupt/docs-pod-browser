======================
Manage VC-Based Access
======================

.. admonition:: Alpha Release

   PodBrowser supports credential-based access management as an Alpha
   feature.

In addition to managing identity-based access control (see
:ref:`modify-permissions`), PodBrowser can manage credentials-based
access control.

With credentials-based access control, you receive access requests (in
the form of a `Verifiable Credential
<https://www.w3.org/TR/vc-data-model/#credentials>`_) to your Folders
and Files. PodBrowser supports denying the request and allowing the
request. If you allow the request, PodBrowser also supports later
revoking access.s

.. image:: /images/podbrowser-vc-request.png
   :alt: PodBrowser Allow Access Dialog
   :width: 600px

Deny or Allow Access Request
============================

You can deny the request or allow the request as is or allow the
request with modifications:

- To deny the request, click :guilabel:`Deny all access`.

- To allow the requested access as is:

  a. Click :guilabel:`Select All` (to select the resources)
  
  #. Click :guilabel:`Confirm access`
  
- To allow the requested access with modification:

  a. You can update the access end date.

  #. You can select which of the requested files and folders you want
     to allow the requested access.
 
  #. Click :guilabel:`Confirm access`.

View Access Request Details
===========================

.. image:: /images/podbrowser-vc-access-details-view.png
   :alt: PodBrowser View VC-based Access Details
   :width: 600px

PodBrowser's displays the VC-based access information for a file or
folder in the :guilabel:`Sharing` panel of the :ref:`Details view
<view-details>`.

.. _vc-access-details:

View VC-Based Access Details
============================

.. image:: /images/podbrowser-vc-access-details-view.png
   :alt: PodBrowser View VC-based Access Details
   :width: 600px

PodBrowser's displays the VC-based access information for a file or
folder in the :guilabel:`Sharing` panel of the :ref:`Details view
<view-details>`.

#. Click on the vertical dots.

#. Click on :guilabel:`View Details`.

Revoke Granted Access
=====================

.. image:: /images/podbrowser-revoke-access.png
   :alt: PodBrowser View VC-based Access Details
   :width: 600px

To revoke the granted access to a file or folder, in the :ref:`access
details view <vc-access-details>`, click :guilabel:`Revoke access to
<file/folder>`.

