API
=====================

XenoCanto Components
---------------------
The :mod:`cantopy.xenocanto_components` module contains multiple wrapper classes and 
functions for interacting with the XenoCanto API.

The main class in this module that a user should interact with is the 
:func:`Query <cantopy.xenocanto_components.Query>` class, which is used to create search
queries for the Xeno-Canto database. However, the module also contains the utility 
:func:`QueryResult <cantopy.xenocanto_components.QueryResult>`, 
:func:`Recording <cantopy.xenocanto_components.Recording>`, and 
:func:`ResultPage <cantopy.xenocanto_components.ResultPage>` classes, which are used to 
store and manage the results of search queries. These classes should not be directly
instantiated by the user.

.. automodule:: cantopy.xenocanto_components
   :members:
   :undoc-members:

Fetch Manager
---------------------
The :mod:`cantopy.fetch_manager` module contains the 
:func:`FetchManager <cantopy.fetch_manager.FetchManager>` class, which is responsible 
for sending search queries to the Xeno-Canto database and retrieving the corresponding 
results.

.. automodule:: cantopy.fetch_manager
   :members:
   :undoc-members:

Download Manager
---------------------
The :mod:`cantopy.download_manager` module contains the 
:func:`DownloadManager <cantopy.download_manager.DownloadManager>` class, which is
responsible for downloading the recordings of the search results retrieved by the
FetchManager.

.. automodule:: cantopy.download_manager
    :members:
    :undoc-members: