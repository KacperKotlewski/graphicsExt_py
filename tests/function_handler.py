from graphicsExtended import *
from graphics import *

try:
    win = GraphExtWin("form", 200, 200)
    win.setBackground(color_rgb(240,240,240))

    def func(arg = None, arg2:int = None):
        print("arguments in function: arg=",arg,", arg2=",arg2)

    f1 = FunctionHolder(func, {"arg":"xyz"})
    f1.getFunctionAttribs()
    f1.run()
    f1.setArguments({"arg2":5})
    f1.run()
    f1.addArguments({"arg":"nice"})
    f1.run()

    f2 = FunctionHolder(func)
    f2.addArguments({"arg":"xdd"})
    f2.run()

    print("function list")
    funcs = FunctionList()
    funcs.add(f1)
    funcs.add(f2)
    funcs.runAll()
    funcs.remove(f2)
    funcs.runAll()

    while True:
        mouse = win.checkMouse()
except GraphicsError:
    pass