from cantopy import CantoPy, Query

cantopy = CantoPy()


def test_query_singlepage():
    "Test a single page fetch to the XenoCanto API"
    # Send a simple query
    query = Query(name="common blackbird", q="A")
    results = cantopy.send_query(query)

    # See if the ResultPage object contain the requested information
    assert len(results) == 1  # We only requested a single page
    assert results[0].recordings[0].en == "Common Blackbird"
    assert results[0].recordings[0].q == "A"

def test_query_multipage():
    "Test a multi (three) page fetch to the XenoCanto API"
    # Send a simple query
    query = Query(name="common blackbird", q="A")
    results = cantopy.send_query(query, max_pages=3)

    # See if the ResultPage object contain the requested information
    assert len(results) == 3 # We requested three pages
    assert results[0].recordings[0].en == "Common Blackbird"
    assert results[0].recordings[0].q == "A"
