import json

from src.cantopy.components.recording import Recording


def test_recording_init():
    # Open the example XenoCanto query response and extract the first recording only
    query_response_recording_json = json.load(
        "tests/test_resources/xenocanto_query_response.json"
    )["recordings"][0]
    recording = Recording(query_response_recording_json)

    # See if all recording fields are captured
    assert recording
