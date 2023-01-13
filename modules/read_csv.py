import csv
import time
import zipfile

from modules.features import Features


class ReadCSV:
    features: Features = None

    def __init__(self, filename: str):
        self.filename: str = filename

    def read(self) -> Features:
        row_header = True
        with zipfile.ZipFile(self.filename) as z:
            csvfile = z.namelist()[0]
            with z.open(csvfile) as f:
                for line in f:
                    for row in csv.reader([line.decode('utf-8')]):
                        if row_header:
                            self.features = Features(row)
                            # row_header = False
                            return self.features
