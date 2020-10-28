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


from WACSAW import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
