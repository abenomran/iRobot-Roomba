"""
This script will give you experience on the event mechanism
for the buttons.

The behaviors implemented here are as follows:

    TASK 1. The robot will not do anything until either the
    (.) or (..) buttons are pressed. Once either of them is
    pressed, the robot will start beeping at a constant pitch

    TASK 2. Building on the behavior in Task 1, when the (.)
    button is pressed the beeping note frequency is doubled
    making it higher pitched. Conversely, when (..) is pressed
    the note frequency is halved, making it lower pitched.

    TASK 3. Building on the behaviors of the two previous tasks,
    now when either of the (.) and (..) buttons are pressed,
    the ring light will turn on and alternate between spinning
    and blinking when the button is pressed.



Let's try it out! Follow the instructions below for each one:

    TASK 1. Running the script with minimal modifications:
        a. Change "BORELA" to the identifier of your robot
        b. Run the file using IDLE, VS Code or the terminal
        c. Once you hear the chime that indicates the robot
        has successfully connected to your laptop, press either
        button to see how the robot will start beeping.

    TASK 2. Modifying the value of the NOTE_FREQUENCY variable:
        a. Uncomment the code blocks in each of the functions
        that are marked with "TASK 2"
        b. Run the file using IDLE, VS Code or the terminal
        c. Once you hear the chime that indicates the robot
        has successfully connected to your laptop. Notice now
        that depending on the button you press, the robot will
        beep at a higher or lower pitch

    TASK 3. Using the switchLights function
        a.  Uncomment the code blocks in each of the functions
        that are marked with "TASK 3", including the switchLights
        function definition
        b. Run the file using IDLE, VS Code or the terminal
        c. Once you hear the chime that indicates the robot
        has successfully connected to your laptop. Notice now
        that depending on the button you press, the robot will
        beep at a higher or lower pitch.
        d. Notice also that the light pattern will switch between
        spinning and blinking whenever either of the buttons is
        pressed.
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

# setting a constant frequency for a note.
NOTE_FREQUENCY = 220
# a flag to check if any button on the robot is pressed.
# it's initialized as False.
ANY_BUTTON_PRESSED = False


# TASK 3
# setting behavior of the lights
LIGHT_BEHAVIOR = "spin"


# setting up an event that will be triggered when the left button on the robot is touched.
@event(robot.when_touched, [True, False])      # the [True, False] list indicates the left button is touched.
async def touched_left(robot):                 # asynchronous event handler.
    global NOTE_FREQUENCY, ANY_BUTTON_PRESSED  # accessing global variables to modify them inside this function.
    print('Left button pressed')               # output message for debugging or user feedback.
    ANY_BUTTON_PRESSED = True                  # updating the flag to True since the button was pressed.

    
    # TASK 2
    NOTE_FREQUENCY = int(2*NOTE_FREQUENCY)    # increases the frequency of the note by one octave
    
    
    # TASK 3
    await switchLights(robot)
    

# Setting up another event for when the robot's right button is touched.
@event(robot.when_touched, [False, True])      # The [False, True] list indicates the right button is touched.
async def touched_right(robot):                # asynchronous event handler.
    global NOTE_FREQUENCY, ANY_BUTTON_PRESSED  # accessing global variables to modify them inside this function.
    print('Right button pressed')              # output message for debugging or user feedback.
    ANY_BUTTON_PRESSED = True                  # updating the flag to True since the button was pressed.
    
    # TASK 2
    NOTE_FREQUENCY = int(NOTE_FREQUENCY/2)     # decreases the frequency of the note by one octave
    
    
    # TASK 3
    await switchLights(robot)
    


# TASK 3
# define an asynchronous function called 'switchLights' that takes in a robot instance.
async def switchLights(robot):
    # accessing the global variable 'LIGHT_BEHAVIOR' to modify its value inside the function.
    global LIGHT_BEHAVIOR
    # Check if the current light behavior is set to 'spin'.
    if LIGHT_BEHAVIOR == "spin":
        # set the robot's lights to spin behavior with a blue color.
        await robot.set_lights(Robot.LIGHT_SPIN, Color(0, 0, 255))
        # change the light behavior mode to 'blink' for the next invocation.
        LIGHT_BEHAVIOR = "blink"
    # check if the current light behavior is set to 'blink'.
    elif LIGHT_BEHAVIOR == "blink":
        # set the robot's lights to blink behavior with a blue color.
        await robot.set_lights(Robot.LIGHT_BLINK, Color(0, 0, 255))
        # Change the light behavior mode back to 'spin' for the next invocation.
        LIGHT_BEHAVIOR = "spin"


# setting up an event that plays a note when the robot's play button is activated.
@event(robot.when_play)
async def play(robot):
    global NOTE_FREQUENCY, ANY_BUTTON_PRESSED
    while True:                                         # an infinite loop until the robot is shut off
        if ANY_BUTTON_PRESSED:                          # check if any button was pressed
            await robot.play_note(NOTE_FREQUENCY, 0.2)  # play the note with the given frequency for 0.2 sec
        await robot.wait(1.0)                           # delays the next iteration of the loop by 1.0 sec

# This line starts the robot's functionality, effectively "booting up" the system and listening for events
robot.play()
