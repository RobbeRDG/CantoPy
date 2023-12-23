import json
from typing import List
from cantopy import ResultPage
from components.query_result import QueryResult


def test_query_result_single_page():
    """Test the initialisation of a QueryResult object containing a single page"""

    # Open the example XenoCanto query response
    with open(
        "tests/test_resources/xenocanto_query_response.json", "r", encoding="utf-8"
    ) as file:
        query_response = json.load(file)

    # Extract the metadata information of this query
    query_metadata = {
        "available_num_recordings": int(query_response["numRecordings"]),
        "available_num_species": int(query_response["numSpecies"]),
        "available_num_pages": int(query_response["numPages"]),
    }

    # Build first resultpage
    result_page = ResultPage(query_response)

    # Build a QueryResult
    query_result = QueryResult(query_metadata, [result_page])

    # Check attirbutes
    assert query_result.available_num_recordings == 67810
    assert query_result.available_num_species == 1675
    assert query_result.available_num_pages == 136

    # Check stored result pages
    assert len(query_result.result_pages) == 1
    assert query_result.result_pages[0] == result_page


def test_query_result_multi_page():
    """Test the initialisation of a QueryResult object containing multiple pages (3 pages)"""

    # Open the example XenoCanto query response
    with open(
        "tests/test_resources/xenocanto_query_response.json", "r", encoding="utf-8"
    ) as file:
        query_response = json.load(file)

    # Extract the metadata information of this query
    query_metadata = {
        "available_num_recordings": int(query_response["numRecordings"]),
        "available_num_species": int(query_response["numSpecies"]),
        "available_num_pages": int(query_response["numPages"]),
    }

    # Build the resultpages
    result_pages: List[ResultPage] = []
    result_page = ResultPage(query_response)
    result_pages.append(result_page)
    result_pages.append(result_page)
    result_pages.append(result_page)

    # Build a QueryResult
    query_result = QueryResult(query_metadata, result_pages)

    # Check attirbutes
    assert query_result.available_num_recordings == 67810
    assert query_result.available_num_species == 1675
    assert query_result.available_num_pages == 136

    # Check stored result pages
    assert len(query_result.result_pages) == 3
    assert query_result.result_pages[0] == result_page
