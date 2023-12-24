from typing import Dict, List
import pytest
import json

from cantopy import ResultPage, QueryResult, Recording

######################################################################
#### XENOCANTO RETURN COMPONENT FIXTURES
######################################################################


@pytest.fixture(scope="session")
def example_xenocanto_query_response() -> Dict[str, str | Dict[str, str]]:
    """An example dict of the query response of the XenoCanto API when sending a 
    Query.

    Returns
    -------
    Dict[str, str]
        The dictionary representation of an example query response of the XenoCanto API.
    """

    # Open the example XenoCanto query response
    with open(
        "resources/test_resources/example_xenocanto_query_response.json",
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
def example_recording(
    example_xenocanto_query_response: Dict[str, str | List[Dict[str, str]]]
) -> Recording:
    """Build a Recording object based on the example XenoCanto API query response.

    Parameters
    ----------
    example_xenocanto_query_response : Dict[str, str  |  Dict[str, str]]
        The dictionary representation of example XenoCanto API query response.

    Returns
    -------
    Recording
        The created Recording object.
    """

    # Handle the string case, which should not be possible
    if isinstance(example_xenocanto_query_response["recordings"], str):
        raise ValueError(
            "The returned recordings instance is a string, but should be a list of dictionaries"
        )

    return Recording(example_xenocanto_query_response["recordings"][0])


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
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
