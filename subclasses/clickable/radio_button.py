from subclasses.clickable.checkbox_familly import _CheckboxFamilly
from subclasses.main_classes.function_handler import FunctionHolder
import graphics as gr

class RadioButton(_CheckboxFamilly):
    def __init__(self, p1:gr.Point, radius:int=8, spaceSize:int=3, checked:bool=False, onclick:FunctionHolder = None):
        self.outlinecircle = gr.Circle(p1,radius)
        self.innercircle = gr.Circle(p1, abs(radius-spaceSize) )
        self.anchor = p1.clone()
        _CheckboxFamilly.__init__(self, gr.Point(p1.x-radius, p1.y-radius), gr.Point(p1.x+radius, p1.y+radius), spaceSize=spaceSize, checked=checked, onclick=onclick)
        self.radius = radius

    def __repr__(self):
        return "RadioButton({}, {}, {})".format(str(self.p1), str(self.p2), str(self.checked))

    def getAnchor(self): return  self.anchor.clone()

    def _setupElemColors(self):
        self.outlinecircle.setOutline(self.config["outline"])
        self.outlinecircle.setFill(self.config["fill"])
        if(self.checked == True):
            self.innercircle.setFill(self.config["outline"])
            self.innercircle.setOutline(self.config["outline"])
        else:
            self.innercircle.setFill(self.config["fill"])
            self.innercircle.setOutline(self.config["fill"])

    def setSpaceSize(self, spaceSize:int):
        self.spaceSize = spaceSize
        self.innercircle.radius = self.radius-self.spaceSize
        self._recreateCircles()

    def setRadious(self, radius:int):
        self.radius = radius
        self.outlinecircle.radius = self.radius
        self.setSpaceSize(self.spaceSize)

    def _recreateCircles(self):
        self.outlinecircle.undraw()
        self.innercircle.undraw()
        oldCircle = self.outlinecircle
        self.outlinecircle = gr.Circle(oldCircle.getCenter(), oldCircle.radius)
        oldCircle = self.innercircle
        self.innercircle = gr.Circle(oldCircle.getCenter(), oldCircle.radius)
        if(self.graphwin != None and self.config["visible"]):
            self.innercircle.draw(self.graphwin)
            self.outlinecircle.draw(self.graphwin)
        self.p1 = gr.Point(self.anchor.x - self.radius,self. anchor.y - self.radius)
        self.p2 = gr.Point(self.anchor.x + self.radius, self.anchor.y + self.radius)
        self._setupElemColors()

    def _draw(self, graphwin:gr.GraphWin):
        self.outlinecircle.draw(graphwin)
        self.innercircle.draw(graphwin)

    def _undraw(self):
        self.outlinecircle.undraw()
        self.innercircle.undraw()

    def _move(self, dx:int, dy:int):
        self.outlinecircle.move(dx,dy)
        self.innercircle.move(dx,dy)
        self.anchor.move(dx, dy)
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def clone(self):
        other = RadioButton(self.p1, self.radious, self.spaceSize, self.checked, self.onclickFunc)
        other.config = self.config.copy()
        other.graphwin = self.graphwin
        return other
