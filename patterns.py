"""
This script will give you experience on the event mechanism
for the robots odometry and navigation.
"""

# importing the Bluetooth class from the irobot_edu_sdk.backend module
from irobot_edu_sdk.backend.bluetooth import Bluetooth
# importing various classes and decorators from the irobot_edu_sdk.robots module
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
# importing the Note class from the irobot_edu_sdk.music module
from irobot_edu_sdk.music import Note

# creating a robot instance using the Create3 class.
# this will be used to control the robot and set up events
# the robot connects via Bluetooth to the robot named "NAME".
robot = Create3(Bluetooth("NAME"))

import math as m

# set up an event that starts when the robot's play button is activated.
@event(robot.when_play)
async def navigate(robot):
    # this line resets the robot's positioning data
    await robot.reset_navigation()

    # === MOVING BY A PRESCRIBED DISTANCE
    """
    for i in range(3):
        await robot.turn_right(60)
        await robot.move(30)
        # retrieves the current position of the robot and stores it in 'pos'
        pos = (await robot.get_position())
        # prints the x, y coordinates, and heading (theta) of the robot
        print("x = {}, y = {}, theta = {}".format(pos.x, pos.y, pos.heading))
    """

    # === NAVIGATING TO SPECIFIC LOCATIONS
    """
    for (x,y) in [(15,int(-15*m.sqrt(3))),(-15,int(-15*m.sqrt(3))),(0,0)]:
        await robot.navigate_to(x,y)
        # retrieves the current position of the robot and stores it in 'pos'
        pos = (await robot.get_position())
        # prints the x, y coordinates, and heading (theta) of the robot
        print("x = {}, y = {}, theta = {}".format(pos.x, pos.y, pos.heading))
    """


# start the robot's
robot.play()
