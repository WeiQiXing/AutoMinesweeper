# coding:gbk

import pyautogui
from GlobalData import MineData
from Analysis import *
from Identify import *
from Control import *

pyautogui.PAUSE = 0.005
panel, size, facePanel = findPanel()
if size == (8, 8):
    mineSum = 10
elif size == (16, 16):
    mineSum = 40
elif size == (30, 16):
    mineSum = 99
else:
    mineSum = input(u"��������������")
MineData(size, mineSum)

while True:
    # gameStatus = getGameStatus(facePanel)
    # if gameStatus is not None:
    #     if gameStatus:
    #         exit(0)
    #     else:
    #         exit(1)
    identify(panel, size)
    if MineData.status is not None:
        break
    divideInOut(size)
    findByOne(size)
    if clickWhole(panel, size, 'lr'):
        pyautogui.moveTo((1, 1))
        print u"�������ж�"
    else:
        findByTwo(size)
        if clickWhole(panel, size, 'lr'):
            pyautogui.moveTo((1, 1))
            print u"�������ж�"
        else:
            x, y = findByProbability(size)
            print u"����ѡ��һ��"
            click(panel, (x, y), 'left')
            pyautogui.moveTo((1, 1))
