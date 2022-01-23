# Morpheus 2.0
A use of the python MCPI to enhance the multiplayer and singleplayer gameplay.
## To Use:
You will need to install the keyboard, pysimplegui, and MCPI python modules and you will need to execute it as root. if anything goes wrong just use Esc to stop it (Or worst case, use Ctrl+C in the shell)
## To Install:
Run this in terminal (Ctrl+C and Ctrl+Shift+V)
```bash
sudo pip3 install keyboard pysimplegui mcpi
git clone https://github.com/bigjango13/Morpheus-2
```
## To Run:
```bash
sudo python3 Morpheus-2/Morpheus.py
```
## Features:
### Player Teleport
This will teleport your player to any other player in the server, you use the yes and no buttons to pick who you teleport to.
### Waypoint Teleport
You can use this to save a location and then teleport back to it. (One of the many uses of this is when you die, save your location and then teleport back to it after you respawn.)
### Location Teleport
This will teleport your player to a certain XZ coordinates, you will not need to input the Y becuase the program automagically brings you to the top-most non-air block. (if you want to teleport to a XYZ location please use "Exact Location Teleport")
### Exact Location Teleport
This will teleport your player to an XYZ location.
### Player Tracker
This will print the XYZ locaton of a target player over time, can be used to find bases.
### Online Players
This will tell you the amount of players on the server that you are in.
### FreeCam
This allows you to look around without moving your player, the controls are "w" (fast forward), "a" (fast left), "d" (fast right), "s" (fast back), "Shift" (Fast Down), "Space" (Fast up), "Up arrow" (slow forward), "left arrow" (slow left), "right arrow" (slow right), "back arrow" (slow back), "l" (slow Down), "o" (slow up)
### Teleport up
This will teleport you to the highest non-air block.
### Chat Spammer
This can spam a single message in chat.
### Spam from a list
This can spam lines from a file. (good for singing/rickrolling in chat)
### Safewalk
This can be used to walk on air. (Only works on servers, else it will place blocks)
### Fast Break
This allows you to break blocks on server faster (You can use it to get bedrock in survival mode) DO NOT USE IN SINGLE PLAYER!!
### Set Block
This will set a block on your head.
## The API
While there are many things that you can do with just Morpheus, there is an easy way to add more features with the API.
Here is an example of adding a command:
```python
import Morpheus

def exampleFunction():
   print('This is an example.')

Morpheus.addCommand('exampleFunction()', 'Example API function')
Morpheus.start()
```
fisrt you import Morpheus and add a command called `"Example API function"` which calls the function `exampleFunction()`.
After you have added all fo your custom hacks with `Morpheus.addCommand('function', 'name')` you can run `Morpheus.start()` to start Morpheus.
