from subclasses.clickable_object import ClickableObject
import graphics as gr

class Checkbox(ClickableObject):
    def __init__(self, p1, p2, spaceSize=2, checked=False):
        ClickableObject.__init__(self, p1, p2)
        self.spaceSize = spaceSize
        self.checked = checked
        self.outlinebox = gr.Rectangle(p1, p2)
        self.innerbox = gr.Rectangle(gr.Point(p1.x+spaceSize, p1.y+spaceSize), gr.Point(p2.x-spaceSize, p2.y-spaceSize) )
        self._setupElemColors()

    def __repr__(self):
        return "Checkbox({}, {}, {})".format(str(self.p1), str(self.p2), str(self.checked))

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

    def checkClick(self, mouse):
        if(mouse != None):
            if( (mouse.x > self.p1.x and mouse.x < self.p2.x) and (mouse.y > self.p1.y and mouse.y < self.p2.y) ):
                self.checked = not self.checked
                self._setupElemColors()

    def setSpaceSize(self, spaceSize):
        self.spaceSize = spaceSize
        self.innerbox.p1.x = self.p1.x + spaceSize
        self.innerbox.p1.y = self.p1.y + spaceSize
        self.innerbox.p2.x = self.p2.x - spaceSize
        self.innerbox.p2.y = self.p2.y - spaceSize
        if(self.graphwin != None and self.visible):
            self.innerbox.undraw()
            self.innerbox.draw(self.graphwin)

    def _draw(self, graphwin):
        self.outlinebox.draw(graphwin)
        self.innerbox.draw(graphwin)

    def _undraw(self):
        self.outlinebox.undraw()
        self.innerbox.undraw()

    def _move(self, dx, dy):
        self.outlinebox.move(dx,dy)
        self.innerbox.move(dx,dy)

    def clone(self):
        other = Checkbox(self.p1, self.p2, self.spaceSize, self.checked)
        other.config = self.config.copy()
        other.visible = self.visible
        other.graphwin = self.graphwin
        return other
