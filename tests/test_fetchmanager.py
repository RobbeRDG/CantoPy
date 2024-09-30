import pytest
from cantopy import FetchManager
from cantopy.xenocanto_components import Query


@pytest.fixture
def fetch_manager():
    return FetchManager()


@pytest.fixture
def query():
    return Query(species_name="common blackbird", quality="A")


@pytest.fixture
def complex_query():
    """A complex query instances with both operators and spaces in the attribute values.

    In this case, an operator is incorporated in the life_stage attribute and the spaces
    are in the species_name and song_type attributes. These types of attributes are
    usually enclosed in double quotes to avoid issues with the XenoCanto API (this
    however does require the provided argument values to be enclosed in single quotes).

    """
    return Query(
        species_name="common blackbird",
        country="Netherlands",
        song_type='"alarm call"',
        life_stage='"=adult"',
    )


@pytest.mark.parametrize("query_fixture_id", ["query", "complex_query"])
def test_query_singlepage(fetch_manager: FetchManager, query_fixture_id: str, request):
    """Test a single page fetch to the XenoCanto API."""

    # Get the query object
    query = request.getfixturevalue(query_fixture_id)

    # Send a simple query
    query_result = fetch_manager.send_query(query)

    # See if the ResultPage object contain the requested information
    assert len(query_result.result_pages) == 1
    assert query_result.result_pages[0].recordings[0].english_name == "Common Blackbird"
    assert query_result.result_pages[0].recordings[0].quality_rating == "A"


def test_query_multipage(fetch_manager: FetchManager, query: Query):
    """Test a multi (3) page fetch to the XenoCanto API.

    Parameters
    ----------
    fetch_manager : FetchManager
        An instance of the FetchManager class.
    query : Query
        The Query object to send to the XenoCanto API.
    """

    # Send a simple query
    query_result = fetch_manager.send_query(query, max_pages=3)

    # See if the ResultPage object contain the requested information
    assert len(query_result.result_pages) == 3
    assert query_result.result_pages[0].recordings[0].english_name == "Common Blackbird"
    assert query_result.result_pages[0].recordings[0].quality_rating == "A"
