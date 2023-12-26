from cantopy import ResultPage

def test_resultpage_init(example_result_page: ResultPage):
    """Test for the initialisation of a ResultPage object.

    Parameters
    ----------
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response
    """

    # Test page attribute
    assert example_result_page.page == 5

    # Just check if recording is also set,
    # but more detailed recording evaluation is in the Recording test section
    assert len(example_result_page.recordings) == 3
    assert example_result_page.recordings[0].recording_id == 581412
