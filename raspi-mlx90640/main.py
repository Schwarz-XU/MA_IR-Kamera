import sys, os
from TemperatureMeasurement import mlx90640


if __name__ == "__main__":
    sys.path.append(os.path.abspath("."))
    print(os.path.abspath("."))
    mlx90640()
