import pyautogui as gui
import time

# VARIANT: Tries to fish for all 3 rarity colors. Reapplies buffs every 6 loops.

# Screen size: 1920x1080px
# Sonar potion Region (left, top, width, height): [915, 527, 129, 38]
# Wooden Crate (green rarity): RGB: 131, 130, 242
# Iron/Biome Crate (blue rarity): RGB: 136, 232, 148
# Golden Crate (orange rarity): RGB (approximate): 255, 200, 150


### STATS:
# Trial 1 (6 minutes):
    # Downtime (fishing line not casted): 35%
    # Misses: 8 (goodbye, golden crate...)
    # Lines broken: 8 (I need that fishing line accessory ong)

# TODO: See if checking the pixels not being white rarity (bass, trash, etc.) results in more efficient loop times
# IDEA: Remove fishing potions out of the equation, since my base fishing power (w/ Angler armor + golden fishing rod) is 100+

rarities = {'green': (131, 130, 242), 'blue': (136, 232, 148), 'orange': (255, 200, 150)}

loopCount = 0  # 1 Loop is approximately 45s when checking all 3 rarities (green, blue, orange)

while loopCount < 50: 
    for currX in range(938, 980):
        for currY in range(538, 552):
            for rarity in rarities:
                if (gui.pixelMatchesColor(currX, currY, rarities[rarity], tolerance=30)):
                     gui.mouseDown(x=960, y=900) # Catching the fish/crate
                     time.sleep(0.05) # Necessary sleep time for mouse click to register
                     gui.mouseUp()
                     time.sleep(0.05)
                     gui.mouseDown(x=960, y=900) # Casting the line again
                     time.sleep(0.05)
                     gui.mouseUp()
                     print('MEOW! Rarity: ', rarity, ' caught!')
    loopCount += 1
    print('DEBUG: Loop Count: ', loopCount)
    gui.mouseDown(x=960, y=900) # 'Safety' throw to reset fishing bobber every loop
    time.sleep(0.05)
    gui.mouseUp()
    if (loopCount % 6 == 0):
        gui.typewrite("b", interval=0.25) # Rebuffs, using a fishing, crate and sonar potion (~every 4.5 minutes)
        print('DEBUG: Rebuffing!')


print("DEBUG: End of code execution.")
