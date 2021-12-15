#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
def corner(x, y, a1, a2):
    print("corner")
    angle_2=math.acos(((x**2)+(y**2)-(a1**2)-(a2**2))/(2*a1*a2))
    angle_1=math.atan(y/x)-math.atan((a2*math.sin(angle_2))/(a1+(a2*math.cos(angle_2))))

    deg_1= math.degrees(angle_1)
    deg_2= math.degrees(angle_2)

    arm_motor1.run_target(speed = 50, target_angle=deg_1, then=Stop.HOLD, wait=True)
    arm_motor2.run_target(speed = 50, target_angle=deg_2, then=Stop.HOLD, wait=True)

def running_motors(link_1,link_2,dest_x,dest_y):

    angle_2=math.acos(((dest_x**2)+(dest_y**2)-(link_1**2)-(link_2**2))/(2*link_1*link_2))
    angle_1=math.atan(dest_y/dest_x)-math.atan((link_2*math.sin(angle_2))/(link_1+(link_2*math.cos(angle_2))))

    deg_1= math.degrees(angle_1)
    deg_2= math.degrees(angle_2)

    arm_motor1.run_target(speed = 100, target_angle=deg_1, then=Stop.HOLD, wait=False)
    # wait(2000)
    arm_motor2.run_target(speed = 100, target_angle=deg_2, then=Stop.HOLD, wait=False)
    # wait(2000)

    print("Theoretical:", deg_1, " ",deg_2,"\n")


# Create your objects here.5
ev3 = EV3Brick()

arm_motor1 = Motor(Port.B,Direction.COUNTERCLOCKWISE)
arm_motor2 = Motor(Port.A,Direction.CLOCKWISE)


# Write your program here.
ev3.speaker.beep()
arm_motor1.reset_angle(0)
arm_motor2.reset_angle(0)

# Link lengths
a1=110
a2=105

#1st point
x1=215
y1=0

#2nd point
x2=70
y2=70

#3rd point
x3=150
y3=100

#calculate the x and y difference
diff_x=x2-x1
diff_y=y2-y1

#number of increments 
num_inc = 20

#dividing x and y distance into increments 
increment_x=diff_x/num_inc
increment_y=diff_y/num_inc

for i in range(0,num_inc):
    x1=x1+increment_x
    y1=y1+increment_y
    print("i:",i," x:",x1," y:",y1,"\n")
    running_motors(a1,a2,x1,y1)
    wait(500)
    print("Actual:",arm_motor1.angle(), arm_motor2.angle())

# run to corner
# corner(x3,y3,a1,a2)

# wait(3000)


# arm_motor1.reset_angle(0)
# arm_motor2.reset_angle(0)

# x_diff=x3-x2
# y_diff=y3-y2

# ev3.screen.print("Running to (7,7)")
# print("(7,7)")
# angle_3=math.acos(((x3**2)+(y3**2)-(a1**2)-(a2**2))/(2*a1*a2))
# angle_4=math.atan(y3/x3)-math.atan((a2*math.sin(angle_3))/(a1+(a2*math.cos(angle_3))))

# deg_3= math.degrees(angle_3)
# deg_4= math.degrees(angle_4)

# arm_motor1.run_target(speed = 100, target_angle=deg_3, then=Stop.HOLD, wait=True)
# arm_motor2.run_target(speed = 100, target_angle=deg_4, then=Stop.HOLD, wait=True)






# print(value)

# angle_2=math.acos(((x1**2)+(y1**2)-(a1**2)-(a2**2))/(2*a1*a2)) #q2
# print(angle_2)

# y_tan =(a1+(a2*math.cos(angle_2))) 
# x_tan= (a2*math.sin(angle_2)

# angle_1=math.atan(y1/x1)+math.atan((a2*math.sin(angle_2))/(a1+(a2*math.cos(angle_2)))) #q1
# print(angle_1)

# deg_1= math.degrees(angle_1)
# deg_2= math.degrees(angle_2)
# print("theo",deg_2, " ",deg_1,"\n")


# arm_motor1.run_target(speed = 50, target_angle=deg_2, then=Stop.HOLD,wait=True)
# arm_motor2.run_target(speed = 50, target_angle=deg_1, then=Stop.HOLD,wait=True)

# print("actual",arm_motor1.angle(), " ", arm_motor2.angle()) 