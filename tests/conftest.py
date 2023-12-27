from typing import Dict, List
import pytest
import json

from cantopy import ResultPage, QueryResult, Recording

######################################################################
#### XENOCANTO RETURN COMPONENT FIXTURES
######################################################################


@pytest.fixture(scope="session")
def example_xenocanto_query_response_page_1() -> Dict[str, str | Dict[str, str]]:
    """An example dict of the query response of the XenoCanto API when sending a
    Query to recieve the result page with id 1.

    Returns
    -------
    Dict[str, str]
        The dictionary representation of an example query response of the XenoCanto API.
    """

    # Open the example XenoCanto query response
    with open(
        "resources/test_resources/example_xenocanto_query_response_page_1.json",
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


@pytest.fixture(scope="session")
def example_xenocanto_query_response_page_2() -> Dict[str, str | Dict[str, str]]:
    """An example dict of the query response of the XenoCanto API when sending a
    Query to recieve the result page with id 2.

    Returns
    -------
    Dict[str, str]
        The dictionary representation of an example query response of the XenoCanto API.
    """

    # Open the example XenoCanto query response
    with open(
        "resources/test_resources/example_xenocanto_query_response_page_2.json",
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


@pytest.fixture(scope="session")
def example_query_metadata_page_1(
    example_xenocanto_query_response_page_1: Dict[str, str]
) -> Dict[str, int]:
    """Build a response metadata dict from the page 1 example XenoCanto API query response.

    Parameters
    ----------
    example_xenocanto_query_response_page_1 : Dict[str, str]
        The dictionary representation of example XenoCanto API query response.

    Returns
    -------
    Dict[str, int]
        Extracted response metadata from the example page 1 XenoCanto API query response.
    """
    return {
        "available_num_recordings": int(
            example_xenocanto_query_response_page_1["numRecordings"]
        ),
        "available_num_species": int(
            example_xenocanto_query_response_page_1["numSpecies"]
        ),
        "available_num_pages": int(example_xenocanto_query_response_page_1["numPages"]),
    }


@pytest.fixture(scope="session")
def example_query_metadata_page_2(
    example_xenocanto_query_response_page_2: Dict[str, str]
) -> Dict[str, int]:
    """Build a response metadata dict from the page 2 example XenoCanto API query response.

    Parameters
    ----------
    example_xenocanto_query_response_page_2 : Dict[str, str]
        The dictionary representation of example page 2 XenoCanto API query response.

    Returns
    -------
    Dict[str, int]
        Extracted response metadata from the example XenoCanto API query response.
    """
    return {
        "available_num_recordings": int(
            example_xenocanto_query_response_page_2["numRecordings"]
        ),
        "available_num_species": int(
            example_xenocanto_query_response_page_2["numSpecies"]
        ),
        "available_num_pages": int(example_xenocanto_query_response_page_2["numPages"]),
    }


@pytest.fixture(scope="session")
def example_result_page_page_1(
    example_xenocanto_query_response_page_1: Dict[str, str | Dict[str, str]]
) -> ResultPage:
    """Build a ResultPage object from the example page 1 XenoCanto API query response.

    Parameters
    ----------
    example_xenocanto_query_response_page_1 : Dict[str, str  |  Dict[str, str]]
        The dictionary representation of example page 1 XenoCanto API query response.

    Returns
    -------
    ResultPage
        The ResultPage object created from the example XenoCanto API query response.
    """
    return ResultPage(example_xenocanto_query_response_page_1)


@pytest.fixture(scope="session")
def example_result_page_page_2(
    example_xenocanto_query_response_page_2: Dict[str, str | Dict[str, str]]
) -> ResultPage:
    """Build a ResultPage object from the example page 2 XenoCanto API query response.

    Parameters
    ----------
    example_xenocanto_query_response_page_2 : Dict[str, str  |  Dict[str, str]]
        The dictionary representation of example page 2 XenoCanto API query response.

    Returns
    -------
    ResultPage
        The ResultPage object created from the example XenoCanto API query response.
    """
    return ResultPage(example_xenocanto_query_response_page_2)


@pytest.fixture(scope="session")
def example_recording_1_from_example_xenocanto_query_response_page_1(
    example_xenocanto_query_response_page_1: Dict[str, str | List[Dict[str, str]]]
) -> Recording:
    """Build a Recording object based on the first recording in the example page 1
    XenoCanto API query response.

    Parameters
    ----------
    example_xenocanto_query_response_page_1 : Dict[str, str  |  Dict[str, str]]
        The dictionary representation of example page 1 XenoCanto API query response.

    Returns
    -------
    Recording
        The created Recording object.
    """

    # Handle the string case, which should not be possible
    if isinstance(example_xenocanto_query_response_page_1["recordings"], str):
        raise ValueError(
            "The returned recordings instance is a string, but should be a list of dictionaries"
        )

    return Recording(example_xenocanto_query_response_page_1["recordings"][0])


@pytest.fixture(scope="session")
def example_single_page_queryresult(
    example_query_metadata_page_1: Dict[str, int],
    example_result_page_page_1: ResultPage,
) -> QueryResult:
    """Build a single-page QueryResult object based on the example page 1 XenoCanto API
    query response.

    Parameters
    ----------
    example_query_metadata_page_1 : Dict[str, int]
        The extracted metadata from the example page 1 XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example page 1 XenoCanto API query response

    Returns
    -------
    QueryResult
        The constructed single-page QueryResult object.
    """
    return QueryResult(example_query_metadata_page_1, [example_result_page_page_1])


@pytest.fixture(scope="session")
def example_two_page_queryresult(
    example_query_metadata_page_1: Dict[str, int],
    example_result_page_page_1: ResultPage,
    example_result_page_page_2: ResultPage,
) -> QueryResult:
    """Build a two-page QueryResult object based on the example page 1 and 2 XenoCanto API
    query responses.

    Parameters
    ----------
    example_query_metadata_page_1 : Dict[str, int]
        The extracted metadata from the example page 1 XenoCanto API query response.
        Page 2 metadata is the same as page 1 metadata, so this is not needed.
    example_result_page_page_1 : ResultPage
        The ResultPage object created from the example page 1 XenoCanto API query response.
    example_result_page_page_2 : ResultPage
        The ResultPage object created from the example page 2 XenoCanto API query response.

    Returns
    -------
    QueryResult
        The constructed two-page QueryResult object.
    """

    # Build the resultpages
    result_pages: List[ResultPage] = []
    result_pages.append(example_result_page_page_1)
    result_pages.append(example_result_page_page_2)

    return QueryResult(example_query_metadata_page_1, result_pages)
