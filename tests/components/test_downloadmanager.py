from typing import Any, Generator

import shutil
from cantopy import DownloadManager, QueryResult
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
def partially_filled_download_data_base_path() -> Generator[str, Any, Any]:
    """Logic for setting up and breaking down a new partially-filled data folder.

    Upon creation, this folder will already contain part of the recordings returned by
    the example XenoCanto API response. This new folder has the following structure:
    |- folder_root
    |---- spot-winged_wood_quail
    |------- 581411.mp3
    |------- spot-winged_wood_quail_recording_metadata.csv

    Yields
    ------
    Generator[str, Any, Any]
        Return the string path to the newly created partially-filled data folder.
    """
    # Pre-execution configuration
    partially_filled_data_base_path = join(
        TEST_DATA_BASE_FOLDER_PATH, "partially_filled_test_data_folder"
    )
    os.mkdir(partially_filled_data_base_path)

    # Partially fill the newly created folder
    os.mkdir(join(partially_filled_data_base_path, "spot-winged_wood_quail"))
    open(
        join(partially_filled_data_base_path, "spot-winged_wood_quail", "581411.mp3"),
        "w",
    )
    open(
        join(
            partially_filled_data_base_path,
            "spot-winged_wood_quail",
            "winged_wood_quail_recording_metadata.csv",
        ),
        "w",
    )

    yield partially_filled_data_base_path

    # After exectution cleanup
    shutil.rmtree(partially_filled_data_base_path)


@pytest.fixture
def empty_data_folder_download_manager(empty_download_data_base_path: str):
    """Build a DownloadManager instance with its download folder set to a new empty folder.

    Parameters
    ----------
    empty_download_data_base_path : str
        The path to a newly created empty download folder.

    Returns
    -------
    DownloadManager
        The created DownloadManager instance.
    """
    return DownloadManager(empty_download_data_base_path)


@pytest.fixture
def partially_filled_data_folder_download_manager(
    partially_filled_download_data_base_path: str,
):
    """Build a DownloadManager instance with its download folder set a partially-filled data folder.

    Parameters
    ----------
    partially_filled_download_data_base_path : str
        The path to a newly created but partially-filled data folder.

    Returns
    -------
    DownloadManager
        The created DownloadManager instance.
    """
    return DownloadManager(partially_filled_download_data_base_path)


@pytest.fixture
def fake_data_folder_download_manager():
    """Build a DownloadManager instance with its download folder set to a fake/non-existant
    download folder. This DownloadManager instance can be used when we don't need to
    test any file storage functionality of this class.

    Returns
    -------
    DownloadManager
        The created DownloadManager instance.
    """
    return DownloadManager("fake/path")


def test_downloadmanager_download(
    empty_download_data_base_path: str,
    empty_data_folder_download_manager: DownloadManager,
    example_single_page_queryresult: QueryResult,
):
    """Test the DownloadManager functionality for donwloading QueryResult
    in an empty folder.

    Parameters
    ----------
    empty_download_data_base_path : str
        Empty forlder for storing the test downloaded data.
    empty_data_folder_download_manager : DownloadManager
        DownloadManager configured with the "empty_download_data_base_path" as download path.
    example_single_page_queryresult : QueryResult
        Single-page QueryResult object based on the example XenoCanto API query response
        containing the information that needs to be downloaded.
    """
    # Run the download functionality on a single page
    empty_data_folder_download_manager._download_recordings(
        example_single_page_queryresult.get_all_recordings()
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


def test_downloadmanager_detect_already_donwloaded_recordings(
    partially_filled_data_folder_download_manager: DownloadManager,
    example_single_page_queryresult: QueryResult,
):
    """Test the detection of already downloaded recordings for the DownloadManager.

    Parameters
    ----------
    partially_filled_data_folder_download_manager : DownloadManager
        DownloadManager instance set to a partially-filled data folder.
    example_single_page_queryresult : QueryResult
        Single-page QueryResult object based on the example XenoCanto API query response.
    """
    detected_already_downloaded_recordings = partially_filled_data_folder_download_manager._detect_already_downloaded_recordings(
        example_single_page_queryresult.get_all_recordings()
    )

    # Check if the already downloaded recordings have been detected correctly
    assert len(detected_already_downloaded_recordings.keys()) == 3
    assert detected_already_downloaded_recordings["581412"] == "new"
    assert detected_already_downloaded_recordings["581411"] == "already_downloaded"
    assert detected_already_downloaded_recordings["427716"] == "new"


def test_downloadmanager_downloaeded_recording_metadata_generation(
    fake_data_folder_download_manager: DownloadManager,
    example_single_page_queryresult: QueryResult,
):
    """Test the downloaded recording metadata generation procedure for the DownloadManager
    class.

    Parameters
    ----------
    fake_data_folder_download_manager : DownloadManager
        DownloadManager instance set to a non-existant path, since we won't be downloading anything.
    example_single_page_queryresult : QueryResult
        Single-page QueryResult object based on the example XenoCanto API query response
        containing the recordings for which we want to generate the downloaded
        recording metadata information.
    """
    # The provided example_page_queryresult contains 3 recordings.
    # Lets simulate that after running the recording download logic, only recordings "581412"
    # and "427716" were downloaded, with the download of recording "581411" resulting in an error.
    # This would thus return a download_pass_or_fail_dict in the form
    download_pass_or_fail = {"581412": "pass", "581411": "fail", "427716": "pass"}

    # Generate the metadata
    downloaded_recording_metadata = (
        fake_data_folder_download_manager._generate_downloaded_recording_metadata(
            example_single_page_queryresult.get_all_recordings(),
            download_pass_or_fail,
        )
    )

    # Since we only want to generate the metadata for the recordings that have indeed
    # been downloaded, the returned metadata should only contain the metadata for records
    # with id "581412" and "427716" (which occupy indexes 0 and 2 in the
    # example_single_page_queryresult's recordings list)
    assert len(downloaded_recording_metadata) == 2
    assert (
        downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 581412
        ]
        == example_single_page_queryresult.result_pages[0]
        .recordings[0]
        .to_dataframe_row()
    )
    assert downloaded_recording_metadata.loc[
        downloaded_recording_metadata["recording_id"] == 581411
    ].empty()
    assert (
        downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 427716
        ]
        == example_single_page_queryresult.result_pages[0]
        .recordings[2]
        .to_dataframe_row()
    )


def test_downloadmanager_generate_animal_folder_name(
    fake_data_folder_download_manager: DownloadManager,
):
    """Test the generation of the animal folder name for the DownloadManager.

    Parameters
    ----------
    fake_data_folder_download_manager : DownloadManager
        DownloadManager instance set to a non-existant path, since we won't be downloading anything.
    """
    # Spaces should be replaced by "_"
    assert (
        fake_data_folder_download_manager._generate_animal_folder_name(
            "test with just spaces"
        )
        == "test_with_just_spaces"
    )

    # Everything should be lower case
    assert (
        fake_data_folder_download_manager._generate_animal_folder_name(
            "tEst CAPITAL Bird name"
        )
        == "test_capital_bird_name"
    )

    # Special chars
    assert (
        fake_data_folder_download_manager._generate_animal_folder_name(
            "black-winged bird"
        )
        == "black-winged_bird"
    )
