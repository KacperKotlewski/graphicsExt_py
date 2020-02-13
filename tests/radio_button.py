from graphicsExtended import *
from graphics import *

try:
    win = GraphExtWin("form", 200, 200)
    win.setBackground(color_rgb(240,240,240))

    print(SquarePoint(Point(40,40)))
    rb1 = ClickableObject.factory(RadioButton, SquarePoint(Point(40,40)))
    rb1.draw(win)
    rb2 = RadioButton(Point(160,40))
    rb2.draw(win)
    rb1.setRadious(30)

    while True:
        mouse = win.checkMouse()
        rb1.checkClick(mouse)
        rb2.checkClick(mouse)
except GraphicsError:
    pass