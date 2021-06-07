# 聊天轰炸
import pyautogui
import pyperclip
import time

content = """
要发送的内容
"""

# 聊天窗口坐标
x = 0
y = 0

time.sleep(5)

for line in content.split("\n"):
    if line:
        pyautogui.click(x, y)
        pyperclip.copy(line)
        pyautogui.hotkey("ctrl", "v")
