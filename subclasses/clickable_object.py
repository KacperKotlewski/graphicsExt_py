import graphics as gr

class ClickableObject(gr.GraphicsObject):

    def __init__(self, p1, p2):
        gr.GraphicsObject.__init__(self, ["outline", "fill"])
        self.p1 = p1.clone()
        self.p2 = p2.clone()
        self.visible = False
        self.graphwin = None

    def __repr__(self):
        return "ClickableObject({}, {})".format(str(self.p1), str(self.p2))

    def checkClick(self, mouse):
        if(mouse != None):
            if( (mouse.x > self.p1.x and mouse.x < self.p2.x) and (mouse.y > self.p1.y and mouse.y < self.p2.y) ):
                print("clicked")


    def setOutline(self, color):
        self._reconfig("outline", color)
        self._setOutline(color)
    def _setOutline(self, color):
        pass

    def setFill(self, color):
        self._reconfig("fill", color)
        self._setFill(color)
    def _setFill(self, color):
        pass


    def draw(self, graphwin):
        self.graphwin = graphwin
        self.visible = True
        self._draw(graphwin)
    def _draw(self, graphwin):
        pass

    def undraw(self):
        self.visible = False
        self._undraw()
    def _undraw(self):
        pass

    def getP1(self): return self.p1.clone()
    def getP2(self): return self.p2.clone()
    def getCenter(self):
        p1 = self.p1
        p2 = self.p2
        return gr.Point((p1.x+p2.x)/2.0, (p1.y+p2.y)/2.0)


    def clone(self):
        other = ClickableObject(self.p1, self.p2)
        other.config = self.config.copy()
        other.visible = self.visible
        other.graphwin = self.graphwin
        return other
