#!/usr/bin/env python3
"""Return a foobang

Авторыбалка для майнкрафта.
При потере из виду крассного цвета,
нажимает правую кнопку миши, после
чего ждет 2 секунды

Для старта нажмите g для остановки h

"""
print("Fish bot V1")
print("g-start")
print("h-stop")
from ctypes import windll, Structure, c_long, byref 
# нужно для определения положения курсора
 
import time                                     # для пауз
import cv2                                      # для отпеределения цвета
import mss                                      # позволяет делать скриншоты очень быстро
import numpy                                    # нужно для определеия цвета (сумирования масок)
import pyautogui                                # нажатие на кнопку
import keyboard                                 # для работы с клавиатурой

class POINT(Structure):
    """Kласс для сохранения положения мыши"""
    _fields_ = [("x", c_long), ("y", c_long)]
 
def queryMousePosition():
    """Узнает положение мыши и возвращает его""" 
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

import LR1_Arseni_Zagreba                       #docstring
print(LR1_Arseni_Zagreba.__doc__)                
print(LR1_Arseni_Zagreba.queryMousePosition.__doc__)
help(LR1_Arseni_Zagreba.POINT)

sct = mss.mss()

while True:
    if keyboard.is_pressed('g'):
# если нажата Г то запустить в работу код
        while True:
            cur =  queryMousePosition()         # положение миши 
            mon = {"top": cur['y'] -150, "left": cur['x'] -20,
                   "width": 40, "height": 160} 
# сделать скриншот козле курсора таких то размеров
    
            img = numpy.asarray(sct.grab(mon))  # сохраняет скриншот 

            cv2.imshow("Fish bot V1", img)      # отображает скриншот


            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyALLWindows()
                break
    
# create hsv
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
# поиск крассного цвета
 
# define masks
# задача параметров крассного цвета который ищу, 
# 2 раза что б икать края диапазона
# lower mask (0-10)
            lower_red = numpy.array([0,50,50])
            upper_red = numpy.array([10,255,255])
            mask0 = cv2.inRange(hsv, lower_red, upper_red)
 
 # upper mask (170-180)
            lower_red = numpy.array([170,50,50])
            upper_red = numpy.array([180,255,255])
            mask1 = cv2.inRange(hsv, lower_red, upper_red)
 
# join masks
            mask = mask0+mask1
     
# check
            hasRed = numpy.sum(mask)

            if hasRed > 0:
                print("RED detected!") 
             
            else:
                print("RED NOT detected!")      
                pyautogui.click(button='right') # нажать правую кнопку
                time.sleep(2)
# ожидание 2 сек (для предотвращения двойных кликов)
            
            if keyboard.is_pressed('h'):  
# если нажата х выйти из цакла и ждать нажатия Г
                print("break")
                break

        time.sleep(1)                           # пауза в 1C
            
