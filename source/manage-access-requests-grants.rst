=================================
Manage Access Requests and Grants
=================================

In addition to managing policy-based access control (see
:ref:`modify-permissions`), PodBrowser can manage access requests and
grants.

With access requests, you receive access requests (in the form of a
`Verifiable Credential
<https://www.w3.org/TR/vc-data-model/#credentials>`_) to your Folders
and Files. PodBrowser supports both approving and denying the access
request. If you approve the access request, PodBrowser also supports
later revoking access grants.

.. image:: /images/podbrowser-access-request.png
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

.. _access-details:

View Access Request Details
===========================

.. image:: /images/podbrowser-access-grant-view.png
   :alt: PodBrowser View Access Grants for Resource
   :width: 600px

PodBrowser's displays the access grants for a file or
folder in the :guilabel:`Sharing` panel of the :ref:`Details view
<view-details>`.

#. Click on the vertical dots.

#. Click on :guilabel:`View Details`.

Revoke Granted Access
=====================

.. image:: /images/podbrowser-revoke-access.png
   :alt: PodBrowser View Access Grants for Resource
   :width: 600px

To revoke the granted access to a file or folder, in the :ref:`access
details view <access-details>`, click :guilabel:`Revoke access to
<file/folder>`.

