import sys, os
from TemperatureMeasurement import pub

sys.path.append(os.path.abspath("."))
print(os.path.abspath("."))

if __name__ == "__main__":
    pub()