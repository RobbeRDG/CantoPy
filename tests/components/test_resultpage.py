import json

from cantopy import ResultPage


def test_resultpage_init():
    """Test for the initialisation of a ResultPage object from a dict returned by the XenoCanto API"""
    # Open the example XenoCanto query response
    with open(
        "tests/test_resources/xenocanto_query_response.json", "r", encoding="utf-8"
    ) as file:
        query_response = json.load(file)
    result_page = ResultPage(query_response)

    # Test page attribute
    assert result_page.page == 5

    # Just check if recording is also set,
    # but more detailed recording evaluation is in the Recording test section
    assert len(result_page.recordings) == 3
    assert result_page.recordings[0].id == 581412
