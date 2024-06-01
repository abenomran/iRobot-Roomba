from math import atan2, degrees, sqrt

def getCorrectionAngle(heading):
    angle = int(heading - 90)
    return angle
"""
print(getCorrectionAngle(135.6))
print(getCorrectionAngle(25))
"""


def getAngleToDestination(currentPosition, destination):
     # atan2 and degrees imported from math module
    (x1, y1) = currentPosition
    (x2, y2) = destination
    destAngle = int(degrees(atan2((x2-x1),(y2-y1))))
    """
    if y2 < y1 and x2 < x1:
        destAngle = int(degrees(atan2((y2-y1),(x2-x1))) - 180)
    else:
        destAngle = int(90 - degrees(atan2((y2-y1),(x2-x1))))
    """
    return destAngle

"""
currentPosition = (1, 1)
destination = (5, 3)
print(getAngleToDestination(currentPosition, destination))

currentPosition = (5, 5)
destination = (1, 1)
print(getAngleToDestination(currentPosition, destination))
"""


def getMinProxApproachAngle(readings, angles):
    minProx = 4095/(readings[0] + 1)
    minAngle = angles[0]
    for (i, reading) in enumerate(readings):
        prox = 4095/(reading + 1)
        if prox < minProx:
            minProx = prox
            minAngle = angles[i]
    return (minProx, minAngle)
"""
IR_ANGLES = [-65.3, -38.0, -20.0, -3.0, 14.25, 34.0, 65.3]
readings = [4, 347, 440, 408, 205, 53, 27]
print(getMinProxApproachAngle(readings, IR_ANGLES))

IR_ANGLES = [-65.3, -38.0, -20.0, -3.0, 14.25, 34.0, 65.3]
readings = [731, 237, 202, 229, 86, 120, 70]
print(getMinProxApproachAngle(readings, IR_ANGLES))
"""


def checkPositionArrived(currentPosition, destination, threshold):
    (x1, y1) = currentPosition
    (x2, y2) = destination
    distance = sqrt(((y2-y1)**2) + ((x2-x1)**2)) # distance formula
    return distance <= threshold
"""
print(checkPositionArrived((97, 99), (100, 100), 5.0))
print(checkPositionArrived((50, 50), (45, 55), 5))
"""
