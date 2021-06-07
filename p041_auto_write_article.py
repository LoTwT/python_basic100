# 自动写文档
import pyautogui
import pyperclip
import time

content = "abcdefghijklmnopqrstuvwxyz"

time.sleep(2)

pyautogui.click(600, 400)

for s in content:
    pyperclip.copy(s)
    pyautogui.hotkey("ctrl", "v")
