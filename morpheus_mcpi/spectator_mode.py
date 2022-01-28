import mcpi.minecraft as minecraft
import keyboard
from time import sleep


def switch():
    mc = minecraft.Minecraft.create()
    x, y, z = mc.player.getPos()
    cx, cy, cz = x, y, z
    mc.camera.setFixed()
    mc.camera.setPos(x, y, z)

    while True:
        if keyboard.is_pressed("w"):
            cz = cz + 1
            mc.player.setPos(x, y, z)
            mc.camera.setPos(cx, cy, cz)
            sleep(0.01)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("s"):
            cz = cz - 1
            mc.player.setPos(x, y, z)
            mc.camera.setPos(cx, cy, cz)
            sleep(0.01)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("d"):
            cx = cx - 1
            mc.player.setPos(x, y, z)
            mc.camera.setPos(cx, cy, cz)
            sleep(0.01)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("a"):
            cx = cx + 1
            mc.player.setPos(x, y, z)
            mc.camera.setPos(cx, cy, cz)
            sleep(0.01)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("space"):
            cy = cy + 1
            mc.player.setPos(x, y, z)
            mc.camera.setPos(cx, cy, cz)
            sleep(0.01)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("shift"):
            cy = cy - 1
            mc.player.setPos(x, y, z)
            mc.camera.setPos(cx, cy, cz)
            sleep(0.01)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("esc"):
            mc.player.setPos(x, y, z)
            mc.camera.setNormal()
            break
        elif keyboard.is_pressed("up"):
            cz = cz + 1
            mc.camera.setPos(cx, cy, cz)
            mc.player.setPos(x, y, z)
            sleep(0.1)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("down"):
            cz = cz - 1
            mc.camera.setPos(cx, cy, cz)
            mc.player.setPos(x, y, z)
            sleep(0.1)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("right"):
            cx = cx - 1
            mc.camera.setPos(cx, cy, cz)
            mc.player.setPos(x, y, z)
            sleep(0.1)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("left"):
            cx = cx + 1
            mc.camera.setPos(cx, cy, cz)
            mc.player.setPos(x, y, z)
            sleep(0.1)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("o"):
            cy = cy + 1
            mc.camera.setPos(cx, cy, cz)
            mc.player.setPos(x, y, z)
            sleep(0.1)
            mc.player.setPos(x, y, z)
        elif keyboard.is_pressed("l"):
            cy = cy - 1
            mc.camera.setPos(cx, cy, cz)
            mc.player.setPos(x, y, z)
            sleep(0.1)
            mc.player.setPos(x, y, z)


if __name__ == "__main__":
    switch()
