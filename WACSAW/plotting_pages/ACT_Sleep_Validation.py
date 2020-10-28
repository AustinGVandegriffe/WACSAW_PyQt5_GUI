from ..imports import *
from ..supporting_classes.mpl_canvas import *
from ..supporting_classes.datetime_edits import *

class ACTValidationPlot(QtWidgets.QMainWindow):
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        print(f"PRESS: {self.toolbar._active}; {event.key()}; {event.isAutoRepeat()}; {event.modifiers()==QtCore.Qt.ShiftModifier}; {event.text()}")
        if event.isAutoRepeat():
            return
        elif event.text().lower() == 'z':
            self.toolbar.zoom()
        elif event.text().lower() == 'x':
            self.toolbar.pan()
        elif event.modifiers()==QtCore.Qt.ShiftModifier and event.text().lower() == 'h':
            self.toolbar.home()
        return

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
        print(f"RELEASE: {self.toolbar._active}; {event.key()}; {event.isAutoRepeat()}; {event.modifiers()==QtCore.Qt.ShiftModifier}; {event.text()}")
        if event.isAutoRepeat():
            return
        # elif event.modifiers()==QtCore.Qt.ShiftModifier:
        if event.text().lower() == 'z':
            self.toolbar.zoom()
        elif event.text().lower() == 'x':
            self.toolbar.pan()
        return

    def __init__(self, parent=None):
        super().__init__(parent.main_window)
        self.parent = parent

    ####################################################################################################################
    #####  Span Functions  #############################################################################################
    ####################################################################################################################
    #->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    color_dct = {0: "steelblue", 1: "orangered"}
    def update_act_sleep_wake_spans(self):
        ax = self.canvas.axes
        t_diff = self.parent.df["act_sleep"].diff().abs()
        t_diff.values[0] = 1
        t_diff.values[-1] = 1
        t_timestamps = t_diff.loc[t_diff == 1].index
        sw_switch = self.parent.df['act_sleep'][0]

        ax[0].patches = []
        for i in range(1, len(t_timestamps)):
            ax[0].axvspan(t_timestamps[i - 1], t_timestamps[i], alpha=0.15, color=self.color_dct[sw_switch])
            sw_switch = np.absolute(sw_switch - 1)

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
    #->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def add_sleep(self,
        xmin :np.float64, #
        xmax :np.float64
    ):
        mn = np.datetime64(np.int(xmin), 's')
        mx = np.datetime64(np.int(xmax), 's')
        t_indices = (self.parent.df.index >= mn) & (self.parent.df.index <= mx)
        self.parent.df.loc[t_indices, "act_sleep"] = 0
        self.update_act_sleep_wake_spans()

    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
    def add_wake(self, xmin, xmax):
        mn = np.datetime64(np.int(xmin), 's')
        mx = np.datetime64(np.int(xmax), 's')
        t_indices = (self.parent.df.index >= mn) & (self.parent.df.index <= mx)
        self.parent.df.loc[t_indices, "act_sleep"] = 1
        self.update_act_sleep_wake_spans()
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
    ####################################################################################################################
    #####  Plotting and Show Functions  ################################################################################
    ####################################################################################################################
    def __plot_svm(self, df):
        ax = self.canvas.axes
        df["svm"].plot(ax=ax[0], linewidth=0.5, color="steelblue",alpha=0.5)
        df["svm"].rolling(window=20,center=True).median().plot(ax=ax[0], linewidth=0.5, color="steelblue", alpha=0.5)
        ax[0].set_xlim(df.index.values[0], df.index.values[-1])
        ax[0].set_ylim(-0.05, df["svm"].max())
        # ax[0].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%m-%d| %H:%M:%S"))
    def _show(self, df):
        self.canvas = MplCanvas(self, width=10, height=6, dpi=100)

        # If you do not keep the SpanSelector part of the class it will be
        ## destructed at the end of the function, hence self.* = SpanSelector(...)
        self.span_add_sleep = SpanSelector(self.canvas.axes[0], self.add_sleep, 'horizontal', useblit=True,
                                      rectprops=dict(alpha=0.25, facecolor='blue'), span_stays=True, button=[1])
        self.span_add_wake = SpanSelector(self.canvas.axes[0], self.add_wake, 'horizontal', useblit=True,
                                     rectprops=dict(alpha=0.25, facecolor='orangered'), span_stays=True, button=[3])

        # self.canvas.mpl_connect('button_press_event', self.key_press)

        self.__plot_svm(df)
        self.update_act_sleep_wake_spans()
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center()-QtWidgets.QApplication.desktop().screen().rect().center())
        self.show()
        self.activateWindow()
        self.raise_()