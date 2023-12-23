class DownloadManager:
    """A helper class for downloading the retrieved recordings from the XenoCanto APi.
    """
    def __init__(self, data_base_path: str):
        """Init a DownloadManager instance

        Parameters
        ----------
        data_base_path : str
            The base data folder where we want our download manager to store the downloaded files.
        """
        self.data_base_path = data_base_path

    
