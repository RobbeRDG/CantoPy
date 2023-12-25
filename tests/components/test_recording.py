from cantopy import Recording


def test_recording_init(example_recording: Recording):
    """Test for the initialization of a Recording object.

    Parameters
    ----------
    example_recording : Recording
        A Recording object based on the example XenoCanto API query response.
    """

    # See if all recording fields are captured
    assert example_recording.recording_id == 581412
    assert example_recording.generic_name == "Odontophorus"
    assert example_recording.specific_name == "capueira"
    assert example_recording.subspecies_name == "plumbeicollis"
    assert example_recording.species_group == "birds"
    assert example_recording.english_name == "Spot-winged Wood Quail"
    assert example_recording.recordist_name == "Ciro Albano"
    assert example_recording.country == "Brazil"
    assert example_recording.locality_name == "RPPN Serra Bonita, Camacan-BA, Bahia"
    assert example_recording.latitude == -15.3915
    assert example_recording.longitude == -39.5643
    assert example_recording.sound_type == "duet, song"
    assert example_recording.sex == "female, male"
    assert example_recording.life_stage == "adult"
    assert example_recording.recording_method == "field recording"
    assert example_recording.recording_url == "//xeno-canto.org/581412"
    assert example_recording.audio_file_url == "https://xeno-canto.org/581412/download"
    assert (
        example_recording.license_url == "//creativecommons.org/licenses/by-nc-sa/4.0/"
    )
    assert example_recording.quality_rating == "A"
    assert example_recording.recording_length.seconds == 194
    assert (
        example_recording.recording_timestamp.strftime("%Y-%m-%d %X")
        == "2020-08-02 08:00:00"
    )
    assert example_recording.upload_timestamp.strftime("%Y-%m-%d") == "2020-08-09"
    assert example_recording.background_species == ["Sclerurus scansor"]
    assert example_recording.recordist_remarks == ""
    assert example_recording.animal_seen == "yes"
    assert example_recording.playback_used == "yes"
    assert example_recording.automatic_recording == "no"
    assert example_recording.recording_device == ""
    assert example_recording.microphone_used == ""
    assert example_recording.sample_rate == 48000


def test_to_dataframe_row(example_recording: Recording):
    # Build the recording dataframe row
    example_recording_df_row = example_recording.to_dataframe_row()

    # test if the dataframe row contains the correct information
    assert example_recording_df_row["recording_id"] == 581412
    assert example_recording_df_row["generic_name"] == "Odontophorus"
    assert example_recording_df_row["specific_name"] == "capueira"
    assert example_recording_df_row["subspecies_name"] == "plumbeicollis"
    assert example_recording_df_row["species_group"] == "birds"
    assert example_recording_df_row["english_name"] == "Spot-winged Wood Quail"
    assert example_recording_df_row["recordist_name"] == "Ciro Albano"
    assert example_recording_df_row["country"] == "Brazil"
    assert (
        example_recording_df_row["locality_name"]
        == "RPPN Serra Bonita, Camacan-BA, Bahia"
    )
    assert example_recording_df_row["latitude"] == -15.3915
    assert example_recording_df_row["longitude"] == -39.5643
    assert example_recording_df_row["sound_type"] == "duet, song"
    assert example_recording_df_row["sex"] == "male, female"
    assert example_recording_df_row["life_stage"] == "adult"
    assert example_recording_df_row["recording_method"] == "field recording"
    assert example_recording_df_row["recording_url"] == "//xeno-canto.org/581412"
    assert (
        example_recording_df_row["audio_file_url"]
        == "https://xeno-canto.org/581412/download"
    )
    assert (
        example_recording_df_row["license_url"]
        == "//creativecommons.org/licenses/by-nc-sa/4.0/"
    )
    assert example_recording_df_row["quality_rating"] == "A"
    assert example_recording_df_row["recording_length"] == 194
    assert example_recording_df_row["recording_timestamp"] == "2020-08-02 08:00:00"
    assert example_recording_df_row["upload_timestamp"] == "2020-08-09"
    assert example_recording_df_row["background_species"] == ["Sclerurus scansor"]
    assert example_recording_df_row["recordist_remarks"] == ""
    assert example_recording_df_row["animal_seen"] == "yes"
    assert example_recording_df_row["playback_used"] == "yes"
    assert example_recording_df_row["automatic_recording"] == "no"
    assert example_recording_df_row["recording_device"] == ""
    assert example_recording_df_row["microphone_used"] == ""
    assert example_recording_df_row["sample_rate"] == 48000
