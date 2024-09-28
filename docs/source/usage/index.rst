Usage
=====================
For general usage, the CantoPy package contains three main components to look up and 
download recordings from the Xeno-Canto API: the 
:func:`Query <cantopy.xenocanto_components.Query>` class, the 
:func:`FetchManager <cantopy.fetch_manager.FetchManager>`, and the 
:func:`DownloadManager <cantopy.download_manager.DownloadManager>`.

The following example demonstrates how to use these components to retrieve high-quality 
(*quality="A"*) recordings of a common blackbird (*Turdus merula*):

.. code-block:: python

    from cantopy import Query, FetchManager, DownloadManager

    # Initialize the search query
    query = Query(species_name="common blackbird", quality="A")

    # Find matching query results on the Xeno-Canto database
    query_result = FetchManager.send_query(query, max_pages=3)

    # Initialize a DownloadManager
    download_manager = DownloadManager("<download_base_folder>")

    # Download the corresponding recordings of the retrieved results
    download_manager.download_all_recordings_in_queryresult(query_result)

For more detailed information on the usage of each component, refer to the 
:doc:`API documentation <../api/index>`.