from adafruit_servokit import ServoKit
import board
import busio
import time


def run():
    # On the Jetson Nano
    # Bus 0 (pins 28,27) is board SCL_1, SDA_1 in the jetson board definition file
    # Bus 1 (pins 5, 3) is board SCL, SDA in the jetson definition file
    # Default is to Bus 1; We are using Bus 0, so we need to construct the busio first ...
    print("Initializing Servos")

    # i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))
    i2c_bus0=(busio.I2C(board.SCL, board.SDA))

    print("Initializing ServoKit")
    kit = ServoKit(channels=16, i2c=i2c_bus0)

    print("Done initializing")
    sweep = range(0,180)
    for degree in sweep:
        kit.servo[0].angle=degree
        # kit.servo[1].angle=degree
        time.sleep(0.01)

    time.sleep(0.5)

    sweep = range(180,0, -1)
    for degree in sweep :
        kit.servo[0].angle=degree
        time.sleep(0.01)

if __name__=="__main__":
    while True: 
        run()