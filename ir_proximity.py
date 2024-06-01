"""
This script will give you experience on the event mechanism
for the IR sensors.

The behaviors implemented here are as follows:

    TASK 1. The robot will read the data from the IR sensors
    and print the reading corresponding to each IR angle to
    the screen in an interval of 2 seconds.

    TASK 2. The robot will read the data from the IR sensors,
    find the maximum proximity (max reading) and set the
    brightness of the ring light accordingly. The closest an
    object is to any of the IR sensors, the brighter the ring
    light will become.

NOTE: Make sure that in this script you comment out the blocks
of code that are marked with TASK 1. This will allow you to see
a much smoother adjustment of the brightness in TASK 2.

Let's try it out! Follow the instructions below for each one:

    TASK 1. Running the script with minimal modifications:
        a. Change "BORELA" to the identifier of your robot
        b. Run the file using IDLE, VS Code or the terminal
        d. Once you hear the chime that indicates the robot
        has successfully connected to your laptop, move your
        hand by the IR sensors to see the proximity value change
        for the angle at which your hand is at

    TASK 2. Running the script changing light intensity:
        a. Change "BORELA" to the identifier of your robot
        b. Comment the code block in each of the functions
        that are marked with  "TASK 1"
        c. Uncomment the code blocks in each of the functions
        that are marked with  "TASK 2"
        d. Run the file using IDLE, VS Code or the terminal
        e. Once you hear the chime that indicates the robot
        has successfully connected to your laptop, move your
        hand by the IR sensors to see the proximity value change
        for the angle at which your hand is at. Also notice how
        the light intensity changes by getting closer or further
        from the robot.
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

# a list of angles for the robot's infrared (IR) sensors,
# indicating their respective positions.
IR_ANGLES = [-65.3, -38.0, -20.0, -3.0, 14.25, 34.0, 65.3]


# TASK 2
# find the maximum proximity value from a list of readings.
def findMaxProximity(readings):
    maxProximity = readings[0]      # initialize maxProximity with the first value from the readings list.
    for read in readings:           # Loop through each reading in the readings list.
        if read > maxProximity:     # if the current reading is greater than the current maxProximity:
            maxProximity = read     # update maxProximity with the current reading.
    return maxProximity             # return the maximum proximity value found.

# adjust the brightness of the robot's lights based on proximity readings.
async def setBrightness(robot, readings):
    maxProximity = findMaxProximity(readings)   # find the maximum proximity from the readings list using the previously defined function.
    intensity = int(255 * maxProximity / 4095)  # calculate light intensity based on proximity.
    await robot.set_lights_rgb(intensity, intensity, intensity)  # set the robot's lights to the calculated intensity.


# set up an event that starts when the robot's play button is activated.
@event(robot.when_play)
async def play(robot):
    global IR_ANGLES
    # print instruction to the user.
    print('try moving your hand right in front of the IR sensors')
    # begin an infinite loop to constantly read from the IR sensors.
    while True:
        # get the IR raw proximity readings from the robot's sensors.
        readings = (await robot.get_ir_proximity()).sensors # list

        # TASK 1
        # loop through each reading index
        for i in range(len(readings)):
            # get reading in position i
            read = readings[i]
            # get the angle corresponding to the current reading
            angle = IR_ANGLES[i]
            # print the angle and normalized proximity value.
            print("IR at {} degrees, reading = {}".format(angle, read))
        print("--------------------------------------")
        await robot.wait(2) # block execution for two seconds
        
        # TASK 2
        await setBrightness(robot, readings) # call the asyn function to adjust the brightness
        await robot.wait(0.1)                # block execution for a tenth of a second
        



# start the robot's functionality, effectively "booting up" the system and listening for events.
robot.play()
