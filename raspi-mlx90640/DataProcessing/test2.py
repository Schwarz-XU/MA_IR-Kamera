import time
from datetime import datetime
import csv


class Write_file:
    def __init__(self, file_name, file_time):
        self.file_name = file_name
        self.file_time = file_time

    def run_script(self):
        print(self.file_name)
        print(self.file_time)
