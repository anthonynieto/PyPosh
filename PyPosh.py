# Welcome to PyPosh v1.0
# Requirements: (1) Python 3.7 (2) Chrome (3) 1920 x 1080
# Mouse diagnostics: pyautogui.displayMousePosition()

import time
import pyautogui
from datetime import datetime

pyautogui.FAILSAFE = True

# Frequent functions
def pause(t):
    time.sleep(t)

def pgup(n):
    for pg in range(n):
        pyautogui.typewrite (['pageup'])
        pause(.50)

def up(n):
    for val in range(n):
        pyautogui.typewrite (['up'])
        pause(.20)

def populate(n):
    for num in range(n):
        pyautogui.typewrite (['end'])
        pause(1)

def share():
    pyautogui.click(817,372)

def freshset():
    pyautogui.click(1775,666)
    pause(.25)
    pyautogui.typewrite (['home'])
    pause(.25)
    pyautogui.typewrite (['f5'])
    pause(10)
    populate(30)
    pause(1)
        
# Diagnostic output (console+log) start
started = datetime.now()
slog = str(started)
print(f"PyPosh started: {started}")
file = open("log.txt", "a+")
file.write("Started: " + slog + "\n")

# Open Chrome
pause(.25)
pyautogui.moveTo(660, 1055, duration=.25)
pyautogui.click(660,1055)
pause(1)
pyautogui.moveTo(1070, 50, duration=.25)
pyautogui.click(1070,50)
pyautogui.typewrite ('https://poshmark.com/login')
pyautogui.typewrite (['enter'])
pause(3)

# Login to Poshmark
pyautogui.moveTo(864,489)
pyautogui.click(864,489)
pyautogui.typewrite ('EMAIL')
pause(.5)
pyautogui.moveTo(864,547)
pyautogui.click(864,547)
pause(.25)
pyautogui.typewrite ('PASSWORD')
pause(.25)
pyautogui.typewrite (['enter'])
pause(10)

# START program
pyautogui.click(1070,50)
pyautogui.typewrite ('https://poshmark.com/closet/USERNAME?availability=available')
pyautogui.typewrite (['enter'])
pause(3)

# Begin loop
populate(25)              
pause(1)
up(10)
pause(1.5)

def sharecloset(n):
    for num in range(n):

        # Set 1: 1st  item (top left)
        pyautogui.click (746,171)
        pause(5)
        share()
        pause(3)

        pyautogui.click (1016,169)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1275,170)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1545,170)
        pause(1)
        share()
        pause(1)

        # Set 1: 2nd row (middle)
        pyautogui.click (736,589)
        pause(.75)
        share()
        pause(.75)

        pyautogui.click (1010,589)
        pause(.75)
        share()
        pause(.75)

        pyautogui.click (1281,589)
        pause(.75)
        share()
        pause(.75)

        pyautogui.click (1548,589)
        pause(.75)
        share()
        pause(.75)

        # Set 1: 3rd row (bottom)
        pyautogui.click (739,1006)
        pause(.75)
        share()
        pause(.75)

        pyautogui.click (1007,1007)
        pause(.5)
        share()
        pause(.75)

        pyautogui.click (1275,1006)
        pause(.5)
        share()
        pause(.75)


        # Naviagte to Set 2
        pgup(1)
        up(11)
        pause(1)


        # Set 2: 1st row (top)
        pyautogui.click (742,174)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1006,174)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1281,174)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1550,174)
        pause(1)
        share()
        pause(1)

        # Set 2: 2nd row (middle)
        pyautogui.click (751,592)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,592)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,592)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1553,592)
        pause(.5)
        share()
        pause(.5)

        # Set 2: 3rd row (bottom)
        pyautogui.click (742,1011)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1006,1011)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,1011)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1553,1011)
        pause(.5)
        share()
        pause(.5)



        # Navigate to Set 3
        pgup(1)
        up(11)
        pause(1)


        # Set 3: 1st row (top)
        pyautogui.click (742,179)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1011,179)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1281,179)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1559,179)
        pause(1)
        share()
        pause(1)

        # Set 3: 2nd row (middle)
        pyautogui.click (742,596)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,596)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,596)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1544,596)
        pause(.5)
        share()
        pause(.5)

        # Set 3: 3rd row (bottom)
        pyautogui.click (742,1015)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1006,1015)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,1015)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1550,1015)
        pause(.5)
        share()
        pause(.5)


        # Navigate to Set 4
        pgup(1)
        up(11)
        pause(1)


        # Set 4: 1st row (top)
        pyautogui.click (743,182)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1011,182)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1281,182)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1550,182)
        pause(1)
        share()
        pause(1)

        # Set 4: 2nd row (middle)
        pyautogui.click (742,603)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,603)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1287,603)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1551,603)
        pause(.5)
        share()
        pause(3)

        # Set 4: 3rd row (bottom)
        # DON'T DO; we do in Set 5


        # Navigate to Set 5
        pgup(1)

        # Set 5: 1st row (top)
        pyautogui.click (736,165)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1017,165)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1281,165)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1550,165)
        pause(1)
        share()
        pause(1)

        # Set 5: 2nd row (middle)
        pyautogui.click (741,585)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,585)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,585)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1551,585)
        pause(.5)
        share()
        pause(.5)

        # Set 5: 3rd row (bottom)
        pyautogui.click (741,1003)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1006,1003)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,1003)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1551,1003)
        pause(.5)
        share()
        pause(2)


        # Navigate to Set 6
        pgup(1)
        up(11)

        # Set 6: 1st row (top)
        pyautogui.click (742,171)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1011,171)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1286,171)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1550,171)
        pause(1)
        share()
        pause(1)

        # Set 6: 2nd row (middle)
        pyautogui.click (743,588)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,588)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1275,588)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1550,588)
        pause(.5)
        share()
        pause(.5)

        # Set 6: 3rd row (bottom)
        pyautogui.click (741,1006)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,1006)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,1006)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1551,1006)
        pause(.5)
        share()
        pause(2)

        # Navigate to Set 7
        pgup(1)
        up(11)
        pause(1)

        # Set 7: 1st row (top)
        pyautogui.click (742,174)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1017,174)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1281,174)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1544,174)
        pause(1)
        share()
        pause(.75)

        # Set 7: 2nd row (middle)
        pyautogui.click (742,594)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1017,594)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1282,594)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1550,594)
        pause(.5)
        share()
        pause(.5)

        # Set 7: 3rd row (bottom)
        pyautogui.click (742,1011)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,1011)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,1011)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1550,1011)
        pause(.5)
        share()
        pause(1.5)

        # Navigate to Set 8
        pgup(1)
        up(11)
        pause(1)

        # Set 8: 1st row (top)
        pyautogui.click (745,179)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1011,179)
        pause(.5)
        share()
        pause(3)

        pyautogui.click (1275,179)
        pause(.75)
        share()
        pause(3)

        pyautogui.click (1551,179)
        pause(1)
        share()
        pause(1)

        # Set 8: 2nd row (middle)
        pyautogui.click (741,597)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,597)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1281,597)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1551,597)
        pause(.5)
        share()
        pause(.5)

        # Set 8: 3rd row (bottom)
        pyautogui.click (742,1015)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1011,1015)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1275,1015)
        pause(.5)
        share()
        pause(.5)

        pyautogui.click (1550,1015)
        pause(.5)
        share()
        pause(2)

        # REFRESH from HOME
        freshset()
        up(10)
        pause(1.5)

# Enter number of times to repeat sharing program
sharecloset(1)

# Diagnostics (console + output)
ended = datetime.now()
elog = str(ended)
file.write("Ended: " + elog + "\n")
file.close()
print(f"PyPosh ended: {ended}")

# Logoff Poshmark
pyautogui.moveTo(1597, 127, duration=1)
pyautogui.click (1597,127)
pause(1)
pyautogui.moveTo(1600,636, duration=1)
pyautogui.click (1600,636)
pause(5)

# Close Chrome
pyautogui.click (1895,10)
