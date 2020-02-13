from graphicsExtended import *
from graphics import *

try:
    win = GraphExtWin("form", 200, 200)
    win.setBackground(color_rgb(240,240,240))

    sp1 = SquarePoint(Point(10,10))
    sp1.draw(win)
    sp2 = SquarePoint(Point(50,10), width=100)
    sp2.draw(win)
    sp3 = SquarePoint(Point(10,50), height=100)
    sp3.draw(win)
    sp4 = SquarePoint(Point(50,50), 100, 100)
    sp4.draw(win)

    while True:
        mouse = win.checkMouse()
        
except GraphicsError:
    pass