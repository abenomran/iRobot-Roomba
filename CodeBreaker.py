# **** PASSWORD DETECTION MECHANISM ****
# (CodeBreaker.py)

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth("ROBOT_NAME"))

# global pwdInput
pwdInput = ""
pwd = "3241"

@event(robot.when_play)
async def passwordPrompt(robot):
    await robot.set_lights(Robot.LIGHT_ON,Color(255,255,255))
    print("-----------------------------------")
    print("Input your password!")
    print("-----------------------------------")


# Password Checker
async def checkUserCode(robot):
    global pwdInput

    SPEED = 10
    
    if len(pwdInput) == len(pwd):
    
        if pwdInput == pwd:
            
            # initiates dance
            await robot.play_note(Note.A4, 0.25)
            await robot.play_note(Note.A5, 0.25)
            await robot.set_lights(Robot.LIGHT_BLINK,Color(255,255,255))
            await robot.set_wheel_speeds(SPEED + 5,-SPEED)
            await robot.play_note(Note.A5, 0.25)
            await robot.set_lights(Robot.LIGHT_SPIN,Color(0, 255, 0))
            await robot.set_lights(Robot.LIGHT_BLINK,Color(0, 255, 0))
            await robot.play_note(Note.A5, 0.25)
            await robot.wait(3)
            await robot.play_note(Note.A5, 0.25)
            await robot.set_wheel_speeds(-SPEED,SPEED + 5)
            await robot.play_note(Note.A5, 0.25)

            await robot.wait(9.1) 
            await robot.set_wheel_speeds(0,0)
            await robot.set_lights(Robot.LIGHT_ON,Color(255,255,255))


        else: # goes red and low note (disappointment sound)
            await robot.play_note(220, 0.5)
            await robot.set_lights(Robot.LIGHT_BLINK,Color(255, 0, 0))

            await robot.wait(5) 
            await robot.set_lights(Robot.LIGHT_ON,Color(255,255,255))

            #reopens password inputting
            pwdInput = ""

    
    
    



# Left button press --> 1
@event(robot.when_touched, [True, False])
async def leftBtnInput(robot):
    await robot.play_note(Note.C5, 0.25)
    
    global pwdInput
    pwdInput += "1" 
    print("Password: " + pwdInput)
    print("-----------------------------------")

    await checkUserCode(robot)
    
    

# Right button press --> 2
@event(robot.when_touched, [False, True])
async def rightBtnInput(robot):
    await robot.play_note(Note.D5, 0.25)
    
    global pwdInput
    pwdInput += "2" 
    print("Password: " + pwdInput)
    print("-----------------------------------")

    await checkUserCode(robot)

# Left bumper press --> 3
@event(robot.when_bumped, [True, False])
async def leftBumperInput(robot):
    await robot.play_note(Note.E5, 0.25)
    
    global pwdInput
    pwdInput += "3" 
    print("Password: " + pwdInput)
    print("-----------------------------------")

    await checkUserCode(robot)

# Right bumper press --> 4
@event(robot.when_bumped, [False, True])
async def rightBumperInput(robot):
    await robot.play_note(Note.F5, 0.25)
    
    global pwdInput
    pwdInput += "4" 
    print("Password: " + pwdInput)
    print("-----------------------------------")

    await checkUserCode(robot)


# (255, 0, 0) red
# (0, 255, 0) green


#trigger execution
robot.play()