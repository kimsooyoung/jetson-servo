# jetson-servo


## Setup
```
$ git clone https://github.com/kimsooyoung/jetson-servo.git
$ cd jetson-servo
$ ./installServoKit.sh
```

## Python interpreter Example

```
$ python3
> from adafruit_servokit import ServoKit
> kit = ServoKit(channels=16)
> kit.servo[0].angle=180
> kit.servo[0].angle=0
> quit()
```

## JoyStick Example

```

```


# Reference
* [JetsonHacksNano's ServoKit](https://github.com/JetsonHacksNano/ServoKit)