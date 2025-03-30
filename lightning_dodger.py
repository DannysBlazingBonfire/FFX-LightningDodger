import pyautogui
import pydirectinput
import time

lightning_counter = 0

def DodgeLightning():
    if(pyautogui.pixelMatchesColor(x=10, y=10, expectedRGBColor=(206, 206, 254), tolerance=10)):
        global lightning_counter
        lightning_counter += 1

        pydirectinput.press('enter')
        print("Lightnings dodged: " + str(lightning_counter))
        time.sleep(1)     

def main():
    pyautogui.PAUSE=0.00

    while True:
        DodgeLightning()

if __name__ == "__main__":
    main()