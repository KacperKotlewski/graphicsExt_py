from graphicsExtended import *
from graphics import *
import time

try:
    #"""
    win = GraphExtWin("Calculator", 200, 200)
    win.setBackground(color_rgb(240,240,240))

    checkbox = Checkbox(Point(10,10), Point(30,30))
    text = Text(Point(50,50), "xd")
    btn1 = Button(Point(50,10), Point(130,30), "text")
    btn2 = Button(Point(50,50), Point(130,70), text)
    rect = Rectangle(Point(100,100), Point(130,130))
    checkbox.draw(win)
    rect.draw(win)
    btn1.draw(win)
    btn2.draw(win)


    while True:
        time.sleep(0.1)
        mouse = win.checkMouse()
        checkbox.checkClick(mouse)
        btn1.checkClick(mouse)
        btn2.checkClick(mouse)
        print()
        print(mouse)
    #"""

except:
    win.close()