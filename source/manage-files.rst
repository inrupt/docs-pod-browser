=======================
Manage Data: Files View
=======================

To manage the files in a Pod, go to :guilabel:`Files` view in
PodBrowser. The :guilabel:`Files` view is the default view, but you can
also switch to the :guilabel:`Files` view by clicking on the Files icon
on the top menu bar.

.. image:: /images/podbrowser-files-view.png
   :alt: PodBrowser Files View
   :width: 600px

The :guilabel:`Files` view displays the contents of your Pod.
The contents of your Pod have the following type:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Type

     - Description

   * - Container

     - A Container is analogous to a folder; it contains other
       Containers and Resources.

   * - Resource

     - A Resource refers to a file of any type.

Navigate the Pod
================

In the :guilabel:`Files` view, click on a folder to navigate into the
folder.

Alternatively, you can go directly to a folder:

#. Click on the :guilabel:`Pod` indicator dropdown on the top left-hand side.

#. Select :guilabel:`-> Change Pod`.

#. Enter the URI of a folder. You must include specify the full URL,
   including the protocol ``https:// ...``.

#. Click :guilabel:`Go`.

.. _view-details:

View Details of Folders and Files
=================================

To view the details of a folder:

#. Go to the specific folder and click :guilabel:`Folder
   Details` to open a Details view. The Details view provides
   information about the current folder you are browsing.

   For example, the following image displays the details for the
   folder named ``profile``:

   .. image:: /images/podbrowser-folder-details.png
      :alt: Details of the profile Folder/Container
      :width: 650px

#. From the folder's Details view:

   - You can :ref:`Delete <delete>` the folder.

   - You can view its Details.

   - You can modify the :ref:`Permissions <modify-permissions>` to the folder.

To view the details of a file/Resource:

#. Click on the file to open a Details view. The Details view
   provides information about the current selected file. For example,
   the following image displays the details for the file named
   ``card``:

   .. image:: /images/podbrowser-resource-details.png
      :alt: Details of a file named card
      :width: 650px

#. From the file's Details view:

   - You can :ref:`Download <download>` the file.

   - You can :ref:`Delete <delete>` the file.

   - You can view its Details.

   - You can modify the :ref:`Permissions <modify-permissions>` to the File.

.. _delete:

Delete Folders and Files
========================

You can delete a folder or a file from its :ref:`Details view
<view-details>`:

#. Open the Details View for the folder or file to delete:

   - For a folder, navigate to the folder and click :guilabel:`Folder
     Details`. This opens its Details View.

   - For a file, select the file. This opens its Details View.

#. From the Details view, click :guilabel:`Delete`. A Confirmation
   dialog appears. 

#. To confirm the delete, click :guilabel:`OK` in the Confirmation
   dialog.

.. _download:

Download Files
==============

You can download a file from its :ref:`Details view <view-details>`:

#. Select the file to download. This opens its Details View.

#. From the Details view, click :guilabel:`Download`. Follow your Web
   browser's download action flow.

.. _modify-permissions:

Modify Permissions for Folders and Files
========================================

You can modify the access permissions for a folder or a file from its
:ref:`Details view <view-details>`:

#. Open the Details View:

   - For a folder, navigate to the folder and click
     :guilabel:`Folder Details`. This opens its Details View.

   - For a file, select the file. This opens its Details View.

#. From the Details view, click :guilabel:`Permissions` to expand the
   panel.

   - To grant access to a new individual, 

     a. Click :guilabel:`Add with WebID`.

     #. Enter the individual's WebID. You must include specify the full
        URL, including the protocol ``https:// ...``.

     #. Expand the access modes by clicking on the Access Modes caret (``v``).

     #. Select the access modes to grant.

     #. Click :guilabel:`Add`.

   - To modify existing access for an individual,
   
     a. Expand the individual's access modes by clicking on the associated
        Access Modes caret (``v``).
     
        - To revoke an access mode, deselect the access mode to revoke.

        - To grant an access mode, select the access mode to grant.

     #. Click :guilabel:`SAVE`.

Create Folder
=============

To create a folder in the current folder:

#. Click on the :guilabel:`Create File` link.

#. Enter in the folder's name.

#. Click :guilabel:`Create Folder`.

Upload Files
============

To upload a file to the current folder:

#. Click on the :guilabel:`Upload File` link.

#. Select the file to upload.

Switch Pod
==========

To switch to another Pod:

#. Click on the :guilabel:`Pod` indicator dropdown on the top left-hand side.

#. Select :guilabel:`-> Change Pod`.

#. Enter the Pod URI (or the URI of a folder in the Pod). You must
   include specify the full URL, including the protocol ``https:// ...``.

#. Click :guilabel:`Go`.

.. _files-view-bookmark:

Bookmark Files and Folders and Pods
===================================

Bookmark Files and Folders
--------------------------

To bookmark a folder or a file:

#. Select the star icon next to the folder or file. 

To remove the folder or file from your bookmarks:

#. Deselect the star icon.

Bookmark a Pod
--------------

To bookmark the current Pod:

#. Click on the :guilabel:`Pod` indicator dropdown on the top left-hand side.

#. Select :guilabel:`Bookmark Pod`.

To remove a Pod from your bookmarks:

#. Click on the :guilabel:`Pod` indicator dropdown on the top left-hand side.

#. Select :guilabel:`Remove Pod Bookmark`.

You can view your saved Bookmarks in :doc:`Bookmarks View
</manage-bookmarks>`.

