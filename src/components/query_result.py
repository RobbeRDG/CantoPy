# For information regarding the response structure of the XenoCanto API see:
# https://xeno-canto.org/explore/api

import json


class QueryResult:
    """Class for storing the results of a query to the Xeno Canto API"""

    def __init__(self, json_response: str):
        """Create a QueryResult object form the XenoCanto json response

        Parameters
        ----------
        json_response : str
            The json response from the XenoCanto API. This response json has the following attributes:
                - numRecording: the total number of recordings found for this query
                - numSpecies: the total number of species found for this query
                - page: the page number of the results page that is being displayed
                - numPages: the total number of pages available for this query
                - recordings: an array of recording objects, described in detail below
        """

        # Extract all the information from the response
        self.num_recordings = int(json_response["numRecording"])  # type: ignore
        self.num_species = int(json_response["numSpecies"])  # type: ignore
        self.page = int(json_response["page"])  # type: ignore
        self.num_pages = int(json_response["num_pages"])  # type: ignore
        self.recordings = json_response["recordings"]  # type: ignore

def test_queryresult_init():
    pass
