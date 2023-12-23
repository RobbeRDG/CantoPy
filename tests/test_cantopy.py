from cantopy import CantoPy, Query

cantopy = CantoPy()


def test_query_singlepage():
    "Test a single page fetch to the XenoCanto API"

    # Send a simple query
    query = Query(name="common blackbird", q="A")
    query_result = cantopy.send_query(query)

    # See if the ResultPage object contain the requested information
    assert len(query_result.result_pages) == 1
    assert query_result.result_pages[0].recordings[0].en == "Common Blackbird"
    assert query_result.result_pages[0].recordings[0].q == "A"


def test_query_multipage():
    "Test a multi (three) page fetch to the XenoCanto API"
    # Send a simple query
    query = Query(name="common blackbird", q="A")
    query_result = cantopy.send_query(query, max_pages=3)

    # See if the ResultPage object contain the requested information
    assert len(query_result.result_pages) == 3
    assert query_result.result_pages[0].recordings[0].en == "Common Blackbird"
    assert query_result.result_pages[0].recordings[0].q == "A"
