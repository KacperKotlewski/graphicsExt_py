from subclasses.main_classes.clickable_object import ClickableObject
from subclasses.main_classes.function_handler import FunctionHolder
import graphics as gr

class _CheckboxFamilly(ClickableObject):
    def __init__(self, p1:gr.Point, p2:gr.Point, spaceSize:int=5, checked:bool=False, onclick:FunctionHolder=None):
        ClickableObject.__init__(self, p1, p2, onclick=onclick)
        self.spaceSize = spaceSize
        self.checked = checked
        self.outlinebox = gr.Rectangle(p1, p2)
        self.innerbox = gr.Rectangle(gr.Point(p1.x+spaceSize, p1.y+spaceSize), gr.Point(p2.x-spaceSize, p2.y-spaceSize) )
        self._setupElemColors()

    def __repr__(self):
        return "_CheckboxFamilly({}, {}, {})".format(str(self.p1), str(self.p2), str(self.checked))

    def _setOutline(self, color):
        self._reconfig("outline", color)
        self._setupElemColors()

    def _setFill(self, color):
        self._reconfig("fill", color)
        self._setupElemColors()

    def _setupElemColors(self):
        self.outlinebox.setOutline(self.config["outline"])
        self.outlinebox.setFill(self.config["fill"])
        if(self.checked == True):
            self.innerbox.setFill(self.config["outline"])
            self.innerbox.setOutline(self.config["outline"])
        else:
            self.innerbox.setFill(self.config["fill"])
            self.innerbox.setOutline(self.config["fill"])

    def _clicked(self):
        self.checked = not self.checked
        self._setupElemColors()

    def setSpaceSize(self, spaceSize):
        self.spaceSize = spaceSize
        self.innerbox.p1.x = self.p1.x + spaceSize
        self.innerbox.p1.y = self.p1.y + spaceSize
        self.innerbox.p2.x = self.p2.x - spaceSize
        self.innerbox.p2.y = self.p2.y - spaceSize
        if(self.graphwin != None and self.config["visible"]):
            self.redraw()

    def _draw(self, graphwin):
        self.outlinebox.draw(graphwin)
        self.innerbox.draw(graphwin)

    def _undraw(self):
        self.outlinebox.undraw()
        self.innerbox.undraw()

    def _move(self, dx, dy):
        self.outlinebox.move(dx,dy)
        self.innerbox.move(dx,dy)
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def clone(self):
        other = _CheckboxFamilly(self.p1, self.p2, self.spaceSize, self.checked, self.onclickFunc)
        other.config = self.config.copy()
        other.graphwin = self.graphwin
        return other
