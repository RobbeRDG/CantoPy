from typing import Dict, List
from cantopy import ResultPage
from components.query_result import QueryResult
import pytest


@pytest.fixture()
def example_query_metadata(
    example_xenocanto_query_response: Dict[str, str]
) -> Dict[str, int]:
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
    """Build a single-page QueryResult object based on the example XenoCanto API query response.

    Parameters
    ----------
    example_query_metadata : Dict[str, int]
        The extracted metadata from the example XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response

    Returns
    -------
    QueryResult
        The constructed single-page QueryResult object.
    """
    return QueryResult(example_query_metadata, [example_result_page])


@pytest.fixture
def example_three_page_queryresult(
    example_query_metadata: Dict[str, int], example_result_page: ResultPage
) -> QueryResult:
    """Build a three-page QueryResult object based on the example XenoCanto API query response.

    Parameters
    ----------
    example_query_metadata : Dict[str, int]
        The extracted metadata from the example XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response.
        In order to build a three-page QueryResult, we just create a list of three copies
        of this result page.

    Returns
    -------
    QueryResult
        The constructed three-page QueryResult object.
    """

    # Build the resultpages
    result_pages: List[ResultPage] = []
    result_pages.append(example_result_page)
    result_pages.append(example_result_page)
    result_pages.append(example_result_page)

    return QueryResult(example_query_metadata, result_pages)


def test_query_result_single_page(
    example_single_page_queryresult: QueryResult, example_result_page: ResultPage
):
    """Test the initialisation of a QueryResult object containing a single page.

    Parameters
    ----------
    example_single_page_queryresult : QueryResult
        A three-page QueryResult object based on the example XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response.
    """

    # Check attirbutes
    assert example_single_page_queryresult.available_num_recordings == 67810
    assert example_single_page_queryresult.available_num_species == 1675
    assert example_single_page_queryresult.available_num_pages == 136

    # Check stored result pages
    assert len(example_single_page_queryresult.result_pages) == 1
    assert example_single_page_queryresult.result_pages[0] == example_result_page


def test_query_result_multi_page(
    example_three_page_queryresult: QueryResult, example_result_page: ResultPage
):
    """Test the initialisation of a QueryResult object containing multiple pages (3 pages).

    Parameters
    ----------
    example_single_page_queryresult : QueryResult
        A three-page QueryResult object based on the example XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response.
    """

    # Check attirbutes
    assert example_three_page_queryresult.available_num_recordings == 67810
    assert example_three_page_queryresult.available_num_species == 1675
    assert example_three_page_queryresult.available_num_pages == 136

    # Check stored result pages
    assert len(example_three_page_queryresult.result_pages) == 3
    assert example_three_page_queryresult.result_pages[0] == example_result_page
