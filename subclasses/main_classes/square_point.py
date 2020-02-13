import graphics as gr

class SquarePoint(gr.GraphicsObject):
    def __init__(self, point=gr.Point(0,0), width=20, height=20):
        gr.GraphicsObject.__init__(self, ["outline", "fill"])
        self.point = point.clone()
        self.width = width
        self.height = height
        self.box = gr.Rectangle(self.getP1(), self.getP2())

    def __repr__(self):
        return "SquarePoint(p={}, w={}, h={})".format(str(self.point), str(self.width), str(self.height))

    def getP1(self): return self.point.clone()
    def getP2(self): return gr.Point(self.point.x + self.width, self.point.y + self.height).clone()

    def setWidth(self, width): self.width = width
    def setHeight(self, height): self.height = height
    def setP1(self, point): self.point = point
    def setP2(self, point):
        self.width = point.x
        self.height = point.y

    def _move(self, dx, dy):
        self.p1.move(dx, dy)

    def draw(self, graphwin):
        self.box.p1 = self.getP1()
        self.box.p2 = self.getP2()
        self.box.draw(graphwin)

    def undraw(self):
        self.box.undraw()

    def redraw(self):
        self.undraw()
        self.draw()