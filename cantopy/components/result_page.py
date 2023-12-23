from typing import List, Dict, Any
from cantopy.components.recording import Recording


class ResultPage:
    """Wrapper for storing a single page of results of a query to the Xeno Canto API

    Attributes
    ----------
    available_num_recordings : int
        The total number of recordings available for this query, independent of page limit.
    available_num_species : int
        The total number of species available for this query, independent of page limit.
    page : int
        The page number of the results page that is being displayed.
    available_num_pages : int
        The total number of pages available for this query.
    recordings : List[Recording]
        An array of recording objects containing detailed information about each recording.

    """

    def __init__(self, single_page_query_response: Dict[str, Any]):
        """Create a ResultPage object from the XenoCanto json response

        Parameters
        ----------
        single_page_query_response : dict
            The response from the XenoCanto API.
        """

        self.available_num_recordings = int(single_page_query_response["numRecordings"])
        self.available_num_species = int(single_page_query_response["numSpecies"])
        self.page = int(single_page_query_response["page"])
        self.available_num_pages = int(single_page_query_response["numPages"])
        self.recordings: List[Recording] = []
        for query_response_recording in single_page_query_response.get("recordings", []):
            self.recordings.append(Recording(query_response_recording))
