from typing import Any, Generator, List

import shutil
from cantopy import DownloadManager, QueryResult, ResultPage
import json
import os
from os.path import join
import pytest

TEST_DATA_BASE_FOLDER_PATH = (
    "/workspaces/CantoPy/resources/test_resources/test_data_folders"
)

@pytest.fixture
def empty_download_data_base_path() -> Generator[str, Any, Any]:
    """Logic for setting up and breaking down a new empty data folder.

    Yields
    ------
    Generator[str, Any, Any]
        Return the string path to the newly created empty data folder.
    """
    # Pre-execution configuration
    empty_download_data_base_path = join(
        TEST_DATA_BASE_FOLDER_PATH, "empty_test_data_folder"
    )
    os.mkdir(empty_download_data_base_path)

    yield empty_download_data_base_path

    # After exectution cleanup
    shutil.rmtree(empty_download_data_base_path)


@pytest.fixture
def empty_data_folder_download_manager(empty_download_data_base_path: str):
    """Build a DownloadManager instance with its download folder set to a new empty folder.

    Parameters
    ----------
    empty_download_data_base_path : str
        The path a newly created empty download folder.

    Returns
    -------
    DownloadManager
        The created DownloadManager instance.
    """
    return DownloadManager(empty_download_data_base_path)


@pytest.fixture
def single_page_query_result() -> QueryResult:
    """Build an example single-result page QueryResult object for testing the DownloadManager.

    Returns
    -------
    QueryResult
        The test QueryResult instance.
    """

    # Open the example XenoCanto query response
    with open(
        "resources/test_resources/xenocanto_query_response.json", "r", encoding="utf-8"
    ) as file:
        query_response = json.load(file)

    # Extract the metadata information of this query
    query_metadata = {
        "available_num_recordings": int(query_response["numRecordings"]),
        "available_num_species": int(query_response["numSpecies"]),
        "available_num_pages": int(query_response["numPages"]),
    }

    # Build the resultpage
    result_page = ResultPage(query_response)

    # Build a QueryResult
    return QueryResult(query_metadata, [result_page])


def test_downloadmanager_single_page_download(
    empty_download_data_base_path: str,
    empty_data_folder_download_manager: DownloadManager,
    single_page_query_result: QueryResult,
):
    # Run the download functionality on a single page
    empty_data_folder_download_manager.download_queryresult_files(
        single_page_query_result
    )

    # After download, we should have a new folder containing three recordings and a
    # recording metadata file in the format:
    # |- spot-winged_wood_quail
    # |---- 581412.mp3
    # |---- 581411.mp3
    # |---- 427716.mp3
    # |---- spot-winged_wood_quail_recording_metadata.csv

    assert len(os.listdir(empty_download_data_base_path)) == 1
    assert os.listdir(empty_download_data_base_path)[0] == "spot-winged_wood_quail"

    bird_folder = join(empty_download_data_base_path, "spot-winged_wood_quail")
    assert len(os.listdir(bird_folder)) == 3
    assert "581412.mp3" in os.listdir(bird_folder)
    assert "581411.mp3" in os.listdir(bird_folder)
    assert "427716.mp3" in os.listdir(bird_folder)
    assert "spot-winged_wood_quail_recording_metadata.csv" in os.listdir(bird_folder)


def test_downloadmanager_duplicate_download_removal():
    # TODO write
    assert False == True


def test_download_mannager_multi_thread():
    # TODO write
    assert False == True


def test_downloadmanager_metadata_generation():
    # TODO write
    assert False == True
