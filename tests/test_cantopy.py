from cantopy import CantoPy, Query

cantopy = CantoPy()


def test_query_singlepage():
    # Send a simple query
    query = Query(name="common blackbird", q="A")
    results = cantopy.send_query(query)

    # See if the QueryResult object contain the requested information
    assert len(results) == 1  # We only requested a single page
    assert results[0].recordings[0].en == "Common Blackbird"
    assert results[0].recordings[0].q == "A"
