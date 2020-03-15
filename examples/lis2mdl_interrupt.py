import time
import board
import busio
import adafruit_lis2mdl

i2c = busio.I2C(board.SCL, board.SDA)
lis = adafruit_lis2mdl.LIS2MDL(i2c)
lis.interrupt_threshold = 80
lis.interrupt_enabled = True

while True:
    x_hi, y_hi, z_hi, x_lo, y_lo, z_lo, int_triggered = lis.faults

    print(lis.magnetic)
    print("Xhi:%s\tYhi:%s\tZhi:%s" % (x_hi, y_hi, z_hi))
    print("Xlo:%s\tYlo:%s\tZlo:%s" % (x_lo, y_lo, z_lo))
    print("Int triggered: %s" % int_triggered)
    print()

    time.sleep(1)
