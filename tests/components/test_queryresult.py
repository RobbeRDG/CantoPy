from typing import Dict, List
from cantopy import ResultPage
from components.query_result import QueryResult
import pytest


@pytest.fixture()
def example_query_metadata(example_xenocanto_query_response: Dict[str, str]) -> Dict[str, int]:
    """Build a response metadata dict from the example XenoCanto API query response.

    Parameters
    ----------
    query_response : Dict[str, str]
        The dictionary representation of example XenoCanto API query response.

    Returns
    -------
    Dict[str, int]
        Extracted response metadata from the example XenoCanto API query response.
    """
    return {
        "available_num_recordings": int(
            example_xenocanto_query_response["numRecordings"]
        ),
        "available_num_species": int(example_xenocanto_query_response["numSpecies"]),
        "available_num_pages": int(example_xenocanto_query_response["numPages"]),
    }


@pytest.fixture
def example_result_page(
    example_xenocanto_query_response: Dict[str, str | Dict[str, str]]
) -> ResultPage:
    """Build a ResultPage object from the example XenoCanto API query response.

    Parameters
    ----------
    example_xenocanto_query_response : Dict[str, str  |  Dict[str, str]]
        The dictionary representation of example XenoCanto API query response.

    Returns
    -------
    ResultPage
        The ResultPage object created from the example XenoCanto API query response.
    """
    return ResultPage(example_xenocanto_query_response)


@pytest.fixture
def example_single_page_queryresult(
    example_query_metadata: Dict[str, int], example_result_page: ResultPage
) -> QueryResult:
    """Build a QueryResult object.

    Parameters
    ----------
    example_query_metadata : Dict[str, int]
        The extracted metadata from the example XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response

    Returns
    -------
    QueryResult
        _description_
    """
    return QueryResult(example_query_metadata, [example_result_page])


@pytest.fixture
def example_three_page_queryresult(
    example_query_metadata: Dict[str, int], example_result_page: ResultPage
) -> QueryResult:
    # Build the resultpages
    result_pages: List[ResultPage] = []
    result_pages.append(example_result_page)
    result_pages.append(example_result_page)
    result_pages.append(example_result_page)

    return QueryResult(example_query_metadata, result_pages)


def test_query_result_single_page(single_page_queryresult: QueryResult):
    """Test the initialisation of a QueryResult object containing a single page"""

    # Check attirbutes
    assert single_page_queryresult.available_num_recordings == 67810
    assert single_page_queryresult.available_num_species == 1675
    assert single_page_queryresult.available_num_pages == 136

    # Check stored result pages
    assert len(single_page_queryresult.result_pages) == 1
    assert single_page_queryresult.result_pages[0] == result_page


def test_query_result_multi_page(three_page_queryresult: QueryResult):
    """Test the initialisation of a QueryResult object containing multiple pages (3 pages)"""

    # Check attirbutes
    assert three_page_queryresult.available_num_recordings == 67810
    assert three_page_queryresult.available_num_species == 1675
    assert three_page_queryresult.available_num_pages == 136

    # Check stored result pages
    assert len(three_page_queryresult.result_pages) == 3
    assert three_page_queryresult.result_pages[0] == result_page
