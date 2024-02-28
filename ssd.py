import pyautogui
import random
import time

typeA=["pagal,","motti","stupid"]
while True:
    final=random.choice(typeA)

    pyautogui.typewrite(f"you are {final}")
    pyautogui.press('enter')
    time.sleep(10)