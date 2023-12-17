from typing import List
import requests

from cantopy.components import Query, QueryResult


class CantoPy:
    """CantoPy, the XenoCanto API wrapper"""

    def __init__(self) -> None:
        self.__base_url = "https://www.xeno-canto.org/api/2/recordings"

    def send_query(self, query: Query, max_pages: int = 1) -> List[QueryResult]:
        """Send a query to the Xeno Canto API

        Parameters
        ----------
        query : Query
            the query to send to the Xeno Canto API
        max_pages : int, optional
            specify a maximum number of pages of recordings to fetch, by default 1

        Returns
        -------
        QueryResult
            python object containing the results of the query
        """

        # We need to first send an initial query to determine the number of available result pages
        query_str = query.to_string()
        QueryResult = self.__send_query_request(query_str)

        return [QueryResult]

    def __send_query_request(self, query_str: str, page: int = 1) -> QueryResult:
        query_response = requests.get(
            self.__base_url,
            params={
                "query": query_str,
                "page": page,
            },
            timeout=5.0,
        ).json()

        return QueryResult(query_response)
