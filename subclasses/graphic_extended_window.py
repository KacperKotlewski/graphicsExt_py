import graphics as gr

class GraphExtWin(gr.GraphWin):
    def __init__(self, title="Graphics Window",
                 width=200, height=200, autoflush=True):
        gr.GraphWin.__init__(self,title, width, height, autoflush)
        #TODO: dodaj listenera dla klawiszy myszy oraz czy klawisz jest down czy up

    def __repr__(self):
        return self.win