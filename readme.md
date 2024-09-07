# CantoPy
Cantopy is an API wrapper and downloader for easy retrieval of animal recordings from the XenoCanto database.

## Installation
Download the latest published version of this packages from PyPI by running the following command:

```bash
pip install cantopy
```

## Usage
The CantoPy package contains three main components a user should use to look up and download recordings from the XenoCanto API: the **Query** class, a **FetchManager** and a **DownloadManager**.

### Query
The Query class is a wrapper class to construct a search query for the XenoCanto API.

To for example construct a query to look for high-quality recordings ("A"-quality) of a common blackbird (Turdus merula). The following code snippet can be used:

```python
from cantopy import Query

query = Query(species_name="common blackbird", quality="A")
```

This Query class largely adheres to the same query search fields available on the XenoCanto website search box. For more information about these search fields, visit the [XenoCanto search documentation](https://xeno-canto.org/help/search).


### FetchManager
The FetchManager class handles the communication of our Query to the XenoCanto API. To instanciate such a FetchManager, use the following code:

```python
from cantopy import FetchManager

fetch_manager = FetchManager()
```

The primary use of this FetchManager is to retrieve recordings from the XenoCanto records database adhering to our search Query object. To for example get the recordings adhering to our previously created Query, run the following code:

```python
query_result = fetch_manager.send_query(query, max_pages=3)
```

Here, the `max_pages` attribute is an optional attribute to state the maximum result pages we want to fetch from XenoCanto. In the underlying XenoCanto API, to account for searches with a lot of corresponding records in the database, the API returns the found results on a per-page basis to avoid congestion. When we thus for example set the max number of pages to 3, we only want the three first page results provided by the API. This max pages attribute defaults to `1` if not passed.

### DownloadManager
The DowloadManager handles all things related to downloading the recordings found by the FetchManager for our Query. To create and instance of the DownloadManager, run the following snipped:

```python
from cantopy import DownloadManager

downloadmanager = DownloadManager("/workspaces/birdnet_data_generation/data", max_workers=4)
```

Here the DownloadManager expects a download `data_base_path` as first attribute where it will store all the downloaded recordings. Note that this should be some kind of overarching root folder, the DownloadManager will create a subfolders for each species with downloaded recordings withing this root folder. Secondly, an optional `max_workers` can also be passed during initialization. The downloadmanager supports multi-threaded downloading of the recordings, to allow for concurrent downloading, the max number of workers determines the number of treads to create. The default number of workers is `1`.

The primary purpose of this DownloadManager is to allow for the download of the Query result's recordings obtained by the FetchManager. To for example download the recordings in the QueryResult obtained in our previous Query, run:

```python
downloadmanager.download_all_recordings_in_queryresult(query_result)
```

Note that the Downloadmanager



TODO:
- Make fetchmanager functions simple class methods that don't require class initialization
- Can we change the downloadmanager functions names (simpler)?