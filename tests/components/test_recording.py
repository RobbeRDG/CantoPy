import json

from cantopy import Recording


def test_recording_init():
    """Test for the initialisation of a Recording object from a dict returned by the XenoCanto API"""
    # Open the example XenoCanto query response and extract the first recording only
    with open(
        "tests/test_resources/xenocanto_query_response.json", "r", encoding="utf-8"
    ) as file:
        query_response_recording = json.load(file)["recordings"][0]
    recording = Recording(query_response_recording)

    # See if all recording fields are captured
    assert recording.id == 581412
    assert recording.gen == "Odontophorus"
    assert recording.sp == "capueira"
    assert recording.ssp == "plumbeicollis"
    assert recording.group == "birds"
    assert recording.en == "Spot-winged Wood Quail"
    assert recording.rec == "Ciro Albano"
    assert recording.cnt == "Brazil"
    assert recording.loc == "RPPN Serra Bonita, Camacan-BA, Bahia"
    assert recording.lat == -15.3915
    assert recording.lng == -39.5643
    assert recording.song_type == "duet, song"
    assert recording.sex == "female, male"
    assert recording.stage == "adult"
    assert recording.method == "field recording"
    assert recording.url == "//xeno-canto.org/581412"
    assert recording.file == "https://xeno-canto.org/581412/download"
    assert (
        recording.file_name
        == "XC581412-Odontophorus capueira _Serra Bonita_20200802-074609.mp3"
    )
    assert recording.sono == {
        "small": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/ffts/XC581412-small.png",
        "med": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/ffts/XC581412-med.png",
        "large": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/ffts/XC581412-large.png",
        "full": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/ffts/XC581412-full.png",
    }
    assert recording.osci == {
        "small": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/wave/XC581412-small.png",
        "med": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/wave/XC581412-med.png",
        "large": "//xeno-canto.org/sounds/uploaded/MXVQPUKGWW/wave/XC581412-large.png",
    }
    assert recording.lic == "//creativecommons.org/licenses/by-nc-sa/4.0/"
    assert recording.q == "A"
    assert recording.length.seconds == 194
    assert recording.timestamp.strftime("%Y-%m-%d %X") == "2020-08-02 08:00:00"
    assert recording.uploaded.strftime("%Y-%m-%d") == "2020-08-09"
    assert recording.also == ["Sclerurus scansor"]
    assert recording.rmk == ""
    assert recording.animal_seen == "yes"
    assert recording.playback_used == "yes"
    assert recording.regnr == ""
    assert recording.auto == "no"
    assert recording.dvc == ""
    assert recording.mic == ""
    assert recording.smp == 48000
