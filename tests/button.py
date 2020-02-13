from graphicsExtended import *
from graphics import *

try:
    win = GraphExtWin("form", 200, 200)
    win.setBackground(color_rgb(240,240,240))

    btn1 = Button(Point(10,10), Point(100,50), "text")
    btn1.draw(win)

    btn2 = ClickableObject.factory(Button, SquarePoint(Point(10,70), width=150))
    btn2.setText("text2")
    btn2.draw(win)


    def hello(c:int):
        c["count"] += 1
        print("count=",format(str(c["count"])))
    btn2.additional = {"count":0}
    btn2.onClick(FunctionHolder(hello, {"c":btn2.additional}))

    while True:
        mouse = win.checkMouse()
        btn1.checkClick(mouse)
        btn2.checkClick(mouse)

except GraphicsError:
    pass