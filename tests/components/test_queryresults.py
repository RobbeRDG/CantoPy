import json

from src.cantopy.components.query_result import QueryResult


def test_queryresult_init():
    """Test for the initialisation of a QueryResult object from a dict returned by the XenoCanto API"""
    # Open the example XenoCanto query response
    with open(
        "tests/test_resources/xenocanto_query_response.json", "r", encoding="utf-8"
    ) as file:
        query_response = json.load(file)
    query_result = QueryResult(query_response)

    assert query_result.num_recordings == 67810
    assert query_result.num_species == 1675
    assert query_result.page == 5
    assert query_result.num_pages == 136

    # Just check if recording is also set,
    # but more detailed recording evaluation is in the Recording test section
    assert len(query_result.recordings) == 3
    assert query_result.recordings[0].id == 581412
