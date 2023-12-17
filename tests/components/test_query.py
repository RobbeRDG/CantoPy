from cantopy import Query


def test_to_string():
    """Test for the initialisation of a QueryResult object from a dict returned by the XenoCanto API"""
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
