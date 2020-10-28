"""
/// @file WACSAW_main.py
/// @author Austin Vandegriffe
/// @date 2020-09-16
/// @brief Sets up the skeleton of a GUI for the Wasserstein Algorithm for
/// ## Classifying Sleep and Wake (WACSAW). The functionality of it is defined
/// ## in the included files.
/// @style K&R, and "one true brace style" (OTBS), and '_' variable naming
/////////////////////////////////////////////////////////////////////
/// @references
/// ## [1] Paper coming soon.
"""
from ..imports import *
from .preprocessing_page import *

class Ui_MainWindow(object):
    def alert_popup(self, msg):
        t_popup = QMessageBox(self.main_window)
        t_popup.setWindowTitle("WACSAW Alert")
        t_popup.setText(msg)
        t_popup.setIcon(QMessageBox.Critical)
        t_popup.exec_()

    def browser(self, out_tag, ext="*.csv"):
        fileName = None
        if ext:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.main_window, 'Single File', QtCore.QDir.rootPath(),
                                                                ext)
        else:
            fileName = QtWidgets.QFileDialog.getExistingDirectory(self.main_window, 'Single File',
                                                                 QtCore.QDir.rootPath())
        if fileName:
            out_tag.setText(fileName)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 767)
        self.main_window = MainWindow
        self.widget_main_wacsaw = QtWidgets.QWidget(MainWindow)
        self.widget_main_wacsaw.setObjectName("widget_main_wacsaw")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_main_wacsaw)
        self.gridLayout.setObjectName("gridLayout")
        self.header_gui = QtWidgets.QLabel(self.widget_main_wacsaw)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.header_gui.setFont(font)
        self.header_gui.setObjectName("header_gui")
        self.gridLayout.addWidget(self.header_gui, 0, 0, 1, 1)

        self.wacsaw_tabs = QtWidgets.QTabWidget(self.widget_main_wacsaw)
        self.wacsaw_tabs.setEnabled(True)
        self.wacsaw_tabs.setAcceptDrops(True)
        self.wacsaw_tabs.setAutoFillBackground(False)
        self.wacsaw_tabs.setUsesScrollButtons(True)
        self.wacsaw_tabs.setTabsClosable(False)
        self.wacsaw_tabs.setMovable(True)
        self.wacsaw_tabs.setTabBarAutoHide(False)
        self.wacsaw_tabs.setObjectName("wacsaw_tabs")


        self.tab01_preprocessing = QtWidgets.QWidget()
        self.tab01_preprocessing.setEnabled(True)
        self.tab01_preprocessing.setObjectName("tab01_preprocessing")
        PreprocessingWidgetSetup(self)
        self.wacsaw_tabs.addTab(self.tab01_preprocessing, "")


        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName("tab")
        # self.wacsaw_tabs.addTab(self.tab, "")
        # self.tab_2 = QtWidgets.QWidget()
        # self.tab_2.setEnabled(False)
        # self.tab_2.setObjectName("tab_2")
        # self.wacsaw_tabs.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.wacsaw_tabs, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.widget_main_wacsaw)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1293, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.wacsaw_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header_gui.setText(_translate("MainWindow", "WACSAW Analysis"))
        self.t01_button_browse_output.setText(_translate("MainWindow", "Browse"))
        self.t01_label_output_name.setText(_translate("MainWindow", "Output Name"))
        self.t01_button_save_preprocessing_output.setText(_translate("MainWindow", "Save"))
        self.t01_label_output_path.setText(_translate("MainWindow", "Output Path"))
        self.t01_header_preprocessing.setText(_translate("MainWindow", "Preprocessing"))
        self.t01_label_geneactiv_source_input.setText(_translate("MainWindow", "GENEActiv Source Input"))
        self.t01_button_generate_tilt_angle.setText(_translate("MainWindow", "Generate Tilt Angle"))
        self.t01_button_log_validation.setText(_translate("MainWindow", "Log Validation"))
        self.t01_button_actigraphy_validation.setText(_translate("MainWindow", "Actigraphy Validation"))
        self.t01_button_browse_input.setText(_translate("MainWindow", "Browse"))
        self.t01_button_preprocessing_load_input.setText(_translate("MainWindow", "Load"))
        self.t01_button_clear_dataset.setText(_translate("MainWindow", "Clear"))
        self.wacsaw_tabs.setTabText(self.wacsaw_tabs.indexOf(self.tab01_preprocessing), _translate("MainWindow", "Preprocessing"))
        # self.wacsaw_tabs.setTabText(self.wacsaw_tabs.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        # self.wacsaw_tabs.setTabText(self.wacsaw_tabs.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))