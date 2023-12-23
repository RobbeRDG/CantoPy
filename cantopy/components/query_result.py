from typing import List
from components.result_page import ResultPage


class QueryResult:
    """Container for the ResultPages returned by the XenoCanto API in response to a given Query

    Attributes
    ----------
    available_num_recordings : int
        The total available number of recordings found for this query,
        independent of the amount of recordings in this QueryResult.
    available_num_species : int
        The total available number of species found for this query,
        independent of the amount of recordings in this QueryResult.
    page : int
        The page number of the results page that is being displayed.
    num_pages : int
        The total number of pages available for this query.
    recordings : List[Recording]
        An array of recording objects containing detailed information about each recording.
    """
    def __init__(self, result_pages: List[ResultPage]):
        self.result