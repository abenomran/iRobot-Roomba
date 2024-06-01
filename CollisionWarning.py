from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

# robot is the instance of the robot that will allow us to call
# its methods and to define events with the @event decorator.
robot = Create3(Bluetooth("ROBOT_NAME")) 

# if emergencyStop is false, the robot proceeds, otherwise it will full stop and light red
emergencyStop = False
# LEFT BUTTON
@event(robot.when_touched, [True, False])  # User buttons: [(.), (..)]
async def when_left_button_touched(robot):
    global emergencyStop
    for i in range(15):
        emergencyStop = True
        await robot.set_wheel_speeds(0,0)
        await robot.set_lights(Robot.LIGHT_ON,Color(255,0,0))


# RIGHT BUTTON
@event(robot.when_touched, [False, True])  # User buttons: [(.), (..)]
async def when_right_button_touched(robot):
    global emergencyStop
    for i in range(15):
        emergencyStop = True
        await robot.set_wheel_speeds(0,0)
        await robot.set_lights(Robot.LIGHT_ON,Color(255,0,0))


# EITHER BUMPER
@event(robot.when_bumped, [True, True])  # [left, right]
async def when_either_bumped(robot):
    global emergencyStop
    for i in range(15):
        emergencyStop = True
        await robot.set_wheel_speeds(0,0)
        await robot.set_lights(Robot.LIGHT_ON,Color(255,0,0))
        
def findMaxProximity(readings):
    maxProximity = readings[0]      
    for read in readings:           
        if read > maxProximity:     # if the current reading is greater than the current minProximity:
            maxProximity = read     # update maxProximity with the current reading.
    return maxProximity 

"""
async def note_lights(robot, note, time, color):
    await robot.play_note(note, time)
    await robot.set_lights(Robot.LIGHT_BLINK, color)
"""

@event(robot.when_play)
async def avoidCollision(robot):

    #while True: 
    
    while not emergencyStop:
        readings = (await robot.get_ir_proximity()).sensors
        #print(readings)
        # he also said specifically index reading 3 so it's the central one at -3 degrees
        readingCenter = readings[3]

        proximity = 4095/(findMaxProximity(readings) + 1)
        #print(proximity)

        if proximity <= 5.0:
            await robot.set_lights(Robot.LIGHT_ON,Color(255, 0, 0))
            await robot.set_wheel_speeds(0, 0)

            # he said put these in separate async functions and call on them
            await robot.play_note(Note.D7, 1)
            
            
        elif proximity <= 30.0:
            await robot.set_wheel_speeds(1, 1) 
            await robot.play_note(Note.D6, 0.1)
            await robot.set_lights(Robot.LIGHT_BLINK,Color(255, 165, 0))
        
        elif proximity <= 100.0:
            await robot.set_wheel_speeds(4, 4)
            await robot.play_note(Note.D5, 0.1)
            await robot.set_lights(Robot.LIGHT_BLINK,Color(255, 255, 0))
            
        else:
            await robot.set_wheel_speeds(8, 8)
            await robot.set_lights(Robot.LIGHT_BLINK,Color(0, 255, 0))
        


# start the robot
robot.play()
