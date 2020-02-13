from graphicsExtended import *
from graphics import *

try:
    win = GraphExtWin("form", 200, 200)
    win.setBackground(color_rgb(240,240,240))

    def printNameAndPos(object:ClickableObject):
        print("name=",object)
        print("point=",object.p1)

    cl1 = ClickableObject(Point(160,40), Point(180,60))
    cl1.onClick(FunctionHolder(printNameAndPos, {"object":cl1}))
    cl1.draw(win)

    cl2 = ClickableObject.factory(ClickableObject, SquarePoint(Point(40,40)), FunctionHolder(printNameAndPos, {"object":cl1}))
    cl2.draw(win)

    while True:
        mouse = win.checkMouse()
        cl1.checkClick(mouse)
        cl2.checkClick(mouse)
except GraphicsError:
    pass