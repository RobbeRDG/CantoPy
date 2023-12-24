from typing import Dict

import pytest

from cantopy import ResultPage


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


def test_resultpage_init(example_result_page: ResultPage):
    """Test for the initialisation of a ResultPage object.

    Parameters
    ----------
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response
    """

    # Test page attribute
    assert example_result_page.page == 5

    # Just check if recording is also set,
    # but more detailed recording evaluation is in the Recording test section
    assert len(example_result_page.recordings) == 3
    assert example_result_page.recordings[0].id == 581412
