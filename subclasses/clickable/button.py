from subclasses.main_classes.clickable_object import ClickableObject
import graphics as gr
import time

class Button(ClickableObject):
    def __init__(self, p1, p2, text="", onClick = None, arguments = None):
        ClickableObject.__init__(self, p1, p2)
        self.setText(text)
        self.outlinebox = gr.Rectangle(p1, p2)
        self.config["textColor"] = "black"
        self.config["onclickColor"]="grey"

    def __repr__(self):
        return "Button({}, {}, '{}')".format(str(self.p1), str(self.p2), str(self.Text))

    def setText(self, text):
        if(type(text) == str):
            t = gr.Text(self.getCenter(), text)
            self.Text = t
        elif(type(text) == gr.Text):
            text.anchor = self.getCenter()
            self.Text = text

    def _clicked(self):
        self.outlinebox.setFill(self.config["onclickColor"])
        
        time.sleep(0.1)

    def _notClicked(self):
        if(self.outlinebox.config["fill"] != self.config["fill"]):
            self.outlinebox.setFill(self.config["fill"])

    def _draw(self, graphwin):
        self.outlinebox.draw(graphwin)
        self.Text.draw(graphwin)

    def _undraw(self):
        self.outlinebox.undraw()
        self.Text.undraw()

    def _move(self, dx, dy):
        self.outlinebox.move(dx, dy)
        self.Text.move(dx, dy)
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def clone(self):
        other = Button(self.p1, self.p2, self.Text)
        other.config = self.config.copy()
        return other