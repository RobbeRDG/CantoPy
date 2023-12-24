from cantopy import Recording

def test_recording_init(example_recording: Recording):
    """Test for the initialisation of a Recording object.

    Parameters
    ----------
    example_recording : Recording
        A Recording object based on the example XenoCanto API query response.
    """

    # See if all recording fields are captured
    assert example_recording.id == 581412
    assert example_recording.gen == "Odontophorus"
    assert example_recording.sp == "capueira"
    assert example_recording.ssp == "plumbeicollis"
    assert example_recording.group == "birds"
    assert example_recording.en == "Spot-winged Wood Quail"
    assert example_recording.rec == "Ciro Albano"
    assert example_recording.cnt == "Brazil"
    assert example_recording.loc == "RPPN Serra Bonita, Camacan-BA, Bahia"
    assert example_recording.lat == -15.3915
    assert example_recording.lng == -39.5643
    assert example_recording.song_type == "duet, song"
    assert example_recording.sex == "female, male"
    assert example_recording.stage == "adult"
    assert example_recording.method == "field recording"
    assert example_recording.url == "//xeno-canto.org/581412"
    assert example_recording.file == "https://xeno-canto.org/581412/download"
    assert (
        example_recording.file_name
        == "XC581412-Odontophorus capueira _Serra Bonita_20200802-074609.mp3"
    )
    assert example_recording.sono == {
        "small": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/ffts/XC581412-small.png",
        "med": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/ffts/XC581412-med.png",
        "large": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/ffts/XC581412-large.png",
        "full": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/ffts/XC581412-full.png",
    }
    assert example_recording.osci == {
        "small": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/wave/XC581412-small.png",
        "med": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/wave/XC581412-med.png",
        "large": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/wave/XC581412-large.png",
    }
    assert example_recording.lic == "//creativecommons.org/licenses/by-nc-sa/4.0/"
    assert example_recording.q == "A"
    assert example_recording.length.seconds == 194
    assert example_recording.timestamp.strftime("%Y-%m-%d %X") == "2020-08-02 08:00:00"
    assert example_recording.uploaded.strftime("%Y-%m-%d") == "2020-08-09"
    assert example_recording.also == ["Sclerurus scansor"]
    assert example_recording.rmk == ""
    assert example_recording.animal_seen == "yes"
    assert example_recording.playback_used == "yes"
    assert example_recording.regnr == ""
    assert example_recording.auto == "no"
    assert example_recording.dvc == ""
    assert example_recording.mic == ""
    assert example_recording.smp == 48000
