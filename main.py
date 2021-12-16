#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math

#GLOBAL VARIABLES

#number of increments 
num_inc = 20

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

def corner(x, y, a1, a2):
    angle_2=math.acos(((x**2)+(y**2)-(a1**2)-(a2**2))/(2*a1*a2))
    angle_1=math.atan2(y,x)-math.atan2((a2*math.sin(angle_2)),(a1+(a2*math.cos(angle_2))))

    deg_1= math.degrees(angle_1)
    deg_2= math.degrees(angle_2)

    arm_motor1.run_target(speed = 50, target_angle=deg_1, then=Stop.HOLD, wait=True)
    arm_motor2.run_target(speed = 50, target_angle=deg_2, then=Stop.HOLD, wait=True)

def running_motors(link_1,link_2,dest_x,dest_y):
    angle_2=math.acos(((dest_x**2)+(dest_y**2)-(link_1**2)-(link_2**2))/(2*link_1*link_2))
    angle_1=math.atan2(dest_y,dest_x)-math.atan2((link_2*math.sin(angle_2)),(link_1+(link_2*math.cos(angle_2))))

    deg_1= math.degrees(angle_1)
    deg_2= math.degrees(angle_2)

    arm_motor1.run_target(speed = 100, target_angle=deg_1, then=Stop.HOLD, wait=False)
    # wait(2000)
    arm_motor2.run_target(speed = 100, target_angle=deg_2, then=Stop.HOLD, wait=False)
    # wait(2000)

    print("Theoretical:", deg_1, " ",deg_2,"\n")

def draw_line(x1, y1, x2, y2):
    #calculate the x and y difference
    diff_x=x2-x1
    diff_y=y2-y1

    #dividing x and y distance into increments 
    increment_x=diff_x/num_inc
    increment_y=diff_y/num_inc

    for i in range(0, num_inc):
        x1=x1+increment_x
        y1=y1+increment_y
        print("i:",i," x:",x1," y:",y1,"\n")
        running_motors(a1,a2,x1,y1)
        wait(500)
        print("Actual:",arm_motor1.angle(), arm_motor2.angle())

def pen_down():
    servo_motor.reset_angle(0)
    servo_motor.run_time(speed=100, time=3100, then=Stop.HOLD, wait=True)

def pen_up():
    servo_motor.reset_angle(0)
    servo_motor.run_time(speed=-100, time=3000, then=Stop.HOLD, wait=True)
    

# Create your objects here.
ev3 = EV3Brick()

arm_motor1 = Motor(Port.B,Direction.COUNTERCLOCKWISE)
arm_motor2 = Motor(Port.A,Direction.CLOCKWISE)
servo_motor = Motor(Port.C,Direction.COUNTERCLOCKWISE)


# Write your program here.
ev3.speaker.beep()
arm_motor1.reset_angle(0)
arm_motor2.reset_angle(0)


# Link lengths
a1=65
a2=120

#1st point
x1=215
y1=0

#2nd point
x2=70
y2=70

# #3rd point
x3=150
y3=100

# pen_up()
# pen_down()

print("Corner: (5, 3)")
pen_up()
corner(50, 30, a1, a2)
wait(2000)
pen_down()

wait(2000)
print("First point: (12,3)")
draw_line(50,30,120,30)

wait(1000)
print("Second point: (7, 8)")
draw_line(120, 30, 70, 80)

wait(2000)
print("Thrid point:(12,8)")
draw_line(70, 80, 120, 80)

wait(2000)
print("Done :(5,3)")
draw_line(120, 80, 50, 30)