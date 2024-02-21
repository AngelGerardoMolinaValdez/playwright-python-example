import os

class DataDirContent:
    def __init__(self, filename: str) -> None:
        cd = os.path.dirname(__file__)
        data_dir = os.path.join(cd, "..", "data")
        self.__data_source = os.path.abspath(os.path.join(data_dir, filename))

    def get_content(self):
        return self.__data_source
