from cgitb import reset
from typing import Dict, List
from cantopy.components.query_result import QueryResult
from cantopy.components.recording import Recording
from os.path import exists, join
import pandas as pd


class DownloadManager:
    """A helper class for downloading the retrieved recordings from the XenoCanto APi."""

    def __init__(self, data_base_path: str):
        """Init a DownloadManager instance

        Parameters
        ----------
        data_base_path : str
            The base data folder where we want our download manager to store the downloaded files.
        """
        self.data_base_path = data_base_path

    def download_all_recordings_in_queryresult(self, query_result: QueryResult):
        """Download all the recordings contained in the provided QueryResult.

        Parameters
        ----------
        query_result : QueryResult
            The QueryResult instance containing the recordings we want to download.
        """

        # Get all the recordings from the query result
        recordings = query_result.get_all_recordings()

        # First detect the recordings that are already downloaded
        detected_already_downloaded_recordings = (
            self._detect_already_downloaded_recordings(recordings)
        )

        # Download the not-already-downloaded recordings
        not_already_downloaded_recordings = filter(
            lambda x: detected_already_downloaded_recordings[str(x.recording_id)]
            == "new",
            recordings,
        )
        download_pass_or_fail = self._download_recordings(
            not_already_downloaded_recordings
        )

        # Generate the metadata dataframe for the downloaded recordings
        downloaded_recordings_metadata = self._generate_downloaded_recordings_metadata(
            not_already_downloaded_recordings,
            download_pass_or_fail,
        )

        # Udate the metadata file of each one of the downloaded animals
        self._update_animal_recordings_metadata_files(downloaded_recordings_metadata)

    def _update_animal_recordings_metadata_files(
        self, downloaded_recordings_metadata: pd.DataFrame
    ):
        # Get the list of animals
        animals = downloaded_recordings_metadata["english_name"].unique()  # type: ignore

        # For each animal, update its metadata file
        for animal in animals:
            # Get the animal folder name
            animal_folder_name = self._generate_animal_folder_name(animal)

            # Get the animal metadata file path
            animal_metadata_file_path = join(
                self.data_base_path,
                animal_folder_name,
                f"{animal_folder_name}_recording_metadata.csv",
            )

            # Get the animal metadata file
            animal_metadata = pd.read_csv(animal_metadata_file_path)  # type: ignore

            # Append the new metadata to the animal metadata file
            animal_metadata = pd.concat(  # type: ignore
                [
                    animal_metadata,
                    downloaded_recordings_metadata[
                        downloaded_recordings_metadata["english_name"] == animal
                    ],  # type: ignore
                ],
                ignore_index=True,
            )

            # Sort the animal metadata file by recording id
            animal_metadata = animal_metadata.sort_values(by=["recording_id"])  # type: ignore

            # Update the animal metadata file
            animal_metadata.to_csv(animal_metadata_file_path, index=False)

    def _detect_already_downloaded_recordings(
        self, recordings: List[Recording]
    ) -> Dict[str, str]:
        """Detect the recordings that are already downloaded in the data folder.

        Parameters
        ----------
        recordings : List[Recording]
            The list of recordings we want to check for already downloaded recordings.

        Returns
        -------
        Dict[str, str]
            A dictionary containing the input recording ids as keys and their downloaded status as values
            ("already_downloaded" or "new").
        """
        detected_already_downloaded_recordings: Dict[str, str] = {}

        for recording in recordings:
            species_folder_name = self._generate_animal_folder_name(
                recording.english_name
            )
            # Generate the path where the recording should be located
            recording_path = join(
                self.data_base_path,
                species_folder_name,
                f"{recording.recording_id}.mp3",
            )

            if exists(recording_path):
                detected_already_downloaded_recordings[
                    str(recording.recording_id)
                ] = "already_downloaded"
            else:
                detected_already_downloaded_recordings[
                    str(recording.recording_id)
                ] = "new"

        return detected_already_downloaded_recordings

    def _generate_downloaded_recordings_metadata(
        self, recordings: List[Recording], download_pass_or_fail: Dict[str, str]
    ) -> pd.DataFrame:
        """Generate the metadata dataframe for the downloaded recordings.

        Parameters
        ----------
        recordings : List[Recording]
            The list of recordings we want to generate the metadata dataframe for.
        download_pass_or_fail : Dict[str, str]
            A dictionary containing the downloaded status of each recording ("pass" or "fail").

        Returns
        -------
        pd.DataFrame
            The metadata dataframe for the downloaded recordings.
        """

        downloaded_recording_metadata = pd.DataFrame({})

        for recording in recordings:
            # Only generate recording information for downloaded recordings
            if download_pass_or_fail[str(recording.recording_id)] == "pass":
                downloaded_recording_metadata = pd.concat([downloaded_recording_metadata, recording.to_dataframe_row()])  # type: ignore

        return downloaded_recording_metadata

    def _generate_animal_folder_name(self, animal_english_name: str) -> str:
        """Generate the download folder name for the animal recordings based on their english name.

        Parameters
        ----------
        animal_english_name : str
            The english name of the animal.

        Returns
        -------
        str
            The generated download folder name for the animal recordings.
        """
        # To lowercase
        animal_folder_name = animal_english_name.lower()

        # Remove spaces
        animal_folder_name = animal_folder_name.replace(" ", "_")

        # Remove special characters
        animal_folder_name = animal_folder_name.replace("-", "_")

        return animal_folder_name
