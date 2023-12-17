from typing import List, Dict, Any
from cantopy.components.recording import Recording


class QueryResult:
    """Wrapper for storing the results of a query to the Xeno Canto API

    Attributes
    ----------
    num_recordings : int
        The total number of recordings found for this query.
    num_species : int
        The total number of species found for this query.
    page : int
        The page number of the results page that is being displayed.
    num_pages : int
        The total number of pages available for this query.
    recordings : List[Recording]
        An array of recording objects containing detailed information about each recording.

    """

    def __init__(self, query_response: Dict[str, Any]):
        """Create a QueryResult object from the XenoCanto json response

        Parameters
        ----------
        query_response : dict
            The response from the XenoCanto API.
        """

        self.num_recordings = int(query_response["numRecordings"])
        self.num_species = int(query_response["numSpecies"])
        self.page = int(query_response["page"])
        self.num_pages = int(query_response["numPages"])
        self.recordings: List[Recording] = []
        for query_response_recording in query_response.get("recordings", []):
            self.recordings.append(Recording(query_response_recording))
