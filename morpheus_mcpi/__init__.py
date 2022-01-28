# /bin/python3

# Made By FG6 (Bigjango)
# Credit to basedSkeleton
# Credit to Martin O'Hanlon (github: martinohanlon) for parts for the SafeWalk() code


import mcpi.minecraft as minecraft
import keyboard, math
from . import spectator_mode
import PySimpleGUI as sg
from time import sleep
from os.path import isfile

try:
    mc = minecraft.Minecraft.create()
    entityIds = mc.getPlayerEntityIds()
    mc.camera.setNormal(entityIds[0])
except:
    window = sg.Window(
        "Minecraft not detected",
        [[sg.Text("You need to open minecraft first")], [sg.Button("Quit")]],
    )
    window.read()
    window.close()
    quit()

realCommands = {
    "PlayerToPlayerTp()": "Teleport to player",
    "WaypointTeleport()": "Waypoint teleport",
    "FastBreak()": "Fast break",
    "SmartSpam()": "Spam From A List",
    "TrackPlayer()": "Track a player",
    "SmartLocationTeleport()": "Location teleport",
    "WhosOnline()": "Who's online",
    "SetBlock()": "setblock",
    "ExactLocationTeleport()": "Exact location teleport",
    "FreeCam()": "Freecam",
    "TeleportUp()": "Up",
    "SpamChat()": "Spam",
    "SafeWalk()": "Safewalk (glitchy)",
}
originalCommands = [
    "PlayerToPlayerTp()",
    "WaypointTeleport()",
    "FastBreak()",
    "SmartSpam()",
    "TrackPlayer()",
    "SmartLocationTeleport()",
    "WhosOnline()",
    "SetBlock()",
    "ExactLocationTeleport()",
    "FreeCam()",
    "TeleportUp()",
    "SpamChat()",
    "SafeWalk()",
]


def addCommand(command, name):
    global realCommands
    realCommands.update({command: name})
    if command in originalCommands:
        originalCommands.remove(command)


def PlayerToPlayerTp():
    entityIds = mc.getPlayerEntityIds()
    i = ""
    target = 1
    while i != "yes" and len(entityIds) != target:
        mc.camera.setFollow(entityIds[target])
        window = sg.Window(
            "Player to player Teleport",
            [[sg.Text("Is this them?")], [sg.Button("yes")], [sg.Button("no")]],
        )
        yesno = window.read()
        i = yesno[0]
        window.close()
        if i != "yes":
            target = target + 1

    if not i != "yes" and len(entityIds) != target:
        mc.player.setPos(mc.entity.getPos(entityIds[target]))

    else:
        window = sg.Window(
            "Player to player Teleport",
            [[sg.Text("Sorry, that is everyone")], [sg.Button("Quit")]],
        )
        window.read()
        window.close()

    mc.camera.setNormal(entityIds[0])


def TrackPlayer():
    entityIds = mc.getPlayerEntityIds()
    i = ""
    target = 1
    while i != "yes" and len(entityIds) != target:
        mc.camera.setFollow(entityIds[target])
        window = sg.Window(
            "Player Tracker",
            [[sg.Text("Is this them?")], [sg.Button("yes")], [sg.Button("no")]],
        )
        yesno = window.read()
        i = yesno[0]
        window.close()
        if i != "yes":
            target = target + 1
    if not i != "yes" and len(entityIds) != target:
        sleeptime = int(input("What is should the seconds between each report be? "))
        r = int(input("How mny times should I report on them? "))
        while r > 0:
            print(mc.entity.getPos(entityIds[target]))
            if r != 1:
                sleep(sleeptime)
            r = r - 1

    else:
        window = sg.Window(
            "Player to player Teleport",
            [[sg.Text("Sorry, that is everyone")], [sg.Button("Quit")]],
        )
        window.read()
        window.close()

    mc.camera.setNormal(entityIds[0])


def SmartLocationTeleport():
    layout = [
        [sg.Text("Location Teleport")],
        [sg.Text("X-pos:")],
        [sg.Input("")],
        [sg.Text("Z-pos:")],
        [sg.Input("")],
        [sg.Button("done")],
    ]
    window = sg.Window("Location Teleport", layout)
    yesno = window.read()
    cordList = yesno[1]
    x = cordList[0]
    z = cordList[1]
    window.close()
    try:
        y = mc.getHeight(float(x), float(z)) + 0.01
        mc.player.setPos(float(x), float(y), float(z))
    except:
        pass


def ExactLocationTeleport():
    layout = [
        [sg.Text("Exact Location Teleport")],
        [sg.Text("X-pos:")],
        [sg.Input("")],
        [sg.Text("Y-pos:")],
        [sg.Input("")],
        [sg.Text("Z-pos:")],
        [sg.Input("")],
        [sg.Button("done")],
    ]
    window = sg.Window("Exact Location Teleport", layout)
    yesno = window.read()
    cordList = yesno[1]
    x = cordList[0]
    y = cordList[1]
    z = cordList[2]
    window.close()
    try:
        mc.player.setPos(float(x), float(y), float(z))
    except:
        pass


def WhosOnline():
    entityIds = mc.getPlayerEntityIds()
    if len(entityIds) != 1:
        if len(entityIds) == 2:
            layout = [
                [
                    sg.Text(
                        "you and " + str(len(entityIds) - 1) + " other player is online"
                    )
                ],
                [sg.Button("ok")],
            ]
            window = sg.Window("Whos OnLine", layout)
            window.read()
        else:
            layout = [
                [
                    sg.Text(
                        "you and "
                        + str(len(entityIds) - 1)
                        + " other players are online"
                    )
                ],
                [sg.Button("ok")],
            ]
            window = sg.Window("Whos Online", layout)
            window.read()
    else:
        layout = [[sg.Text("Sadly, you are alone")], [sg.Button("ok")]]
        window = sg.Window("Whos OnLine", layout)
        window.read()
    window.close()


def SetBlock():
    layout = [
        [sg.Text("Setblock")],
        [sg.Text("what block (use block id)? ")],
        [sg.Input("")],
        [sg.Button("done")],
    ]
    window = sg.Window("Setblock", layout)
    setblock = window.read()
    setblock = setblock[1]
    setblock = setblock[0]
    try:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y + 1, z, int(setblock))
    except:
        pass
    window.close()


def FreeCam():
    spectator_mode.switch()


def SpamChat():
    layout = [
        [sg.Text("Spam")],
        [sg.Text("Message to spam: ")],
        [sg.Input("")],
        [sg.Text("Delay:")],
        [sg.Input("")],
        [sg.Button("done"), sg.Button("stop")],
    ]
    window = sg.Window("Spam", layout)
    spamInput = window.read()
    if spamInput[0] == "done":
        inputList = spamInput[1]
        message = inputList[0]
        sleeptime = inputList[1]
        if sleeptime == "s":
            sleeptime = message.strip().count(" ") - message.strip().count("  ") / 2.55
        else:
            try:
                sleeptime = float(sleeptime)
            except:
                sleeptime = 6
        while not keyboard.is_pressed("esc"):
            mc.postToChat(message)
            sleep(sleeptime)
    window.close()


def TeleportUp():
    x, y, z = mc.player.getPos()
    y = mc.getHeight(x, z) + 0.01
    mc.player.setPos(x, y, z)


def SmartSpam():
    layout = [
        [sg.Text("List Spam")],
        [sg.Text("File to spam from (include the path to it): ")],
        [sg.Input("")],
        [sg.Text("Amount:")],
        [sg.Input("")],
        [sg.Button("done"), sg.Button("stop")],
    ]
    window = sg.Window("List Spam", layout)
    spamInput = window.read()
    if spamInput[0] == "done":
        inputList = spamInput[1]
        message = inputList[0]
        amount = inputList[1]
        window.close()
        try:
            amount = int(amount)
        except:
            amount = 1
        if amount < 1:
            amount = 1
        if isfile(message) == True:
            sleeptime = message.strip().count(" ") - message.strip().count("  ") / 2.55
            spamList = open(message, "r")
            for i in range(amount):
                for line in spamList.readlines():
                    if not line.strip() == "":
                        mc.postToChat(line.strip().rstrip("?"))
                        if keyboard.is_pressed("esc"):
                            return 0
                        sleep(line.strip().count(" ") - line.strip().count("  ") / 6)
                        if keyboard.is_pressed("esc"):
                            return 0
                    else:
                        sleep(3)


def distance(x, y, z, x2, y2, z2):
    xd = x2 - x
    yd = y2 - y
    zd = z2 - z
    return math.sqrt((xd * xd) + (yd * yd) + (zd * zd))


def WaypointTeleport():
    window = sg.Window(
        "Waypoint Teleport",
        [
            [
                sg.Text(
                    "Click 'set' to save this location, then click 'use' to return to it"
                )
            ],
            [sg.Button("Use")],
            [sg.Button("Set")],
            [sg.Button("Cancel")],
        ],
    )
    yesno = window.read()
    i = yesno[0]
    window.close()
    if i == "Set":  # making it so you can actually save a location
        global wayx, wayy, wayz
        wayx, wayy, wayz = mc.player.getPos()
        file = open(
            "morpheus.ini", "w"
        )  # making the location saved stay even when the game is closed
        file.write(
            "[morpheus]\nwayx: "
            + "'"
            + str(wayx)
            + "'\nwayy: "
            + "'"
            + str(wayy)
            + "'\nwayz"
            + "'"
            + str(wayz)
            + "'"
        )  # write to file
        file.close  # done
    if i == "Use":  # changing the variables so they don't get overwritten
        mc.player.setPos(wayx, wayy, wayz)


def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))


def SafeWalk():
    
    window = sg.Window(
        "Warning",
        [[sg.Text("Do not try this in singleplayer. Sneak to place blocks below.")], [sg.Button("OK")]],
    )
    window.read()
    window.close()
    
    mc = minecraft.Minecraft.create()
    lastPlayerPos = mc.player.getPos()
    while not keyboard.is_pressed("esc"):
        playerPos = mc.player.getPos()
        mc.setBlock(playerPos.x, playerPos.y - 1, playerPos.z, 246)
        movementX = lastPlayerPos.x - playerPos.x
        movementZ = lastPlayerPos.z - playerPos.z
        if (
            (movementX < -0.2)
            or (movementX > 0.2)
            or (movementZ < -0.2)
            or (movementZ > 0.2)
        ):
            nextPlayerPos = playerPos
            while (int(playerPos.x) == int(nextPlayerPos.x)) and (
                int(playerPos.z) == int(nextPlayerPos.z)
            ):
                nextPlayerPos = minecraft.Vec3(
                    nextPlayerPos.x - movementX,
                    nextPlayerPos.y,
                    nextPlayerPos.z - movementZ,
                )
            blockBelowPos = roundVec3(nextPlayerPos)
            if blockBelowPos.z < 0:
                blockBelowPos.z = blockBelowPos.z - 1
            if blockBelowPos.x < 0:
                blockBelowPos.x = blockBelowPos.x - 1
            blockBelowPos.y = blockBelowPos.y - 1
            mc.setBlock(blockBelowPos.x, blockBelowPos.y, blockBelowPos.z, 246)
            lastPlayerPos = playerPos


def FastBreak():
    while not keyboard.is_pressed("esc"):
        x, y, z = mc.player.getPos()
        for change_y in range(0, 3):
            for change_x in range(-2, 2):
                for change_z in range(-2, 2):
                    if mc.getBlock(x + change_x, y + change_y, z + change_z) != 0:
                        mc.setBlock(x + change_x, y + change_y, z + change_z, 38)


def getGuiLayout(commandList):
    menulayout = []
    for commander in commandList:
        menulayout.append([sg.Button(commandList[commander])])

    return menulayout


def start():
    window = sg.Window("Morpheus 2 Minecraft Hack", getGuiLayout(realCommands))
    while True:
        buttonpressed = window.read()
        t = list({s for s in realCommands if realCommands[s] == buttonpressed[0]})
        if str(buttonpressed[0]) == "None":
            quit()
        else:
            try:
                if t[0] in originalCommands:
                    method_name = t[0][:-2]
                    possibles = globals().copy()
                    possibles.update(locals())
                    method = possibles.get(method_name)
                    method()
                else:
                    getattr(__main__, t[0][:-2])()
            except Exception as oops:
                window = sg.Window(
                    "Error",
                    [
                        [
                            sg.Text(
                                "Sorry, something went wrong. Error message: "
                                + str(oops)
                            )
                        ],
                        [sg.Button("Quit")],
                    ],
                )
                window.read()
                window.close()
                quit()


if __name__ == "__main__":
    start()
