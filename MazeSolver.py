from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

import AuxMazeSolver as aux

# === CREATE ROBOT OBJECT
robot = Create3(Bluetooth("T-X"))

# === FLAG VARIABLES
HAS_COLLIDED = False
HAS_ARRIVED = False

# === BUILD MAZE DICTIONARY
N_X_CELLS = 3
N_Y_CELLS = 3
CELL_DIM = 50
MAZE_DICT = aux.createMazeDict(N_X_CELLS, N_Y_CELLS, CELL_DIM)
MAZE_DICT = aux.addAllNeighbors(MAZE_DICT, N_Y_CELLS, N_Y_CELLS)

# === DEFINING ORIGIN AND DESTINATION
PREV_CELL = None
START = (0,0)
CURR_CELL = START
DESTINATION = (2,2)
MAZE_DICT[CURR_CELL]["visited"] = True

# === PROXIMITY TOLERANCES
WALL_THRESHOLD = 120


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
# MAZE NAVIGATION AND EXPLORATION

# === NAVIGATE TO CELL
async def navigateToNextCell(robot, nextCell, orientation):
    global MAZE_DICT, PREV_CELL, CURR_CELL, CELL_DIM

    #cardinalDir = ['E', 'N', 'W', 'S']
    PREV_CELL = CURR_CELL
    (x, y) = CURR_CELL
    direction = -1
    
    if orientation == 'E':
        if nextCell == (x, y-1):
            direction = 'right'
        elif nextCell == (x+1, y):
            direction = 'straight'
        elif nextCell == (x, y+1):
            direction = 'left'
        else:
            direction = 'previous'
    elif orientation == 'N':
        if nextCell == (x+1, y):
            direction = 'right'
        elif nextCell == (x, y+1):
            direction = 'straight'
        elif nextCell == (x-1, y):
            direction = 'left'
        else:
            direction = 'previous'
    elif orientation == 'W':
        if nextCell == (x, y+1):
            direction = 'right'
        elif nextCell == (x-1, y):
            direction = 'straight'
        elif nextCell == (x, y-1):
            direction = 'left'
        else:
            direction = 'previous'
    elif orientation == 'S':
        if nextCell == (x-1, y):
            direction = 'right'
        elif nextCell == (x, y-1):
            direction = 'straight'
        elif nextCell == (x+1, y):
            direction = 'left'
        else:
            direction = 'previous'

    if direction == 'straight':
        pass
    elif direction == 'right':
        await robot.turn_right(90)
    elif direction == 'left':
        await robot.turn_left(90)
    elif direction == 'previous':
        await robot.turn_right(180)
    else:
        print('Invalid!')
    
    
    await robot.move(CELL_DIM)
    CURR_CELL = nextCell
    MAZE_DICT[CURR_CELL]['visited'] = True

# === EXPLORE MAZE
@event(robot.when_play)
async def navigateMaze(robot):
    global HAS_COLLIDED, HAS_ARRIVED
    global PREV_CELL, CURR_CELL, START, DESTINATION
    global MAZE_DICT, N_X_CELLS, N_Y_CELLS, CELL_DIM, WALL_THRESHOLD

    await robot.set_lights(Robot.LIGHT_SPIN, Color(255,255,255)) #white light indicator
    while not HAS_COLLIDED:
        if not HAS_ARRIVED:
            if aux.checkCellArrived(CURR_CELL, DESTINATION):
                await robot.set_lights(Robot.LIGHT_SPIN, Color(0,255,0))
                break

        pos = await robot.get_position()
        orientation = aux.getRobotOrientation(pos.heading)
        potentialCells = aux.getPotentialNeighbors(CURR_CELL, orientation)
        # left front right behind

        readings = (await robot.get_ir_proximity()).sensors
        IR0 = 4095/(readings[0]+1)
        IR3 = 4095/(readings[3]+1)
        IR6 = 4095/(readings[6]+1)
        wallList = aux.getWallConfiguration(IR0, IR3, IR6, WALL_THRESHOLD)
        print(wallList)

        navNeighbors = aux.getNavigableNeighbors(wallList, potentialCells, PREV_CELL, N_X_CELLS, N_Y_CELLS)

        MAZE_DICT = aux.updateMazeNeighbors(MAZE_DICT, CURR_CELL, navNeighbors)
        MAZE_DICT = aux.updateMazeCost(MAZE_DICT, CURR_CELL, DESTINATION)
        nextMove = aux.getNextCell(MAZE_DICT, CURR_CELL)
        aux.printMazeGrid(MAZE_DICT, N_X_CELLS, N_Y_CELLS, 'cost')
        await navigateToNextCell(robot, nextMove, orientation)


# start the robot
robot.play()
