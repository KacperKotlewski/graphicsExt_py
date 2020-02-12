from subclasses.clickable_object import ClickableObject
import graphics as gr

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

    #TODO: dodaj onclick(function)