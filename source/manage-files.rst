=======================
Manage Data: Files View
=======================

To manage the files in a Pod, go to :guilabel:`Files` view in
PodBrowser; i.e., click on :guilabel:`Files` on the top menu bar.

.. image:: /images/podbrowser-files-view.png
   :alt: PodBrowser Files View
   :width: 600px

Files View
==========

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

#. Click on the :guilabel:`Your Pod` on the top right-hand side.

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

#. From the folder's Details view:

   - You can :ref:`Delete <delete>` the folder.

   - You can view its Details.

   - You can modify the :ref:`Sharing <modify-permissions>` permissions
     for the folder.

To view the details of a file/Resource:

#. Click on the file to open a Details view. The Details view
   provides information about the current selected file.

#. From the file's Details view:

   - You can :ref:`Download <download>` the file.

   - You can :ref:`Delete <delete>` the file.

   - You can view its Details.

   - You can modify the :ref:`Sharing <modify-permissions>` permissions
     for the File.

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

#. From the Details view, click :guilabel:`Sharing` to expand the
   panel. You can:

   - Manage Editors (:guilabel:`+ Edit Editors`), 

   - Manage Viewers (:guilabel:`+ Edit Viewers`), or 

   - Specify Advanced Sharing.

   .. tip::
   
      When adding a new WebID for sharing, you must include specify the
      full URL, including the protocol ``https:// ...``.

Create Folder
=============

To create a folder in the current folder:

#. Click on the :guilabel:`Create Folder` link.

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

#. Click on the :guilabel:`Your Pod` dropdown on the top right-hand side.

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

#. Click on the :guilabel:`Your Pod` dropdown on the top right-hand side.

#. Select :guilabel:`Bookmark Pod`.

To remove a Pod from your bookmarks:

#. Click on the :guilabel:`Your Pod` dropdown on the top right-hand side.

#. Select :guilabel:`Remove Pod Bookmark`.

You can view your saved Bookmarks in :doc:`Bookmarks View
</manage-bookmarks>`.

