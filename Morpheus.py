#/bin/python3

# Made By FG6 (Bigjango)
# Credit to Martin O'Hanlon (github: martinohanlon) for parts for the SafeWalk() code
# Credit to basedSkeleton


import mcpi.minecraft as minecraft
import keyboard, math
import spectator_mode
import PySimpleGUI as sg
from random import random
from time import sleep

try:
    mc = minecraft.Minecraft.create()
    entityIds = mc.getPlayerEntityIds()
    mc.camera.setNormal(entityIds[0])
except:
    window = sg.Window('Error', [[sg.Text('An error has occurred: You need to join a world/server in MCPi to use Morpheus.')], [sg.Button('Exit')]])
    window.read()
    window.close()
    quit()
    
realcommands = {'PlayerToPlayerTp()':'Player Teleport (M)', 'WaypointTeleport()':'Waypoint Teleport', 'SmartLocationTeleport()':'Location Teleport', 'ExactLocationTeleport()':'Exact Location Teleport', 'TrackPlayer()':'Player Tracker', 'WhosOnline()':'Online Players', 'FreeCam()':'FreeCam', 'TeleportUp()':'Teleport up', 'SpamChat()':'Chat Spammer', 'SmartSpam()':'Smart Chat Spammer', 'SafeWalk()':'Safewalk (glitchy)', 'FastBreak()':'Fast Break (M)', 'SetBlock()':'Set Block', 'ChangeWorld()':'Change all blocks in the world'}


def PlayerToPlayerTp():
    entityIds = mc.getPlayerEntityIds()
    i = ''
    target = 1
    while i != 'yes' and len(entityIds) != target:
        mc.camera.setFollow(entityIds[target])
        window = sg.Window('Player Teleport', [[sg.Text('Is this the player you want to teleport to?')], [sg.Button('yes')], [sg.Button('no')]])
        yesno = window.read()
        i = yesno[0]
        window.close()
        if i != 'yes':
            target = target + 1

    if not i != 'yes' and len(entityIds) != target:
        mc.player.setPos(mc.entity.getPos(entityIds[target]))

    else:
        window = sg.Window('Player Teleport', [[sg.Text('There are no more players left.')], [sg.Button('Quit')]])
        window.read()
        window.close()
        
    mc.camera.setNormal(entityIds[0])
    
def TrackPlayer():
    entityIds = mc.getPlayerEntityIds()
    i = ''
    target = 1
    while i != 'yes' and len(entityIds) != target:
        mc.camera.setFollow(entityIds[target])
        window = sg.Window('Player Tracker', [[sg.Text('Is this the player you want to track?')], [sg.Button('yes')], [sg.Button('no')]])
        yesno = window.read()
        i = yesno[0]
        window.close()
        if i != 'yes':
            target = target + 1
    if not i != 'yes' and len(entityIds) != target:
        sleeptime = int(input('How many seconds between each report should there be? '))
        r = int(input('How many times should I report on them? '))
        while r > 0:
            print(mc.entity.getPos(entityIds[target]))
            if r != 1:
                sleep(sleeptime)
            r = r-1
        print('done!')
        
    else:
        window = sg.Window('Player Tracker', [[sg.Text('Sorry, that is everyone')], [sg.Button('Quit')]])
        window.read()
        window.close()

    mc.camera.setNormal(entityIds[0])

def SmartLocationTeleport():
    layout = [[sg.Text('Location Teleport')], [sg.Text('X-pos:')], [sg.Input('')],[sg.Text('Z-pos:')], [sg.Input('')], [sg.Button("done")]]
    window = sg.Window('Location Teleport', layout)
    yesno = window.read()
    cordList = yesno[1]
    x = cordList[0]
    z = cordList[1]
    window.close()
    try:
        y = mc.getHeight(float(x),float(z))+0.01
        mc.player.setPos(float(x),float(y),float(z))
    except TypeError:
        print('You must input a number')
    except:
        print('Unknown error, make sure the location exists.')
    
def ExactLocationTeleport():
    layout = [[sg.Text('Exact Location Teleport')], [sg.Text('X-pos:')], [sg.Input('')], [sg.Text('Y-pos:')], [sg.Input('')], [sg.Text('Z-pos:')], [sg.Input('')], [sg.Button("done")]]
    window = sg.Window('Exact Location Teleport', layout)
    yesno = window.read()
    cordList = yesno[1]
    x = cordList[0]
    y = cordList[1]
    z = cordList[2]
    window.close()
    try:
        mc.player.setPos(float(x),float(y),float(z))
    except TypeError:
        print('You must input a number')
    except:
        print('Unknown error, make sure the location exists.')

def WhosOnline():
    entityIds = mc.getPlayerEntityIds()
    if len(entityIds) != 1:
        if len(entityIds) == 2:
            layout = [[sg.Text("There's "+str(len(entityIds)-1)+" other player(s) online")], [sg.Button("ok")]]
            window = sg.Window('Online Players', layout)
            window.read()
        else:
            layout = [[sg.Text("There's "+str(len(entityIds)-1)+" other player(s) online")], [sg.Button("ok")]]
            window = sg.Window('Online Players', layout)
            window.read()
    else:
        layout = [[sg.Text('There are no other players online.')], [sg.Button("ok")]]
        window = sg.Window('Online Players', layout)
        window.read()
    window.close()
    
def SetBlock():
    layout = [[sg.Text('Setblock')], [sg.Text('Block ID:')], [sg.Input('')], [sg.Button("done")]]
    window = sg.Window('Setblock', layout)
    setblock = window.read()
    setblock = setblock[1]
    setblock = setblock[0]
    try:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y+1, z, int(setblock))
    except TypeError:
        print('You must input a number')
    except:
        print('Unknown error. Make sure the block exists.')
    window.close()
    
def FreeCam():
    spectator_mode.switch()

def SpamChat():
    layout = [[sg.Text('Chat Spammer')], [sg.Text('Message to spam:')], [sg.Input('')], [sg.Text('Time in between each message (in seconds):')], [sg.Input('')], [sg.Button("done")]]
    window = sg.Window('Chat Spammer', layout) #basedSkeleton moment
    yesno = window.read()
    cordList = yesno[1]
    message = cordList[0]
    sleeptime = cordList[1]
    window.close()
    while not keyboard.is_pressed('esc'):
        mc.postToChat(message)
        sleep(float(sleeptime))


def TeleportUp():
    x,y,z = mc.player.getPos()
    y = mc.getHeight(x,z)+0.01
    mc.player.setPos(x,y,z)
    
def SmartSpam():
    spam = []
    message = input('Type a message to spam. Type (\'ex\' to finish) ')
    while message != 'ex':
        spam.append(message)
        message = input('Type a message to spam. Type (\'ex\' to finish) ')
    r = input('How many messages should be sent?')
    for n in range(0, int(r)):
        for i in spam:
            mc.postToChat(i)
            sleep(1)

def distance(x,y,z,x2,y2,z2):
    xd = x2 - x
    yd = y2 - y
    zd = z2 - z
    return(math.sqrt((xd*xd)+(yd*yd)+(zd*zd)))

def WaypointTeleport():
    window = sg.Window('Waypoint Teleport', [[sg.Text('Click \'set\' to save this location, then click \'use\' to return to it')], [sg.Button('Use')],  [sg.Button('Set')],[sg.Button('Cancel')]])
    yesno = window.read()
    i = yesno[0]
    window.close()
    if i == 'Set': # making it so you can actually save a location
        global wayx,wayy,wayz
        wayx,wayy,wayz = mc.player.getPos()
        file = open("morpheus.ini", "w") #making the location saved stay even when the game is closed
        file.write("[morpheus]\nwayx: " + "'" + str(wayx) + "'\nwayy: " + "'" + str(wayy) + "'\nwayz" + "'" + str(wayz) + "'" ) #write to file
        file.close #done
    if i == 'Use': # changing the variables so they don't get overwritten
        mc.player.setPos(wayx, wayy, wayz)

def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

def SafeWalk():
    unsafeblocks = [0, 10, 11, 30]
    lastPlayerPos = mc.player.getPos()
    while not keyboard.is_pressed('esc'):
        playerPos = mc.player.getPos()
        movementX = lastPlayerPos.x - playerPos.x
        movementZ = lastPlayerPos.z - playerPos.z
        if ((movementX < -0.2) or (movementX > 0.2) or (movementZ < -0.2) or (movementZ > 0.2)):
            nextPlayerPos = playerPos
            while ((int(playerPos.x) == int(nextPlayerPos.x)) and (int(playerPos.z) == int(nextPlayerPos.z))):
                nextPlayerPos = minecraft.Vec3(nextPlayerPos.x - movementX, nextPlayerPos.y, nextPlayerPos.z - movementZ)
            blockBelowPos = roundVec3(nextPlayerPos)
            if blockBelowPos.z < 0: blockBelowPos.z = blockBelowPos.z - 1
            if blockBelowPos.x < 0: blockBelowPos.x = blockBelowPos.x - 1
            blockBelowPos.y = blockBelowPos.y - 1
            if mc.getBlock(blockBelowPos) in unsafeblocks:
                mc.setBlock(blockBelowPos.x, blockBelowPos.y, blockBelowPos.z, 246)
            lastPlayerPos = playerPos

def FastBreak():
    while not keyboard.is_pressed('esc'):
        x, y, z = mc.player.getPos()
        for change_y in range(0, 3):
            for change_x in range(-2, 2):
                for change_z in range(-2, 2):
                    if mc.getBlock(x+change_x,y+change_y,z+change_z) != 0:
                        mc.setBlock(x+change_x,y+change_y,z+change_z,0)
def ChangeWorld():
    layout = [[sg.Text('Change all the blocks in the world')], [sg.Text('Block ID:')], [sg.Input('')], [sg.Button("done")]]
    window = sg.Window('Change all blocks', layout)
    setblock = window.read()
    setblock = setblock[1]
    setblock = setblock[0]
    try:
        mc.setBlocks(-256, -128, -256, 256, 128, 256,int(setblock))
    except TypeError:
        print('You must input a number')
    except:
        print('Unknown error. Make sure the block exists.')

menulayout = []
layout = ''
for commander in realcommands:
    if commander == list(realcommands)[len(realcommands)-1]:
        layout = layout + ('[sg.Button("'+realcommands[commander]+'")]')
    else:
        layout = layout + ('[sg.Button("'+realcommands[commander]+'")], ')

exec('menulayout = [[sg.Text("Select a hack to use.")], '+str(layout)+']')
window = sg.Window('Morpheus 2.0', menulayout)

while True:
    buttonpressed = window.read()
    t=list({s for s in realcommands if realcommands[s]==buttonpressed[0]})
    if str(buttonpressed[0]) == 'None':
        quit()
    else:
        try:
            exec(t[0])
        except Exception as oops:
            window = sg.Window('Error', [[sg.Text('An error has occured: '+str(oops))], [sg.Button('Quit')]])
            window.read()
            window.close()
            quit()
