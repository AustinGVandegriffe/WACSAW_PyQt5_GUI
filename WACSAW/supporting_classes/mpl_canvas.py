from ..imports import *






class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100, rows=1, cols=1):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.subplots(rows,cols, sharex=True)
        if not isinstance(self.axes, np.ndarray):
            self.axes = [self.axes]
        super(MplCanvas, self).__init__(fig)