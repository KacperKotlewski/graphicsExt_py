import graphics as gr
import graphicsExtended as ge

class ClickableObject(gr.GraphicsObject):
    def factory(factory_type, square_point:ge.SquarePoint, onclick:ge.FunctionHolder = None):
        temp = None
        if(factory_type == ClickableObject): temp = ClickableObject(square_point.getP1(), square_point.getP2())
        elif(factory_type == ge.Checkbox): temp = ge.Checkbox(square_point.getP1(), square_point.getP2())
        elif(factory_type == ge.Button): temp = ge.Button(square_point.getP1(), square_point.getP2())
        elif(factory_type == ge.RadioButton): temp = ge.RadioButton(square_point.getP1())
        if(temp != None):
            if(onclick != None): temp.onclickFunc=onclick
            return temp
        else:
            assert 0, ("Bad  type of factory_type 'ClickableObject(factory_type, square_point)': "+format(str(factory_type)))

    factory = staticmethod(factory)

    def __init__(self, p1:gr.Point, p2:gr.Point, onclick:ge.FunctionHolder=None):
        gr.GraphicsObject.__init__(self, ["outline", "fill"])
        self.p1 = p1.clone()
        self.p2 = p2.clone()
        self.box = gr.Rectangle(p1, p2)
        self.config["visible"] = False
        self.onclickFunc = None
        self.graphwin = None

    def __repr__(self):
        return "ClickableObject({}, {})".format(str(self.p1), str(self.p2))

    def onClick(self, onClick:ge.FunctionHolder):
        self.onclickFunc = onClick

    def checkClick(self, mouse):
        clicked = False
        if(mouse != None):
            if( (mouse.x > self.p1.x and mouse.x < self.p2.x) and (mouse.y > self.p1.y and mouse.y < self.p2.y) ):
                self._clicked()
                if type(self.onclickFunc) == ge.FunctionHolder:
                    self.onclickFunc.run()
                clicked=True
        elif(not clicked):
            self._notClicked()

    def _clicked(self): pass
    def _notClicked(self): pass


    def setOutline(self, color):
        self._reconfig("outline", color)
    def _setOutline(self, color):
        pass

    def setFill(self, color):
        self._reconfig("fill", color)
    def _setFill(self, color):
        pass


    def draw(self, graphwin:gr.GraphWin):
        self.graphwin = graphwin
        self.config["visible"] = True
        self._draw(graphwin)
    def _draw(self, graphwin:gr.GraphWin):
        self.box.p1 = self.getP1()
        self.box.p2 = self.getP2()
        self.box.draw(graphwin)

    def undraw(self):
        self.config["visible"] = False
        self._undraw()
    def _undraw(self):
        self.box.undraw()

    def _move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def redraw(self, graphwin:gr.GraphWin):
        self.undraw()
        self.draw(graphwin)

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

