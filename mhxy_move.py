# https://www.python100.com/html/242WYDUG23Q0.html
# 需要管理员权限运行
import time
import pyautogui
from loguru import logger
import pydirectinput
time.sleep(3)
# pyautogui.moveTo(50, 30, duration=1)

x, y = pyautogui.position()

logger.info('x:{},y:{}', x, y)

pydirectinput.moveRel(xOffset=50, yOffset=50, duration=0.4, relative=True)
# pydirectinput.moveTo(100, 150) # 移动鼠标至坐标100，150

# pyautogui.moveTo(x+5, y+30, duration=1)
