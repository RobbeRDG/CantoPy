from cantopy import ResultPage
import pytest


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
    example_queryresult : QueryResult
        A QueryResult object based on the example XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response.
    expected_num_pages : int
        The expected number of result pages.
    """
    example_queryresult = request.getfixturevalue(example_queryresult_fixture_name)

    # Check attributes
    assert example_queryresult.available_num_recordings == 67810
    assert example_queryresult.available_num_species == 1675
    assert example_queryresult.available_num_pages == 136

    # Check stored result pages
    assert len(example_queryresult.result_pages) == expected_num_pages
    assert example_queryresult.result_pages[0] == example_result_page
