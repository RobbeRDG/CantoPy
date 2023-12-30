from typing import List, Dict
from cantopy.xenocanto_components.recording import Recording


class ResultPage:
    """Wrapper for storing a single page of results of a query to the Xeno Canto API.

    Attributes
    ----------
    page_id : int
        The page number of the results page that is being displayed.
    recordings : List[Recording]
        An array of recording objects containing detailed information about each recording.

    """

    def __init__(self, single_page_query_response: Dict[str, str | Dict[str, str]]):
        """Create a ResultPage object from the XenoCanto json response

        Parameters
        ----------
        single_page_query_response : Dict[str, str]
            The query response from the XenoCanto API.

        Raises
        ------
        TypeError
            If the id of the page returned by the XenoCanto API could not be read as a string.
        TypeError
            If a recording returned by the XenoCanto API could not be read as a dict.
        """

        # Set the page id
        if isinstance(single_page_query_response["page"], str):
            self.page_id = int(single_page_query_response["page"])
        else:
            raise TypeError(
                f"Error creating a new ResultPage instance from the XenoCanto API response: \\
                The page id returned by the XenoCanto API could not be read as a string: {single_page_query_response['page']}"
            )

        # Set the recordings
        self.recordings: List[Recording] = []
        for query_response_recording in single_page_query_response["recordings"]:
            if isinstance(query_response_recording, dict):
                self.recordings.append(Recording(query_response_recording))
            else:
                raise TypeError(
                    f"Error creating a new ResultPage instance from the XenoCanto API response: \\
                    a recording returned by the XenoCanto API could not be read as a dictionary: {query_response_recording}"
                )
