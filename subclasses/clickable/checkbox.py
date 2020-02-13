from subclasses.clickable.checkbox_familly import _CheckboxFamilly
from subclasses.main_classes.function_handler import FunctionHolder
import graphics as gr

class Checkbox(_CheckboxFamilly):
    def __init__(self, p1:gr.Point, p2:gr.Point, spaceSize:int=5, checked:bool=False, onclick:FunctionHolder=None):
        _CheckboxFamilly.__init__(self, p1, p2,spaceSize=spaceSize,checked=checked, onclick=onclick)

    def __repr__(self):
        return "Checkbox({}, {}, {})".format(str(self.p1), str(self.p2), str(self.checked))

    def clone(self):
        other = Checkbox(self.p1, self.p2, self.spaceSize, self.checked, self.onclickFunc)
        other.config = self.config.copy()
        other.graphwin = self.graphwin
        return other
