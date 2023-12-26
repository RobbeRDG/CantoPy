from cantopy import ResultPage
import pytest

from components.query_result import QueryResult


@pytest.mark.parametrize(
    "example_queryresult_fixture_name, expected_num_pages",
    [
        ("example_single_page_queryresult", 1),
        ("example_three_page_queryresult", 3),
    ],
)
def test_query_result_initialization(
    example_queryresult_fixture_name: str,
    expected_num_pages: int,
    example_result_page: ResultPage,
    request: pytest.FixtureRequest,
):
    """Test the initialization of a QueryResult object.

    Parameters
    ----------
    example_queryresult_fixture_name : str
        Fixture name of the example QueryResult object based on the example XenoCanto API response.
    expected_num_pages : int
        Expected number of ResultPage instances in the QueryResult object.
    example_result_page : ResultPage
        Example ResultPage object based on the example XenoCanto API response.
    request : pytest.FixtureRequest
        Request fixture to get the example QueryResult object.
    """
    example_queryresult: QueryResult = request.getfixturevalue(
        example_queryresult_fixture_name
    )

    # Check attributes
    assert example_queryresult.available_num_recordings == 67810
    assert example_queryresult.available_num_species == 1675
    assert example_queryresult.available_num_pages == 136

    # Check stored result pages
    assert len(example_queryresult.result_pages) == expected_num_pages
    assert example_queryresult.result_pages[0] == example_result_page


@pytest.mark.parametrize(
    "example_queryresult_fixture_name",
    [
        ("example_single_page_queryresult"),
        ("example_three_page_queryresult"),
    ],
)
def test_query_result_get_all_recordings(
    example_queryresult_fixture_name: str,
    example_result_page: ResultPage,
    request: pytest.FixtureRequest,
):
    """Test the QueryResult's functionality to return all the contained recordings across ResultPages.

    Parameters
    ----------
    example_queryresult_fixture_name : str
        Fixture name of the example QueryResult object based on the example XenoCanto API response.
    example_result_page : ResultPage
        Example ResultPage object based on the example XenoCanto API response.
    request : pytest.FixtureRequest
        Request fixture to get the example QueryResult object.
    """

    example_queryresult: QueryResult = request.getfixturevalue(
        example_queryresult_fixture_name
    )

    # Get all the recordings contained in the example_queryresult
    recordings_list = example_queryresult.get_all_recordings()

    # In the provided query result instance, a single example result page instance gets repeated
    # for the amount of needed result pages.
    # This thus means that the correct total number of recordings that should be returned
    # is equal to the amount of result pages times the amount of recordings in the ResultPage instance.
    num_recordings = len(example_queryresult.result_pages) * len(
        example_result_page.recordings
    )
    assert len(recordings_list) == num_recordings

    # The specific recordings should thus also be a repeating sequence of the recordings
    # in the example result page instance.
    for i in range(0, len(example_queryresult.result_pages)):
        for j in range(0, len(example_result_page.recordings)):
            assert (
                recordings_list[i * len(example_result_page.recordings) + j]
                == example_result_page.recordings[j]
            )
