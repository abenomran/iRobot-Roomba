from collections import deque

def createMazeDict(nXCells, nYCells, cellDim):
    mazeDict = {}
    for x in range(nXCells):
        for y in range(nYCells):
            mazeDict[(x,y)] = {'position': (cellDim * x, cellDim * y), 'neighbors': [], 'visited': False, 'cost': 0}
    return mazeDict
"""
nXCells, nYCells, cellDim = 2, 2, 10
mazeDict = createMazeDict(nXCells, nYCells, cellDim)
print(mazeDict)
"""


def addAllNeighbors(mazeDict, nXCells, nYCells):
    for x in range(nXCells):
        for y in range(nYCells):
            if (x-1, y) in mazeDict:
                mazeDict[(x,y)]['neighbors'].append((x-1, y))
            if (x, y+1) in mazeDict:
                mazeDict[(x,y)]['neighbors'].append((x, y+1))
            if (x+1, y) in mazeDict:
                mazeDict[(x,y)]['neighbors'].append((x+1, y))
            if (x, y-1) in mazeDict:
                mazeDict[(x,y)]['neighbors'].append((x, y-1))

    return mazeDict

"""
mazeDict = createMazeDict(nXCells, nYCells, cellDim)
mazeDict = addAllNeighbors(mazeDict, nXCells, nYCells)
print(mazeDict)
"""

def getRobotOrientation(heading):
    cardinalDeg = [0, 360, 90, 180, 270]
    cardinalDir = ['E', 'E', 'N', 'W', 'S']
    difList = []
    for deg in cardinalDeg:
        difList.append(abs(deg-heading))

    index = difList.index(min(difList))
    return cardinalDir[index]
"""
print(getRobotOrientation(361))
print(getRobotOrientation(88.5))
"""


def getPotentialNeighbors(currentCell, orientation):
    potentialNeighbors = []
    (x,y) = currentCell
    # [leftIndices, frontIndices, rightIndices, backIndices]
    if orientation == 'E':
        potentialNeighbors.append((x, y+1))
        potentialNeighbors.append((x+1, y))
        potentialNeighbors.append((x, y-1))
        potentialNeighbors.append((x-1, y))
    elif orientation == 'N':
        potentialNeighbors.append((x-1, y))
        potentialNeighbors.append((x, y+1))
        potentialNeighbors.append((x+1, y))
        potentialNeighbors.append((x, y-1))
    elif orientation == 'W':
        potentialNeighbors.append((x, y-1))
        potentialNeighbors.append((x-1, y))
        potentialNeighbors.append((x, y+1))
        potentialNeighbors.append((x+1, y))
    elif orientation == 'S':
        potentialNeighbors.append((x+1, y))
        potentialNeighbors.append((x, y-1))
        potentialNeighbors.append((x-1, y))
        potentialNeighbors.append((x, y+1))
    
    return potentialNeighbors
"""
print(getPotentialNeighbors((0,1),"E"))
print(getPotentialNeighbors((2,3),"S"))
"""


def isValidCell(cellIndices, nXCells, nYCells):
    (x, y) = cellIndices
    return (0 <= x < nXCells) and (0 <= y < nYCells)
"""
print(isValidCell((3,3), 4, 5))
print(isValidCell((1,2), 2, 2))
"""


def getWallConfiguration(IR0, IR3, IR6, threshold):
    IR_list = [IR0, IR3, IR6]
    boolList = []
    for IR in IR_list:
        if IR <= threshold:
            boolList.append(True)
        else:
            boolList.append(False)
    return boolList
"""
print(getWallConfiguration(300, 200, 39, 100))
print(getWallConfiguration(23, 800, 10, 100))
"""


def getNavigableNeighbors(wallsAroundCell, potentialNeighbors, prevCell, nXCells, nYCells):
    if prevCell != None:
        navNeighbors = [prevCell]
    else:
        navNeighbors = []
    for index, cell in enumerate(potentialNeighbors):
        if isValidCell(cell, nXCells, nYCells) and index < len(wallsAroundCell) and not wallsAroundCell[index]:
                    if cell != prevCell:
                        navNeighbors.append(cell)
    return navNeighbors
"""
print(getNavigableNeighbors([True, True, False], [(1,2),(2,1),(1,0),(0,1)], (0,1), 2, 2))
print(getNavigableNeighbors([False, True, False], [(0,2),(1,3),(2,2),(1,1)], (1,1), 4, 4))
"""

def updateMazeNeighbors(mazeDict, currentCell, navNeighbors):
    for neighbor in mazeDict[currentCell]['neighbors']:
        if neighbor not in navNeighbors:
            mazeDict[neighbor]['neighbors'].remove(currentCell)
    mazeDict[currentCell]['neighbors'] = navNeighbors
    return mazeDict


def getNextCell(mazeDict, currentCell):
    neighbors = mazeDict[currentCell]['neighbors']
    print(neighbors)
    #unvisited_neighbors = [(mazeDict[neighbor]['cost'], neighbor) for neighbor in neighbors if not mazeDict[neighbor]['visited']]
    unvisited_neighbors = []
    for neighbor in neighbors:
        if not mazeDict[neighbor]['visited']:
            unvisited_neighbors.append((mazeDict[neighbor]['cost'], neighbor))
    unvisited_neighbors.sort()
    
    if unvisited_neighbors:
        return unvisited_neighbors[0][1]
    else:
        visited_neighbors = []
        for neighbor in neighbors:
            visited_neighbors.append((mazeDict[neighbor]['cost'], neighbor))
        visited_neighbors.sort()
        print(visited_neighbors)
        return visited_neighbors[0][1]
    """
    elif not unvisited_neighbors:
        for neighbor in neighbors:
            unvisited_neighbors.append((mazeDict[neighbor]['cost'], neighbor))
            print(unvisited_neighbors)
        unvisited_neighbors.sort()
        print(unvisited_neighbors)
        return unvisited_neighbors[0][1]
    """
    
""" 
mazeDict = {(0, 0): {'position': (0, 0),'neighbors': [(0, 1)], 'visited': True, 'cost': 0},
            (0, 1): {'position': (0, 1),'neighbors': [(0, 0), (1, 1)], 'visited': True, 'cost': 1},
            (1, 0): {'position': (1, 0), 'neighbors': [(1, 1)], 'visited': False, 'cost': 3},
            (1, 1): {'position': (1, 1), 'neighbors': [(1, 0), (0, 1)], 'visited': False, 'cost': 2}}
currentCell = (0,1)
print(getNextCell(mazeDict, currentCell))

mazeDict = {(0, 0): {'position': (0, 0),'neighbors': [(0, 1)], 'visited': True, 'cost': 0},
            (0, 1): {'position': (0, 1),'neighbors': [(0, 0), (1, 1)], 'visited': False, 'cost': 1},
            (1, 0): {'position': (1, 0), 'neighbors': [(1, 1)], 'visited': False, 'cost': 3},
            (1, 1): {'position': (1, 1), 'neighbors': [(1, 0), (0, 1)], 'visited': True, 'cost': 2}}
currentCell = (1,1)
print(getNextCell(mazeDict, currentCell))
"""


def checkCellArrived(currentCell, destination):
     return currentCell == destination
"""
print(checkCellArrived((4,3), (4,3)))
print(checkCellArrived((6,7), (7,6)))
"""


"""
The following implementation of the Flood Fill algorithm is
tailored for maze navigation. It updates the movement cost for
each maze cell as the robot learns about its environment. As
the robot moves and discovers navigable adjacent cells, it
gains new information, leading to frequent updates in the
maze's data structure. This structure tracks the layout and
traversal costs. With each step and discovery, the algorithm
recalculates the cost to reach the destination, adapting to
newly uncovered paths. This iterative process of moving,
observing, and recalculating continues until the robot reaches
its destination, ensuring an optimal path based on the robot's
current knowledge of the maze.
"""
def updateMazeCost(mazeDict, start, goal):
    for (i,j) in mazeDict.keys():
        mazeDict[(i,j)]["flooded"] = False
    queue = deque([goal])
    mazeDict[goal]['cost'] = 0
    mazeDict[goal]['flooded'] = True
    while queue:
        current = queue.popleft()
        current_cost = mazeDict[current]['cost']
        for neighbor in mazeDict[current]['neighbors']:
            if not mazeDict[neighbor]['flooded']:
                mazeDict[neighbor]['flooded'] = True
                mazeDict[neighbor]['cost'] = current_cost + 1
                queue.append(neighbor)
    return mazeDict

"""
This function prints the information from the dictionary as
a grid and can help you troubleshoot your implementation.
"""
def printMazeGrid(mazeDict, nXCells, nYCells, attribute):
    for y in range(nYCells - 1, -1, -1):
        row = '| '
        for x in range(nXCells):
            cell_value = mazeDict[(x, y)][attribute]
            row += '{} | '.format(cell_value)
        print(row[:-1])
