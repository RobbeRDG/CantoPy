from cantopy import ResultPage
from components.query_result import QueryResult

def test_query_result_single_page(
    example_single_page_queryresult: QueryResult, example_result_page: ResultPage
):
    """Test the initialisation of a QueryResult object containing a single page.

    Parameters
    ----------
    example_single_page_queryresult : QueryResult
        A three-page QueryResult object based on the example XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response.
    """

    # Check attirbutes
    assert example_single_page_queryresult.available_num_recordings == 67810
    assert example_single_page_queryresult.available_num_species == 1675
    assert example_single_page_queryresult.available_num_pages == 136

    # Check stored result pages
    assert len(example_single_page_queryresult.result_pages) == 1
    assert example_single_page_queryresult.result_pages[0] == example_result_page


def test_query_result_multi_page(
    example_three_page_queryresult: QueryResult, example_result_page: ResultPage
):
    """Test the initialisation of a QueryResult object containing multiple pages (3 pages).

    Parameters
    ----------
    example_single_page_queryresult : QueryResult
        A three-page QueryResult object based on the example XenoCanto API query response.
    example_result_page : ResultPage
        The ResultPage object created from the example XenoCanto API query response.
    """

    # Check attirbutes
    assert example_three_page_queryresult.available_num_recordings == 67810
    assert example_three_page_queryresult.available_num_species == 1675
    assert example_three_page_queryresult.available_num_pages == 136

    # Check stored result pages
    assert len(example_three_page_queryresult.result_pages) == 3
    assert example_three_page_queryresult.result_pages[0] == example_result_page
