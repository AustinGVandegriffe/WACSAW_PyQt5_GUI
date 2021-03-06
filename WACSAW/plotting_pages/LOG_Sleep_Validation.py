from ..imports import *
from ..supporting_classes.mpl_canvas import *
from ..supporting_classes.datetime_edits import *

class LOGValidationPlot(QtWidgets.QMainWindow):
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

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        self.setFocus()

    def closeEvent(self, event: QtGui.QCloseEvent):
        t_popup = QtWidgets.QMessageBox.question(self.parent.main_window, "WACSAW Alert", "Set ACT series equal to LOG series?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if t_popup == QtWidgets.QMessageBox.Yes:
            self.parent.df["act_sleep"] = self.parent.df["log_sleep"].copy()

    def __init__(self, parent=None):
        super().__init__(parent.main_window)
        self.parent = parent
        self.setupUi()
        self.setFocus()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1069, 768)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 2, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 6, 0, 1, 1)
        self.radio_button_wake = QtWidgets.QRadioButton(self.frame)
        self.radio_button_wake.setObjectName("radio_button_wake")
        self.gridLayout_2.addWidget(self.radio_button_wake, 3, 0, 1, 1)

        self.push_button_submit = QtWidgets.QPushButton(self.frame)
        self.push_button_submit.setObjectName("push_button_submit")
        self.push_button_submit.clicked.connect(lambda: self.sleep_wake_submission())
        self.gridLayout_2.addWidget(self.push_button_submit, 5, 0, 1, 1)

        self.radio_button_sleep = QtWidgets.QRadioButton(self.frame)
        self.radio_button_sleep.setChecked(True)
        self.radio_button_sleep.setObjectName("radio_button_sleep")
        self.gridLayout_2.addWidget(self.radio_button_sleep, 4, 0, 1, 1)

        self.date_time_edit_start = DateTimeEditStart(self.frame, self)
        self.date_time_edit_start.setMouseTracking(True)
        self.date_time_edit_start.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.date_time_edit_start.setCalendarPopup(True)
        # self.date_time_edit_start.setCurrentSectionIndex(0)
        self.date_time_edit_start.setObjectName("date_time_edit_start")
        self.date_time_edit_start.setDateTime(QtCore.QDateTime.currentDateTime())
        self.gridLayout_2.addWidget(self.date_time_edit_start, 1, 0, 1, 1)

        self.date_time_edit_end = DateTimeEditEnd(self.frame, self)
        self.date_time_edit_start.setMouseTracking(True)
        self.date_time_edit_end.setCalendarPopup(True)
        self.date_time_edit_end.setObjectName("date_time_edit_end")
        self.date_time_edit_end.setDateTime(QtCore.QDateTime.currentDateTime())
        self.gridLayout_2.addWidget(self.date_time_edit_end, 2, 0, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 2, 2, 1)
        self.widget_plot = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_plot.sizePolicy().hasHeightForWidth())
        self.widget_plot.setSizePolicy(sizePolicy)
        self.widget_plot.setObjectName("widget_plot")
        self.gridLayout.addWidget(self.widget_plot, 0, 0, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 2, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # After the start DateTimeEdit is set, make the end
        ## DateTimeEdit equal to it (helps with filling out the form).
        self.set_end_to_start = True

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radio_button_wake.setText(_translate("MainWindow", "Wake"))
        self.push_button_submit.setText(_translate("MainWindow", "Submit"))
        self.radio_button_sleep.setText(_translate("MainWindow", "Sleep"))
        self.date_time_edit_end.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd hh:mm:ss"))
        self.date_time_edit_start.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd hh:mm:ss"))

    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
    #->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    color_dct = {0: "steelblue", 1: "orangered"}
    def update_log_sleep_wake_spans(self):
        ax = self.canvas.axes
        t_diff = self.parent.df["log_sleep"].diff().abs()
        t_diff.values[0] = 1
        t_diff.values[-1] = 1
        t_timestamps = t_diff.loc[t_diff == 1].index
        sw_switch = self.parent.df['log_sleep'][0]

        ax[0].patches = [p for p in ax[0].patches if isinstance(p,matplotlib.patches.Rectangle)][0:4]
        if self.radio_button_sleep.isChecked():
            patches = ax[0].patches
            patches[2].set_width(0)
            patches[3].set_width(0)
        else:
            patches = ax[0].patches
            patches[0].set_width(0)
            patches[1].set_width(0)
        for i in range(1, len(t_timestamps)):
            ax[0].axvspan(t_timestamps[i - 1], t_timestamps[i], alpha=0.15, color=self.color_dct[sw_switch])
            sw_switch = np.absolute(sw_switch - 1)
        self.canvas.draw()
        self.widget_plot.setFocus()
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
    #->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def update_spans(self):
        patches = self.canvas.axes[0].patches[:4]#[p for p in ax[0].patches if isinstance(p,matplotlib.patches.Rectangle)][0:4]
        if self.radio_button_sleep.isChecked():
            patches[2].set_width(0)
            patches[3].set_width(0)
        else:
            patches[0].set_width(0)
            patches[1].set_width(0)
    def add_sleep(self,
        xmin :np.float64, #
        xmax :np.float64
    ):
        mn = np.datetime64(np.int(xmin), 's').astype(dt.datetime).strftime("%Y-%m-%d %H:%M:%S")
        mx = np.datetime64(np.int(xmax), 's').astype(dt.datetime).strftime("%Y-%m-%d %H:%M:%S")
        self.date_time_edit_start.setDateTime(QtCore.QDateTime.fromString(mn, "yyyy-MM-dd hh:mm:ss"))
        self.date_time_edit_end.setDateTime(QtCore.QDateTime.fromString(mx, "yyyy-MM-dd hh:mm:ss"))
        self.radio_button_wake.setChecked(False)
        self.radio_button_sleep.setChecked(True)
        self.set_end_to_start = False
        self.update_spans()
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
    #->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def add_wake(self, xmin, xmax):
        mn = np.datetime64(np.int(xmin), 's').astype(dt.datetime).strftime("%Y-%m-%d %H:%M:%S")
        mx = np.datetime64(np.int(xmax), 's').astype(dt.datetime).strftime("%Y-%m-%d %H:%M:%S")
        self.date_time_edit_start.setDateTime(QtCore.QDateTime.fromString(mn, "yyyy-MM-dd hh:mm:ss"))
        self.date_time_edit_end.setDateTime(QtCore.QDateTime.fromString(mx, "yyyy-MM-dd hh:mm:ss"))
        self.radio_button_wake.setChecked(True)
        self.radio_button_sleep.setChecked(False)
        self.set_end_to_start = False
        self.update_spans()
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
    #->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def sleep_wake_submission(self):
        mn = np.datetime64(self.date_time_edit_start.dateTime().toPyDateTime(),'s')
        mx = np.datetime64(self.date_time_edit_end.dateTime().toPyDateTime(), 's')
        t_indices = (self.parent.df.index >= mn) & (self.parent.df.index <= mx)
        self.parent.df.loc[t_indices, "log_sleep"] = 1*(self.radio_button_wake.isChecked())
        # print(f"SUBMISSION: {1*(self.radio_button_wake.isChecked())}")
        self.update_log_sleep_wake_spans()
        self.set_end_to_start = True
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
        self.update_log_sleep_wake_spans()
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = self.widget_plot
        widget.setLayout(layout)
        # self.setCentralWidget(widget)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center()-QtWidgets.QApplication.desktop().screen().rect().center())
        self.show()
        self.activateWindow()
        self.raise_()