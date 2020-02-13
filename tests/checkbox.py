from graphicsExtended import *
from graphics import *

try:
    win = GraphExtWin("form", 200, 200)
    win.setBackground(color_rgb(240,240,240))

    chb1 = ClickableObject.factory(Checkbox, SquarePoint(Point(40,40)))
    chb1.draw(win)
    chb2 = Checkbox(Point(160,40), Point(180,60), 5, True)
    chb2.draw(win)

    while True:
        mouse = win.checkMouse()
        chb1.checkClick(mouse)
        chb2.checkClick(mouse)
except GraphicsError:
    pass