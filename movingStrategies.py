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


# set up an event that starts when the robot's play button is activated.
@event(robot.when_play)
async def navigate(robot):
    # this line resets the robot's positioning data
    await robot.reset_navigation()

    # === MOVING BY A PRESCRIBED SPEED
    """
    # === VERSION 1 - Moving forward ===
    # here, the robot's wheel speeds are set to 5 cm/s
    """
    await robot.set_wheel_speeds(5, 5)
    """
    # === VERSION 2 - Moving backward ===
    # sets the robot's wheel speeds to -5 cm/s
    """
    await robot.set_wheel_speeds(-5, -5)

    """
    # === VERSION 3 - Turning left and moving forward ===
    # turns the robot to the left by 90 degrees.
    """
    await robot.turn_left(90)
    # then moves the robot forward at a speed of 5 cm/s
    await robot.set_wheel_speeds(5, 5)


    # === MOVING BY A PRESCRIBED DISTANCE
    """
    # === VERSION 4 - Moving forward ===
    # moves the robot forward by a distance of 50 cm
    """
    await robot.move(50)

    """
    # === VERSION 5 - Moving backward ===
    # moves the robot backward by a distance of 50 cm
    """
    await robot.move(-50)

    """
    # === VERSION 6 - Turning right and moving forward ===
    # turns the robot to the right by 90 degrees.
    """
    await robot.turn_right(90)
    """
    # then moves the robot forward by a distance of 50 cm
    """
    await robot.move(50)


    # === NAVIGATING TO SPECIFIC LOCATIONS

    """
    # === VERSION 7 - navigate to x = 50cm and y = 100cm ===
    # navigates the robot to the coordinates (x=50cm, y=100cm).
    """
    await robot.navigate_to(50, 100)
    """
    # === VERSION 8 - Navigate to x = -30cm and y = 30cm ===
    # navigates the robot to the coordinates (x=-30cm, y=30cm).
    """

    # this starts an infinite loop.
    while True:
        # retrieves the current position of the robot and stores it in 'pos'
        pos = (await robot.get_position())
        # prints the x, y coordinates, and heading (theta) of the robot
        print("x = {}, y = {}, theta = {}".format(pos.x, pos.y, pos.heading))
        # pauses the loop for 1 sec to prevent overwhelming the system
        await robot.wait(1)


# start the robot's
robot.play()
