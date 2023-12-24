import pytest
from cantopy import Query

@pytest.fixture
def query() -> Query:
    """Build a simple Query object.

    Returns
    -------
    Query
        An example Query object.
    """
    return Query(
        name="common blackbird",
        cnt="Netherlands",
        song_type="alarm call",
        stage="=adult",
        q=">C",
    )

def test_to_string(query: Query):
    """Test the to_string method of the Query class.

    Parameters
    ----------
    query : Query
        The Query object to test the to_string method on.
    """
    assert (
        query.to_string()
        == 'common blackbird+cnt:"Netherlands"+type:"alarm call"+stage:"=adult"+q:">C"'
    )
