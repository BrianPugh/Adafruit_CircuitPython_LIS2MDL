""" Display compass heading data from a calibrated magnetometer """

import time
import math
import board
import busio
import adafruit_lis2mdl

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lis2mdl.LIS2MDL(i2c)

# You will need the calibration values from your magnetometer calibration
# these values are in uT and are in X, Y, Z order (min and max values)
hardiron_calibration = [[-61.4879, 34.4782], [-43.6714, 53.5662], [-40.7337, 52.4554]]

# This will take the magnetometer values, adjust them with the calibraitons
# and return a new array with the XYZ values ranging from -100 to 100
def normalize(magvals):
    ret = [0, 0, 0]
    for i, axis in enumerate(magvals):
        minv, maxv = hardiron_calibration[i]
        axis = min(max(minv, axis), maxv)  # keep within min/max calibration
        ret[i] =(axis - minv) * 200 / (maxv - minv) + -100
    return ret


while True:
    magvals = sensor.magnetic
    normvals = normalize(magvals)
    print("magnetometer: %s -> %s" % (magvals, normvals))

    # we will only use X and Y for the compass calculations, so hold it level!
    compass_heading = int(math.atan2(normvals[1], normvals[0]) * 180.0 / math.pi)
    # compass_heading is between -180 and +180 since atan2 returns -pi to +pi
    # this translates it to be between 0 and 360
    compass_heading += 180

    print("Heading:", compass_heading)
    time.sleep(0.1)