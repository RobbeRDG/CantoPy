from typing import List, Dict, Any
from cantopy.components.recording import Recording


class ResultPage:
    """Wrapper for storing a single page of results of a query to the Xeno Canto API

    Attributes
    ----------
    page : int
        The page number of the results page that is being displayed.
    recordings : List[Recording]
        An array of recording objects containing detailed information about each recording.

    """

    def __init__(self, single_page_query_response: Dict[str, str | Dict[str, str]]):
        """Create a ResultPage object from the XenoCanto json response

        Parameters
        ----------
        single_page_query_response : Dict[str, str]
            The response from the XenoCanto API.
        """

        self.page = int(single_page_query_response["page"])
        self.recordings: List[Recording] = []
        for query_response_recording in single_page_query_response["recordings"]:
            self.recordings.append(Recording(query_response_recording))
