from datetime import timedelta, datetime
from typing import Dict

import pandas as pd
from pandas import Timestamp


class Recording:
    """
    Wrapper for storing a single recording returned by the Xeno Canto API.

    Attributes
    ----------
    recording_id : int
        The recording id number of the recording on xeno-canto.
    generic_name : str
        Generic name of the species.
    specific_name : str
        Specific name (epithet) of the species.
    subspecies_name : str
        Subspecies name (subspecific epithet).
    species_group : str
        Group to which the species belongs (birds, grasshoppers, bats).
    english_name : str
        English name of the species.
    recordist_name : str
        Name of the recordist.
    country : str
        Country where the recording was made.
    locality_name : str
        Name of the locality.
    latitude : float
        Latitude of the recording in decimal coordinates.
    longitude : float
        Longitude of the recording in decimal coordinates.
    sound_type : str
        Sound type of the recording (combining both predefined terms such as 'call' or 'song'
        and additional free text options).
    sex : str
        Sex of the animal.
    life_stage : str
        Life stage of the animal (adult, juvenile, etc.).
    recording_method : str
        Recording method (field recording, in the hand, etc.).
    recording_url : str
        URL specifying the details of this recording.
    audio_file_url : str
        URL to the audio file.
    license_url : str
        URL describing the license of this recording.
    quality_rating : str
        Current quality rating for the recording.
    recording_length : timedelta
        Length of the recording in a timedelta.
    recording_timestamp : datetime
        Timestamp that the recording was made.
    upload_timestamp : datetime
        Date that the recording was uploaded to xeno-canto.
    background_species : list
        An array with the identified background species in the recording.
    recordist_remarks : str
        Additional remarks by the recordist.
    animal_seen : str
        Was the recorded animal seen?
    playback_used : str
        Was playback used to lure the animal?
    temperature : str
        Temperature during recording (applicable to specific groups only).

    automatic_recording : str
        Automatic (non-supervised) recording?
    recording_device : str
        Recording device used.
    microphone_used : str
        Microphone used.
    sample_rate : int
        Sample rate.

    Notes
    -----
    Currently, the recording class does not capture the following information also returned by the
    XenoCanto API:
    - file-name : Original file name of the audio file.
    - sono : An object with the URLs to the four versions of sonograms.
    - osci : An object with the URLs to the three versions of oscillograms.
    - regnr : Registration number of the specimen (when collected).

    """

    def __init__(self, recording_data: Dict[str, str]):
        """Create a Recording object with a given recording dict returned from the XenoCanto API

        Parameters
        ----------
        recording_data : Dict[str, str]
            The dict of the recording returned by the XenoCanto API
        """
        # Extract the recording length from the given string representation
        length_in_minutes = recording_data.get("length", "").split(":")
        recording_length = timedelta(
            minutes=int(length_in_minutes[0]), seconds=int(length_in_minutes[1])
        )

        # Extract the full timestamp from the given string representation
        recording_date = recording_data.get("date", "")
        recording_time = recording_data.get("time", "")

        # In some cases, a date is returned with the day value set to 0 (e.g. "2020-08-00")
        # In this case, set the day value to 1
        if recording_date.endswith("-00"):
            recording_date = recording_date[:-2] + "01"

        # Create a Timestamp object from the date and time
        recording_timestamp = (
            Timestamp(f"{recording_date}T{recording_time}")
            if not (recording_time == "?" or recording_time == "")  # If time is not set
            else Timestamp(recording_date)
        )

        # Extract the uploaded timestamp
        uploaded_timestamp = datetime.fromisoformat(recording_data.get("uploaded", ""))

        ####################################################################
        # Set the Recording object attributes
        ####################################################################

        # Id
        self.recording_id = int(recording_data.get("id", 0))

        # Animal information
        self.generic_name = recording_data.get("gen", "")
        self.specific_name = recording_data.get("sp", "")
        self.subspecies_name = recording_data.get("ssp", "")
        self.species_group = recording_data.get("group", "")
        self.english_name = recording_data.get("en", "")
        self.sound_type = recording_data.get("type", "")
        self.sex = recording_data.get("sex", "")
        self.life_stage = recording_data.get("stage", "")
        self.background_species = recording_data.get("also", "")
        self.animal_seen = recording_data.get("animal-seen", "")

        # Recording information
        self.recordist_name = recording_data.get("rec", "")
        self.recording_method = recording_data.get("method", "")
        self.license_url = recording_data.get("lic", "")
        self.quality_rating = recording_data.get("q", "")
        self.recording_length = recording_length
        self.recording_timestamp = recording_timestamp
        self.date = recording_data.get("date", "")
        self.upload_timestamp = uploaded_timestamp
        self.recording_url = recording_data.get("url", "")
        self.audio_file_url = recording_data.get("file", "")
        self.recordist_remarks = recording_data.get("rmk", "")
        self.playback_used = recording_data.get("playback-used", "")
        self.automatic_recording = recording_data.get("auto", "")
        self.recording_device = recording_data.get("dvc", "")
        self.microphone_used = recording_data.get("mic", "")
        self.sample_rate = (
            int(recording_data.get("smp", 0)) if recording_data.get("smp", 0) else 0
        )

        # Location information
        self.country = recording_data.get("cnt", "")
        self.locality_name = recording_data.get("loc", "")
        self.latitude = (
            float(recording_data.get("lat", ""))
            if recording_data.get("lat", "")
            else None
        )
        self.longitude = (
            float(recording_data.get("lng", ""))
            if recording_data.get("lng", "")
            else None
        )
        self.temperature = recording_data.get("temp", "")

    def to_dataframe_row(self) -> pd.DataFrame:
        """Convert the Recording object to a pandas DataFrame row.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame row containing the recording information.
        """

        data = {
            "recording_id": [self.recording_id],
            "generic_name": [self.generic_name],
            "specific_name": [self.specific_name],
            "subspecies_name": [self.subspecies_name],
            "species_group": [self.species_group],
            "english_name": [self.english_name],
            "sound_type": [self.sound_type],
            "sex": [self.sex],
            "life_stage": [self.life_stage],
            "background_species": [self.background_species],
            "animal_seen": [self.animal_seen],
            "recordist_name": [self.recordist_name],
            "recording_method": [self.recording_method],
            "license_url": [self.license_url],
            "quality_rating": [self.quality_rating],
            "recording_length": [self.recording_length],
            "recording_timestamp": [self.recording_timestamp],
            "date": [self.date],
            "upload_timestamp": [self.upload_timestamp],
            "recording_url": [self.recording_url],
            "audio_file_url": [self.audio_file_url],
            "recordist_remarks": [self.recordist_remarks],
            "playback_used": [self.playback_used],
            "automatic_recording": [self.automatic_recording],
            "recording_device": [self.recording_device],
            "microphone_used": [self.microphone_used],
            "sample_rate": [self.sample_rate],
            "country": [self.country],
            "locality_name": [self.locality_name],
            "latitude": [self.latitude],
            "longitude": [self.longitude],
            "temperature": [self.temperature],
        }

        return pd.DataFrame(data)
