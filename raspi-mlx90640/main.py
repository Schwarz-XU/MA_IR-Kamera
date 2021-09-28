<<<<<<< HEAD
import sys, os
from TemperatureMeasurement import pub

sys.path.append(os.path.abspath("."))

=======
import sys
from TemperatureMeasurement import pub

sys.path.append(".TemperatureMeasurement")
>>>>>>> 88fbc21055378d01d36e60271f2a4ce28fa71064
if __name__ == "main.py":
    pub()