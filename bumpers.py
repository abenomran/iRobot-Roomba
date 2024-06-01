"""
This script will give you experience on the event mechanism
for the bumpers.

The behaviors implemented here are as follows:

    TASK 1. The robot will not do anything until we press one
    of the bumpers. When the right bumper is pressed, the robot
    will spin clockwise and the ring light will turn on in solid
    green. When the left bumper is pressed, the robot will
    spin counterclockwise and the ring light will switch to red

    TASK 2. Building on the behavior in Task 1, now when either
    bumper is pressed the spinning speed will increase by a
    fixed amount until it reaches the robot's maximum speed.



Let's try it out! Follow the instructions below for each one:

    TASK 1. Running the script with minimal modifications:
        a. Change "BORELA" to the identifier of your robot
        b. Run the file using IDLE, VS Code or the terminal
        d. Once you hear the chime that indicates the robot
        has successfully connected to your laptop, press either
        of the bumpers to see how the lights change colors and
        how it rotates to one direction or another depending on
        the bumper that was pressed.

    TASK 2. Modifying the value of the SPEED variable:
        a. Change the initial assignment of the SPEED variable
        to 5 cm/s.
        b. Uncomment the marked line in each of the async event
        functions that are marked with "TASK 2"
        c. Run the file using IDLE, VS Code or the terminal
        d. Once you hear the chime that indicates the robot
        has successfully connected to your laptop, press either
        of the bumpers to see how in addition to the previous
        responses, now the speed with which the robot rotates
        increases with every bumper press.
"""


# importing the Bluetooth class from the irobot_edu_sdk.backend module
from irobot_edu_sdk.backend.bluetooth import Bluetooth
# importing various classes and decorators from the irobot_edu_sdk.robots module
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
# importing the Note class from the irobot_edu_sdk.music module
from irobot_edu_sdk.music import Note

# creating a robot instance using the Create3 class.
# this will be used to control the robot and set up events
# the robot connects via Bluetooth to the robot named "BORELA".
robot = Create3(Bluetooth("EVE"))

# creating a global variable for the wheel speed
# we normally name global variables in all caps to remind us
# they are not local variables
SPEED = 4 # cm/s

# defining an event that is triggered when the robot's left bumper is pressed
@event(robot.when_bumped, [True, False])  # the list [True, False] indicates the left bumper is pressed
async def bumped_left(robot):             # asynchronous function that runs when the event is triggered
    global SPEED                          # specifying that SPEED is a global variable
    print('Left bumper pressed')          # output message indicating the left bumper was pressed
    await robot.set_wheel_speeds(-SPEED,SPEED)  # setting the robot's wheel speeds: left wheel to -SPEED and right wheel to SPEED
    await robot.set_lights_rgb(255, 0, 0) # setting the robot's light to red
    """
    # TASK 2
    SPEED += 2                            # increments the speed by 2 cm/s for the next execution
    """

# defining another event for when the robot's right bumper is pressed
@event(robot.when_bumped, [False, True])  # the list [False, True] indicates the right bumper is pressed
async def bumped_right(robot):            # asynchronous function that runs when the event is triggered
    global SPEED                          # specifying that SPEED is a global variable
    print('Right bumper pressed')         # output message indicating the right bumper was pressed
    await robot.set_wheel_speeds(SPEED,-SPEED)  # setting the robot's wheel speeds: left wheel to SPEED and right wheel to -SPEED
    await robot.set_lights_rgb(0, 255, 0) # setting the robot's light to green
    """
    # TASK 2
    SPEED += 2                            # increments the speed by 2 cm/s for the next execution
    """

# trigger the system execution
robot.play()
