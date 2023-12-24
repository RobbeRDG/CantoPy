from typing import Dict
import pytest
import json


@pytest.fixture(scope="session")
def example_xenocanto_query_response() -> Dict[str, str | Dict[str, str]]:
    """Build an example query response of the XenoCanto API.

    Returns
    -------
    Dict[str, str]
        The dictionary representation of an example query response of the XenoCanto API.
    """

    # Open the example XenoCanto query response
    with open(
        "resources/test_resources/example_xenocanto_query_response.json", "r", encoding="utf-8"
    ) as file:
        return json.load(file)

