import sys, os
from TemperatureMeasurement import pub

print(sys.path)
sys.path.append(os.path.abspath("."))
print(sys.path)

if __name__ == "main.py":
    pub()