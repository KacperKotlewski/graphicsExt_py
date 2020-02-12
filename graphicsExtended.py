import graphics as gr

class GraphExtWin(gr.GraphWin):
    def __init__(self, title="Graphics Window",
                 width=200, height=200, autoflush=True):
        gr.GraphWin.__init__(self,title, width, height, autoflush)
        #TODO: dodaj listenera dla klawiszy myszy oraz czy klawisz jest down czy up

    def __repr__(self):
        return self.win

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

#TODO: dodaj Radio oraz RadioList


class Button(ClickableObject):
    def __init__(self, p1, p2, text="", onClick = None):
        ClickableObject.__init__(self, p1, p2)
        self.setText(text)
        self.outlinebox = gr.Rectangle(p1, p2)
        self.config["textColor"] = "black"
        self.config["onclickColor"]="Grey"

    def __repr__(self):
        return "Button({}, {}, '{}')".format(str(self.p1), str(self.p2), str(self.Text))

    def setText(self, text):
        if(type(text) == str):
            t = gr.Text(self.getCenter(), text)
            self.Text = t
        elif(type(text) == gr.Text):
            text.anchor = self.getCenter()
            self.Text = text


    def checkClick(self, mouse):
        clicked=False
        try:
            if( (mouse.x > self.p1.x and mouse.x < self.p2.x) and (mouse.y > self.p1.y and mouse.y < self.p2.y) ):
                self.outlinebox.setFill(self.config["onclickColor"])
                clicked = True
        except:
            pass
        if(self.outlinebox.config["fill"] != self.config["fill"] and not clicked):
            self.outlinebox.setFill(self.config["fill"])

    def _draw(self, graphwin):
        self.outlinebox.draw(graphwin)
        self.Text.draw(graphwin)

    def _undraw(self):
        self.outlinebox.undraw()
        self.Text.undraw()

    def clone(self):
        other = Button(self.p1, self.p2, self.Text)
        other.config = self.config.copy()
        return other