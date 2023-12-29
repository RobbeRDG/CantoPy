from typing import Any, Generator, List

import shutil
from cantopy import DownloadManager, QueryResult
import os
from os.path import join
import pytest
import pandas as pd


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
    assert "spot_winged_wood_quail_recording_metadata.csv" in os.listdir(bird_folder)

    # TODO: wirte test for failed download


@pytest.mark.parametrize(
    "example_queryresult_fixture_name",
    [
        ("example_single_page_queryresult"),
        ("example_two_page_queryresult"),
    ],
)
def test_downloadmanager_detect_already_donwloaded_recordings(
    example_queryresult_fixture_name: str,
    partially_filled_data_folder_download_manager: DownloadManager,
    request: pytest.FixtureRequest,
):
    """Test the detection of already downloaded recordings for the DownloadManager.

    Parameters
    ----------
    example_queryresult_fixture_name : str
        Fixture name of the example QueryResult object based on the example XenoCanto API response.
    partially_filled_data_folder_download_manager : DownloadManager
        DownloadManager instance set to a partially-filled data folder.
    request : pytest.FixtureRequest
        Request fixture to get the example QueryResult object.
    """
    example_queryresult: QueryResult = request.getfixturevalue(
        example_queryresult_fixture_name
    )

    detected_already_downloaded_recordings = partially_filled_data_folder_download_manager._detect_already_downloaded_recordings(
        example_queryresult.get_all_recordings()
    )

    # Check if the already downloaded recordings have been detected correctly
    if example_queryresult_fixture_name == "example_single_page_queryresult":
        assert len(detected_already_downloaded_recordings.keys()) == 3
        assert detected_already_downloaded_recordings["581412"] == "new"
        assert detected_already_downloaded_recordings["581411"] == "already_downloaded"
        assert detected_already_downloaded_recordings["427716"] == "new"
    elif example_queryresult_fixture_name == "example_two_page_queryresult":
        assert len(detected_already_downloaded_recordings.keys()) == 6
        assert detected_already_downloaded_recordings["581412"] == "new"
        assert detected_already_downloaded_recordings["581411"] == "already_downloaded"
        assert detected_already_downloaded_recordings["427716"] == "new"
        assert detected_already_downloaded_recordings["220366"] == "new"
        assert detected_already_downloaded_recordings["220365"] == "already_downloaded"
        assert detected_already_downloaded_recordings["196385"] == "already_downloaded"


@pytest.mark.parametrize(
    "example_queryresult_fixture_name",
    [
        ("example_single_page_queryresult"),
        ("example_two_page_queryresult"),
    ],
)
def test_downloadmanager_generate_downloaeded_recording_metadata(
    example_queryresult_fixture_name: str,
    fake_data_folder_download_manager: DownloadManager,
    request: pytest.FixtureRequest,
):
    """Test the downloaded recording metadata generation procedure for the DownloadManager
    class.

    Parameters
    ----------
    example_queryresult_fixture_name : str
        Fixture name of the example QueryResult object based on the example XenoCanto API response.
        We want to generate the downloaded recording metadata information for the recordings
        contained in the QueryResult instance.
    fake_data_folder_download_manager : DownloadManager
        A DownloadManager instance set to a non-existant path, since we won't be downloading anything.
    request : pytest.FixtureRequest
        Request fixture to get the example QueryResult object.
    """

    # Create a pass fail dict containing some passed and failed recordings
    download_pass_or_fail = {}
    if example_queryresult_fixture_name == "example_single_page_queryresult":
        download_pass_or_fail["581412"] = "pass"
        download_pass_or_fail["581411"] = "fail"
        download_pass_or_fail["427716"] = "pass"
    elif example_queryresult_fixture_name == "example_two_page_queryresult":
        download_pass_or_fail["581412"] = "pass"
        download_pass_or_fail["581411"] = "fail"
        download_pass_or_fail["427716"] = "pass"
        download_pass_or_fail["220366"] = "fail"
        download_pass_or_fail["220365"] = "pass"
        download_pass_or_fail["196385"] = "pass"

    # Generate the metadata
    example_queryresult: QueryResult = request.getfixturevalue(
        example_queryresult_fixture_name
    )
    downloaded_recording_metadata = (
        fake_data_folder_download_manager._generate_downloaded_recordings_metadata(
            example_queryresult.get_all_recordings(),
            download_pass_or_fail,
        )
    )

    # We only want to generate the metadata for the recordings that have indeed
    if example_queryresult_fixture_name == "example_single_page_queryresult":
        assert len(downloaded_recording_metadata) == 2
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 581412  # type: ignore
        ].equals(example_queryresult.result_pages[0].recordings[0].to_dataframe_row())
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 581411
        ].empty
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 427716  # type: ignore
        ].equals(
            example_queryresult.result_pages[0].recordings[2].to_dataframe_row()  # type: ignore
        )
    elif example_queryresult_fixture_name == "example_two_page_queryresult":
        assert len(downloaded_recording_metadata) == 4
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 581412  # type: ignore
        ].equals(example_queryresult.result_pages[0].recordings[0].to_dataframe_row())
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 581411
        ].empty
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 427716  # type: ignore
        ].equals(example_queryresult.result_pages[0].recordings[2].to_dataframe_row())
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 220366
        ].empty
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 220365  # type: ignore
        ].equals(example_queryresult.result_pages[1].recordings[1].to_dataframe_row())
        assert downloaded_recording_metadata.loc[
            downloaded_recording_metadata["recording_id"] == 196385  # type: ignore
        ].equals(example_queryresult.result_pages[1].recordings[2].to_dataframe_row())


@pytest.mark.parametrize(
    "metadata_to_add_fixture_name",
    [
        ("spot_winged_wood_quail_to_add_test_recording_metadata"),
        ("little_nightjar_to_add_test_recording_metadata"),
        ("combined_to_add_test_recording_metadata"),
    ],
)
def test_downloadmanager_update_animal_recordings_metadata_files(
    partially_filled_data_folder_download_manager: DownloadManager,
    metadata_to_add_fixture_name: str,
    request: pytest.FixtureRequest,
    spot_winged_wood_quail_partial_test_recording_metadata: pd.DataFrame,
    spot_winged_wood_quail_full_test_recording_metadata: pd.DataFrame,
    little_nightjar_partial_test_recording_metadata: pd.DataFrame,
    little_nightjar_full_test_recording_metadata: pd.DataFrame,
):
    to_add_test_recording_metadata: pd.DataFrame = request.getfixturevalue(
        metadata_to_add_fixture_name
    )

    partially_filled_data_folder_download_manager._update_animal_recordings_metadata_files(
        to_add_test_recording_metadata
    )

    if (
        metadata_to_add_fixture_name
        == "spot_winged_wood_quail_to_add_test_recording_metadata"
    ):
        assert spot_winged_wood_quail_full_test_recording_metadata.equals(  # type: ignore
            pd.read_csv(  # type: ignore
                join(
                    partially_filled_data_folder_download_manager.data_base_path,
                    "spot_winged_wood_quail",
                    "spot_winged_wood_quail_recording_metadata.csv",
                )
            )
        )
        assert little_nightjar_partial_test_recording_metadata.equals(  # type: ignore
            pd.read_csv(  # type: ignore
                join(
                    partially_filled_data_folder_download_manager.data_base_path,
                    "little_nightjar",
                    "little_nightjar_recording_metadata.csv",
                )
            )
        )
    elif (
        metadata_to_add_fixture_name == "little_nightjar_to_add_test_recording_metadata"
    ):
        test = pd.read_csv(  # type: ignore
            join(
                partially_filled_data_folder_download_manager.data_base_path,
                "spot_winged_wood_quail",
                "spot_winged_wood_quail_recording_metadata.csv",
            )
        )
        assert spot_winged_wood_quail_partial_test_recording_metadata.equals(  # type: ignore
            pd.read_csv(  # type: ignore
                join(
                    partially_filled_data_folder_download_manager.data_base_path,
                    "spot_winged_wood_quail",
                    "spot_winged_wood_quail_recording_metadata.csv",
                )
            )
        )
        assert little_nightjar_full_test_recording_metadata.equals(  # type: ignore
            pd.read_csv(  # type: ignore
                join(
                    partially_filled_data_folder_download_manager.data_base_path,
                    "little_nightjar",
                    "little_nightjar_recording_metadata.csv",
                )
            )
        )
    elif metadata_to_add_fixture_name == "combined_to_add_test_recording_metadata":
        assert spot_winged_wood_quail_full_test_recording_metadata.equals(  # type: ignore
            pd.read_csv(  # type: ignore
                join(
                    partially_filled_data_folder_download_manager.data_base_path,
                    "spot_winged_wood_quail",
                    "spot_winged_wood_quail_recording_metadata.csv",
                )
            )
        )
        assert little_nightjar_full_test_recording_metadata.equals(  # type: ignore
            pd.read_csv(  # type: ignore
                join(
                    partially_filled_data_folder_download_manager.data_base_path,
                    "little_nightjar",
                    "little_nightjar_recording_metadata.csv",
                )
            )
        )


def test_downloadmanager_generate_animal_folder_name(
    fake_data_folder_download_manager: DownloadManager,
):
    """Test the generation functionality of the animal folder name in the DownloadManager.

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
        == "black_winged_bird"
    )
