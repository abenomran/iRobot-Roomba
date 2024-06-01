from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

import math as m

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
        await robot.set_wheel_speeds(0, 0)
        await robot.set_lights(Robot.LIGHT_ON,Color(255, 0 , 0))


# RIGHT BUTTON
@event(robot.when_touched, [False, True])  # User buttons: [(.), (..)]
async def when_right_button_touched(robot):
    global emergencyStop
    for i in range(15):
        emergencyStop = True
        await robot.set_wheel_speeds(0, 0)
        await robot.set_lights(Robot.LIGHT_ON,Color(255, 0 , 0))


# EITHER BUMPER
@event(robot.when_bumped, [True, True])  # [left, right]
async def when_either_bumped(robot):
    global emergencyStop
    for i in range(15):
        emergencyStop = True
        await robot.set_wheel_speeds(0, 0)
        await robot.set_lights(Robot.LIGHT_ON,Color(255, 0 , 0))

#proximity conversion (more clear than sensor-readings)
proxList = [0, 0, 0, 0, 0, 0, 0]
def findMinProximity(readings):
    global proxList
    for i in range(len(readings)): 
        proximity = 4095/(readings[i] + 1)  
        proxList[i] = proximity

    #finding the minimum proximity and its corresponding angle 
    minProximity = proxList[0] 
    angleList = [-65.3, -38, -20, -3, 14.25, 34.0, 65.3]     
    angle = angleList[0]
    for (i, prox) in enumerate(proxList):
        if prox < minProximity:
            minProximity = prox
            angle = angleList[i]
    return (angle, minProximity)

#initiates robot-play and its functionality
@event(robot.when_play)
async def robotPong(robot):
    global emergencyStop
    global proxList
    
    #gets the robot started
    await robot.set_lights(Robot.LIGHT_SPIN,Color(0, 100, 100)) # cyan
    isCyan = True
    await robot.set_wheel_speeds(15, 15)
    closeBy = False

    global emergencyStop
    while not emergencyStop:

       
        readings = (await robot.get_ir_proximity()).sensors
        #findProximity(readings)
        minTup = findMinProximity(readings)

        if minTup[1] <= 20:
            await robot.set_wheel_speeds(0, 0)
            angle = minTup[0]
            closeBy = True
        
        if closeBy: 
            (reflection, isLeft) = getReflectAngle(angle)
            if isLeft:
                await robot.turn_right(reflection)
            else:
                await robot.turn_left(reflection)

            #alternates between cyan and magenta with this if statement
            if isCyan:
                await robot.set_lights(Robot.LIGHT_SPIN,Color(255, 0, 255)) # magenta
                isCyan = False
            else: 
                await robot.set_lights(Robot.LIGHT_SPIN,Color(0, 100, 100)) # cyan
                isCyan = True
            await robot.set_wheel_speeds(15, 15)
            closeBy = False
    
# gets the angle of reflection (turning angle)
def getReflectAngle(angle):
    reflectionAngle = 0
    if angle < 0: # left
        reflectionAngle = 180 + 2 * angle
        isLeft = True
    else:
        reflectionAngle = 180 - 2 * angle
        isLeft = False

    return (reflectionAngle, isLeft)

# ask for desired
robot.play()
