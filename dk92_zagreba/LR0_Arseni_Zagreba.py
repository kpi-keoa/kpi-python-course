print("Fish bot V1")
print("g-start")
print("h-stop")
from ctypes import windll, Structure, c_long, byref
 
import time
import cv2
import mss
import numpy
import pyautogui
import keyboard  
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
 
def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

 
def click():
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()



sct = mss.mss()
#last_time = time.time()
while True:
    if keyboard.is_pressed('g'):
        #cv2.destroyALLWindows()
        while True:
            cur =  queryMousePosition()
            mon = {"top": cur['y'] -150, "left": cur['x'] -20, "width": 40, "height": 160}
    
            img = numpy.asarray(sct.grab(mon))

            cv2.imshow("Fish bot V1", img)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyALLWindows()
                break
    
        # create hsv
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
    # define masks
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
                print("RED detected!") # do nothing
                #pass
            else:
                print("RED NOT detected!") # catch!       
                pyautogui.click(button='right')
                time.sleep(2)
            
            if keyboard.is_pressed('h'):  # if key 'p' is pressed
                print("break")
                break
        #cv2.destroyALLWindows()
        time.sleep(1)
            
#from mss import mss

#with mss() as sct:
       # sct.shot(mon=0)
