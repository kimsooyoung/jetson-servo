from adafruit_servokit import ServoKit
import board
import busio

import inputs
import serial
import asyncio

import time

# Joystick MUST be "X" Mode!!
class JoySerialSenderTwoBytes(object):

    # 0 ~ 5 / 10 steps
    # 0, 0.5, 1.0, 1.5 ...
    joyDict = {
        'ABS_X': 90,
        'ABS_Y': 120,
        'ABS_RX': 90,
        'ABS_RY': 90,
    }

    servoRange = {
        'ABS_X' : (0, 180),
        'ABS_Y' : (120, 180),
        'ABS_RX': (0, 180),
        'ABS_RY': (0, 180),
    }

    btnDict = {
        'ABS_HAT0X': 0,
        'ABS_HAT0Y': 0,
    }

    def __init__(self):
        super().__init__()

        print(inputs.devices.gamepads)

        pads = inputs.devices.gamepads
        if len(pads) == 0:
            raise Exception("Couldn't find any Gamepads!")

        print("Initializing Servos")
        i2c_bus0=(busio.I2C(board.SCL, board.SDA))

        print("Initializing ServoKit")
        self._kit = ServoKit(channels=16, i2c=i2c_bus0)

        self.msg_header = bytes([255, 1])
        self._loop = asyncio.get_event_loop()

    def rotateServo(self):
        print(self.joyDict)
        
        self._kit.servo[0].angle = self.joyDict['ABS_X']
        self._kit.servo[1].angle = self.joyDict['ABS_Y']
        self._kit.servo[2].angle = self.joyDict['ABS_RX']
        self._kit.servo[3].angle = self.joyDict['ABS_RY']

    def joyLoop(self):
        events = inputs.get_gamepad()
        for event in events:
            if event.code == "ABS_Y" or event.code == "ABS_RY":
                servoRange = self.servoRange[event.code]
                event.state = int((event.state * -1 + 32767) / (32767 + 32768) * (servoRange[1] - servoRange[0])) + servoRange[0]
            elif event.code == "ABS_X" or event.code == "ABS_RX":
                servoRange = self.servoRange[event.code]
                event.state = int((event.state + 32767) / (32767 + 32768) * (servoRange[1] - servoRange[0])) + servoRange[0]

            if (event.code in self.joyDict) or (event.code in self.btnDict):
                self.joyDict[event.code] = event.state
            print(self.joyDict)
        
        self.rotateServo()

    async def joyLoopExecutor(self):
        while True:
            await self._loop.run_in_executor(None, self.joyLoop)

    def run(self):
        try:
            asyncio.ensure_future(self.joyLoopExecutor())
            self._loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self._loop.close()
            print("====== Loop Closed =========")


if __name__=="__main__":

    my_serial = JoySerialSenderTwoBytes()
    my_serial.run()
