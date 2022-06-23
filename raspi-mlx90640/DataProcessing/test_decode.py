import time
import numpy as np
from DataAcquisition import sub


def run():
    while True:
        try:
            sub.run()
            time.sleep(2)
            panel_data = sub.panel_data
            print(len(panel_data))
            if panel_data != "":
                print(panel_data)

        except Exception as e:
            print(repr(e))


if __name__ == '__main__':
    run()
