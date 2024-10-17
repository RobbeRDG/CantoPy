import pytest
from cantopy.xenocanto_components import Query


@pytest.fixture
def query_for_tostring_test() -> Query:
    """Build a simple Query object.

    Returns
    -------
    Query
        An example Query object.
    """
    return Query(
        species_name="common blackbird",
        country="Netherlands",
        song_type='"alarm call"',
        life_stage='"=adult"',
        quality='">C"',
    )


def test_to_string(query_for_tostring_test: Query):
    """Test the to_string method of the Query class.

    Parameters
    ----------
    query_for_tostring_test
        The Query object to test the to_string method on.
    """
    assert (
        query_for_tostring_test.to_string()
        == 'common blackbird cnt:Netherlands type:"alarm call" stage:"=adult" q:">C"'
    )
