"""
# First step: some libraries should be installed in Raspberry Pi before running
# run the following commands in LXTerminal:
sudo apt install python3-matplotlib python3-scipy python3-numpy
sudo apt install python-smbus i2c-tools
sudo pip3 install RPI.GPIO adafruit-blinka
sudo pip3 install adafruit-circuitpython-mlx90640

# Second step: enable i2c and adjust the baudrate of the i2c interface by setting config.txt
# run the following commands in LXTerminal
sudo nano /boot/config.txt
# find the right line, and replace it with:
dtparam=i2c_arm=on,i2c_arm_baudrate=1000000
or
dtparam=i2c_arm=on,i2c_arm_baudrate=400000

# Third step: check the camera connection with running:
sudo i2cdetect -y 1
# The number "33" should be showed in (3, 30) in a 16x8 matrix
"""

import sys, os
from DataAcquisition import high_fps
# from DataAcquisition import mlx90640


if __name__ == "__main__":
    sys.path.append(os.path.abspath("."))
    print(os.path.abspath("."))
    # mlx90640.run()
    high_fps.run()  # for higher performance
