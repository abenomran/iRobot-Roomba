from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

import AuxAutonomousDelivery as aux
from math import atan2, degrees, sqrt

# === CREATE ROBOT 
robot = Create3(Bluetooth("XJ-9"))

# === FLAG VARIABLES
HAS_COLLIDED = False
HAS_REALIGNED = False
HAS_FOUND_OBSTACLE = False
HAS_ARRIVED = False

# === OTHER NAVIGATION VARIABLES
SENSOR2CHECK = 0
IR_ANGLES = [-65.3, -38.0, -20.0, -3.0, 14.25, 34.0, 65.3]
DESTINATION = (0, 120)
ARRIVAL_THRESHOLD = 5


# ==========================================================
# FAIL SAFE MECHANISMS

# EITHER BUTTON
@event(robot.when_touched, [True, True])  # User buttons: [(.), (..)]
async def when_either_button_touched(robot):
    global HAS_COLLIDED
    for i in range(15):
        await robot.set_wheel_speeds(0, 0)
        HAS_COLLIDED = True
    await robot.set_lights(Robot.LIGHT_ON, Color(255, 0, 0))
        

# EITHER BUMPER
@event(robot.when_bumped, [True, True])  # [left, right]
async def when_either_bumped(robot):
    global HAS_COLLIDED
    for i in range(15):
        await robot.set_wheel_speeds(0, 0)
        HAS_COLLIDED = True
    await robot.set_lights(Robot.LIGHT_ON, Color(255, 0, 0))

# ==========================================================

# === REALIGNMENT BEHAVIOR

def getMinProxApproachAngle(readings, angles):
    minProx = 4095/(readings[0] + 1)
    minAngle = angles[0]
    for (i, reading) in enumerate(readings):
        prox = 4095/(reading + 1)
        if prox < minProx:
            minProx = prox
            minAngle = angles[i]
    return (minProx, minAngle)

def getCorrectionAngle(heading):
    angle = int(heading - 90)
    return angle

def getAngleToDestination(currentPosition, destination):
     # atan2 and degrees imported from math module
    (x1, y1) = currentPosition
    (x2, y2) = destination
    destAngle = int(degrees(atan2((x2-x1),(y2-y1))))

    return destAngle

def checkPositionArrived(currentPosition, destination, threshold):
    (x1, y1) = currentPosition
    (x2, y2) = destination
    distance = sqrt(((y2-y1)**2) + ((x2-x1)**2)) # distance formula
    return distance <= threshold


async def realignRobot(robot):
    global DESTINATION
    global HAS_REALIGNED
    pos = await robot.get_position()
    resetAngle = getCorrectionAngle(pos.heading)
    await robot.turn_right(resetAngle)
    destAngle = getAngleToDestination((pos.x, pos.y), DESTINATION)
    await robot.turn_right(destAngle)
    HAS_REALIGNED = True


# === MOVE TO GOAL
async def moveTowardGoal(robot):
    global HAS_FOUND_OBSTACLE, IR_ANGLES, SENSOR2CHECK
    
    await robot.set_wheel_speeds(6, 6)

    readings = (await robot.get_ir_proximity()).sensors
    minProx, minAngle = getMinProxApproachAngle(readings, IR_ANGLES)

    if minProx <= 20.0:
        #await robot.set_wheel_speeds(0, 0)
        HAS_FOUND_OBSTACLE = True
        if minAngle <= 0:
            await robot.turn_right(90 + minAngle)
            SENSOR2CHECK == 0
        else:
            await robot.turn_left(90 - minAngle)
            SENSOR2CHECK == 6
        #robot.wait(1)
        readings = (await robot.get_ir_proximity()).sensors
            
        """
        minProx, minAngle = getMinProxApproachAngle(readings, IR_ANGLES)
        SENSOR2CHECK = IR_ANGLES.index(minAngle)
        print(SENSOR2CHECK)
        """

# === FOLLOW OBSTACLE
async def followObstacle(robot):
    global HAS_FOUND_OBSTACLE, HAS_REALIGNED, SENSOR2CHECK
    
    await robot.set_wheel_speeds(5,5)
    readings = (await robot.get_ir_proximity()).sensors
    prox = 4095/(readings[SENSOR2CHECK] + 1)
    #await robot.set_wheel_speeds(0,0)
    if SENSOR2CHECK == 0:
        if prox <= 20:
            await robot.turn_right(3)
            await robot.set_wheel_speeds(5, 5)
        elif prox >= 100.0:
            await robot.move(35)
            HAS_FOUND_OBSTACLE = False
            HAS_REALIGNED = False
            print("100")

    elif SENSOR2CHECK == 6:
        if prox <= 20:
            await robot.turn_right(-3)
            await robot.set_wheel_speeds(5, 5)
        elif prox >= 100.0:
            await robot.move(35)
            HAS_FOUND_OBSTACLE = False
            HAS_REALIGNED = False
            print("100")

      


# === NAVIGATION TO DELIVERY
@event(robot.when_play)
async def makeDelivery(robot):
    global HAS_ARRIVED, HAS_COLLIDED, HAS_REALIGNED, HAS_FOUND_OBSTACLE
    global DESTINATION, ARRIVAL_THRESHOLD, IR_ANGLES, SENSOR2CHECK
    

    while not HAS_COLLIDED:
        #print("1")
        if not HAS_ARRIVED:
            print("2")
            pos = await robot.get_position()
            print(pos)
            print("3")
            if checkPositionArrived((pos.x, pos.y), DESTINATION, ARRIVAL_THRESHOLD):
                print("4")
                await robot.stop()
                await robot.set_lights(Robot.LIGHT_SPIN, Color(0, 255, 0))
                print("5")
                HAS_ARRIVED = True
                print("6")
                break

        
        if not HAS_REALIGNED:
            print("7")
            await realignRobot(robot)
            #print("8")

        if HAS_REALIGNED and not HAS_FOUND_OBSTACLE: 
            print("9")
            await moveTowardGoal(robot)
            #print("10")

        if HAS_FOUND_OBSTACLE:
            print("11")
            await followObstacle(robot)
            #print("12")
            
# start the robot
robot.play()
