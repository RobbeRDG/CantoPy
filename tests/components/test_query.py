from cantopy import Query


def test_to_string():
    """Test for the to_string method of the Query class"""
    query = Query(
        name="common blackbird",
        cnt="Netherlands",
        song_type="alarm call",
        stage="=adult",
        q=">C",
    )
    assert (
        query.to_string()
        == 'common blackbird+cnt:"Netherlands"+type:"alarm call"+stage:"=adult"+q:">C"'
    )
