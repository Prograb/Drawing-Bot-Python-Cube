import time, os
import pyautogui as pya

os.system("mspaint.exe")

time.sleep(0.9)

distance = 200


while distance:
    pya.dragRel(distance, 0,duration=0.1)
    distance = distance -5
    pya.dragRel(0, distance, duration=0.1)
    pya.dragRel(-distance, 0, duration=0.1)
    distance = distance - 5
    pya.dragRel(0, -distance, duration=0.1)
