class Recording:
    """
    Class representing a recording object.

    Attributes
    ----------
    id : str
        Catalogue number of the recording on xeno-canto.
    gen : str
        Generic name of the species.
    sp : str
        Specific name (epithet) of the species.
    ssp : str
        Subspecies name (subspecific epithet).
    group : str
        Group to which the species belongs (birds, grasshoppers, bats).
    en : str
        English name of the species.
    rec : str
        Name of the recordist.
    cnt : str
        Country where the recording was made.
    loc : str
        Name of the locality.
    lat : float
        Latitude of the recording in decimal coordinates.
    lng : float
        Longitude of the recording in decimal coordinates.
    type : str
        Sound type of the recording (combining both predefined terms such as 'call' or 'song'
        and additional free text options).
    sex : str
        Sex of the animal.
    stage : str
        Life stage of the animal (adult, juvenile, etc.).
    method : str
        Recording method (field recording, in the hand, etc.).
    url : str
        URL specifying the details of this recording.
    file : str
        URL to the audio file.
    file_name : str
        Original file name of the audio file.
    sono : dict
        An object with the URLs to the four versions of sonograms.
    osci : dict
        An object with the URLs to the three versions of oscillograms.
    lic : str
        URL describing the license of this recording.
    q : str
        Current quality rating for the recording.
    length : float
        Length of the recording in minutes.
    time : str
        Time of day that the recording was made.
    date : str
        Date that the recording was made.
    uploaded : str
        Date that the recording was uploaded to xeno-canto.
    also : list
        An array with the identified background species in the recording.
    rmk : str
        Additional remarks by the recordist.
    bird_seen : str
        Despite the field name (which was kept to ensure backward compatibility),
        this field indicates whether the recorded animal was seen.
    animal_seen : str
        Was the recorded animal seen?
    playback_used : str
        Was playback used to lure the animal?
    temperature : str
        Temperature during recording (applicable to specific groups only).
    regnr : str
        Registration number of the specimen (when collected).
    auto : str
        Automatic (non-supervised) recording?
    dvc : str
        Recording device used.
    mic : str
        Microphone used.
    smp : str
        Sample rate.
    """

    def __init__(self, recording_data: dict):
        """Create a Recording object with a given recording dict returned from the XenoCanto API

        Parameters
        ----------
        recording_data : dict
            The dict of the recording returned by the XenoCanto API
        """

        self.id = recording_data["id"]
        self.gen = recording_data["gen"]
        self.sp = recording_data["sp"]
        self.ssp = recording_data["ssp"]
        self.group = recording_data["group"]
        self.en = recording_data["en"]
        self.rec = recording_data["rec"]
        self.cnt = recording_data["cnt"]
        self.loc = recording_data["loc"]
        self.lat = recording_data["lat"]
        self.lng = recording_data["lng"]
        self.type = recording_data["type"]
        self.sex = recording_data["sex"]
        self.stage = recording_data["stage"]
        self.method = recording_data["method"]
        self.url = recording_data["url"]
        self.file = recording_data["file"]
        self.file_name = recording_data["file_name"]
        self.sono = recording_data["sono"]
        self.osci = recording_data["osci"]
        self.lic = recording_data["lic"]
        self.q = recording_data["q"]
        self.length = recording_data["length"]
        self.time = recording_data["time"]
        self.date = recording_data["date"]
        self.uploaded = recording_data["uploaded"]
        self.also = recording_data["also"]
        self.rmk = recording_data["rmk"]
        self.bird_seen = recording_data["bird_seen"]
        self.animal_seen = recording_data["animal_seen"]
        self.playback_used = recording_data["playback_used"]
        self.temperature = recording_data["temperature"]
        self.regnr = recording_data["regnr"]
        self.auto = recording_data["auto"]
        self.dvc = recording_data["dvc"]
        self.mic = recording_data["mic"]
        self.smp = recording_data["smp"]
