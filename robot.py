#!/usr/bin/env python

import wpilib

class MyRobot(wpilib.IterativeRobotBase):
    def robotInit(self):
        motor1 = wpilib.Talon(1)
        motor2 = wpilib.Talon(2)
        motor3 = wpilib.Victor(3)
        motor4 = wpilib.Victor(4)
        dio1 = wpilib.DigitalInput(1)
        analog5 = wpilib.AnalogInput(5)
        self.joystick = wpilib.Joystick(1)

    

    pass

#if __name__ == '__main__':
#    wpilib.run(MyRobot)
