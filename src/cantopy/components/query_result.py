# For information regarding the response structure of the XenoCanto API see:
# https://xeno-canto.org/explore/api


class QueryResult:
    """Wrapper for storing the results of a query to the Xeno Canto API

    Attributes
    ----------
    numRecordings : int
        The total number of recordings found for this query.
    numSpecies : int
        The total number of species found for this query.
    page : int
        The page number of the results page that is being displayed.
    numPages : int
        The total number of pages available for this query.
    recordings : list
        An array of recording objects containing detailed information about each recording.

    """

    def __init__(self, query_response: dict):
        """Create a QueryResult object form the XenoCanto json response

        Parameters
        ----------
        query_response : dict
            The response from the XenoCanto API.
        """

        # Extract all the information from the response
        self.num_recordings = query_response["numRecording"]
        self.num_species = query_response["numSpecies"]
        self.page = query_response["page"]
        self.num_pages = query_response["num_pages"]
        self.recordings = query_response["recordings"]
