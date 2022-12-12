import pyautogui
import time
time.sleep(3)
for i in range(50):
  pyautogui.typewrite("Hello")
  pyautogui.press("Enter")
