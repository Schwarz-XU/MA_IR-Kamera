import sys, os
from TemperatureMeasurement import pub


if __name__ == "__main__":
    sys.path.append(os.path.abspath("."))
    print(os.path.abspath("."))
    pub()
