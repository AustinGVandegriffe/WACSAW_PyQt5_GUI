from ..imports import *
from ..supporting_classes.drop_line_edit import *
from ..plotting_pages.ACT_Sleep_Validation import *
from ..plotting_pages.LOG_Sleep_Validation import *

class PreprocessingWidgetSetup(object):
    @staticmethod
    def active_preprocessing_functionality(self, active: bool):
        for tag in [self.t01_button_generate_tilt_angle,
                    self.t01_button_log_validation,
                    self.t01_button_actigraphy_validation,
                    self.t01_line_edit_preprocessing_output_path,
                    self.t01_button_browse_output,
                    self.t01_line_edit_preprocessing_output_name,
                    self.t01_button_save_preprocessing_output]:
            tag.setEnabled(active)
    @staticmethod
    def load_source_dataframe(self):
        if "background-color" in self.t01_button_preprocessing_load_input.styleSheet():
            self.alert_popup("Cannot load new book until you clear or save the current dataset.")
        try:
            t_str = self.t01_line_edit_preprocessing_source_input.text()
            if t_str == '':
                return
            else:
                self.df = pd.read_csv(t_str, header=0, index_col=None,
                                  skiprows=100)
        except FileNotFoundError:
            raise Exception("Not implemented. FileNotFound for dataset.")
            pass
        try:
            self.df.columns = ["timestamp", "x_m", "y_m", "z_m", "lux_m",
                               "button", "temp_m", "svm", "x_std", "y_std",
                               "z_std", "lux_p"
                               ]
            self.df["timestamp"] = pd.to_datetime(self.df["timestamp"], format="%Y-%m-%d %H:%M:%S:%f").dt.floor('s')
            try:
                self.df["timestamp"] = pd.to_datetime(self.df["timestamp"], format="%Y-%m-%d %H:%M:%S:%f").dt.floor('s')
            except:
                try:
                    self.df["timestamp"] = pd.to_datetime(self.df["timestamp"], format="%Y-%m-%d %H:%M:%S.%f").dt.floor('s')
                except:
                    try:
                        self.df["timestamp"] = pd.to_datetime(self.df["timestamp"], format="%Y-%m-%d %H:%M:%S").dt.floor('s')
                    except:
                        raise Exception("Time format not recognized. Make sure it's YYYY-MM-DD HH:MM:SS:%f")
            self.df.index = pd.DatetimeIndex(self.df["timestamp"])
            self.df["act_sleep"] = np.ones(self.df.shape[0])
            self.df["log_sleep"] = np.ones(self.df.shape[0])
        except:
            raise Exception("Couldn't load dataset. Check format.")
        if not self.df.empty:
            self.t01_button_preprocessing_load_input.setStyleSheet("background-color:rgba(41,172,31,1);")
            self.active_preprocessing_functionality(True)
            # self.button_preprocessing_load_input.setEnabled(False)
    @staticmethod
    def clear_source_dataframe(self):
        self.df.drop(self.df.index, inplace=True)
        self.df = EMPTY_DF
        self.t01_button_preprocessing_load_input.setStyleSheet("")
        self.t01_line_edit_preprocessing_source_input.setText("")
        self.active_preprocessing_functionality(False)

    @staticmethod
    def save_dataframe(self) -> None:
        path = f"{self.t01_line_edit_preprocessing_output_path.text()}/{self.t01_line_edit_preprocessing_output_name.text()}.csv"
        self.df.to_csv( path, header=True, index=False )
        return

    def __init__(_,self):
        self.active_preprocessing_functionality = lambda active: _.active_preprocessing_functionality(self, active)
        self.load_source_dataframe = lambda: _.load_source_dataframe(self)
        self.clear_source_dataframe = lambda: _.clear_source_dataframe(self)
        self.save_dataframe = lambda: _.save_dataframe(self)


        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab01_preprocessing)
        self.gridLayout_2.setObjectName("gridLayout_2")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)


        self.t01_button_save_preprocessing_output = QtWidgets.QPushButton(self.tab01_preprocessing)
        self.t01_button_save_preprocessing_output.setEnabled(False)
        self.t01_button_save_preprocessing_output.setObjectName("t01_button_save_preprocessing_output")
        self.t01_button_save_preprocessing_output.clicked.connect(self.save_dataframe)
        self.gridLayout_2.addWidget(self.t01_button_save_preprocessing_output, 6, 0, 1, 1)


        self.t01_line_edit_preprocessing_output_name = QtWidgets.QLineEdit(self.tab01_preprocessing)
        self.t01_line_edit_preprocessing_output_name.setEnabled(False)
        self.t01_line_edit_preprocessing_output_name.setObjectName("t01_line_edit_preprocessing_output_name")
        self.gridLayout_2.addWidget(self.t01_line_edit_preprocessing_output_name, 5, 1, 1, 1)


        self.t01_line_edit_preprocessing_output_path = DropLineEdit(self.tab01_preprocessing, ensure_dir=True)
        self.t01_line_edit_preprocessing_output_path.setEnabled(False)
        self.t01_line_edit_preprocessing_output_path.setObjectName("t01_line_edit_preprocessing_output_path")
        self.gridLayout_2.addWidget(self.t01_line_edit_preprocessing_output_path, 4, 1, 1, 1)


        self.t01_header_preprocessing = QtWidgets.QLabel(self.tab01_preprocessing)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.t01_header_preprocessing.setFont(font)
        self.t01_header_preprocessing.setObjectName("t01_header_preprocessing")
        self.gridLayout_2.addWidget(self.t01_header_preprocessing, 0, 0, 1, 1)


        self.t01_line_edit_preprocessing_source_input = DropLineEdit(self.tab01_preprocessing, ensure_file=True)
        self.t01_line_edit_preprocessing_source_input.setObjectName("t01_line_edit_preprocessing_source_input")
        self.gridLayout_2.addWidget(self.t01_line_edit_preprocessing_source_input, 1, 1, 1, 1)


        self.t01_button_browse_output = QtWidgets.QPushButton(self.tab01_preprocessing)
        self.t01_button_browse_output.setEnabled(False)
        self.t01_button_browse_output.setObjectName("t01_button_browse_output")
        self.t01_button_browse_output.clicked.connect(lambda: self.browser(self.t01_line_edit_preprocessing_output_path, ext=""))
        self.gridLayout_2.addWidget(self.t01_button_browse_output, 4, 2, 1, 1)


        self.t01_button_browse_input = QtWidgets.QPushButton(self.tab01_preprocessing)
        self.t01_button_browse_input.setObjectName("t01_button_browse_input")
        self.t01_button_browse_input.clicked.connect(lambda: self.browser(self.t01_line_edit_preprocessing_source_input))
        self.gridLayout_2.addWidget(self.t01_button_browse_input, 1, 2, 1, 1)


        self.t01_label_output_name = QtWidgets.QLabel(self.tab01_preprocessing)
        self.t01_label_output_name.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t01_label_output_name.setFont(font)
        self.t01_label_output_name.setObjectName("t01_label_output_name")
        self.gridLayout_2.addWidget(self.t01_label_output_name, 5, 0, 1, 1)


        self.t01_label_output_path = QtWidgets.QLabel(self.tab01_preprocessing)
        self.t01_label_output_path.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t01_label_output_path.setFont(font)
        self.t01_label_output_path.setObjectName("t01_label_output_path")
        self.gridLayout_2.addWidget(self.t01_label_output_path, 4, 0, 1, 1)


        self.t01_label_geneactiv_source_input = QtWidgets.QLabel(self.tab01_preprocessing)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t01_label_geneactiv_source_input.setFont(font)
        self.t01_label_geneactiv_source_input.setObjectName("t01_label_geneactiv_source_input")
        self.gridLayout_2.addWidget(self.t01_label_geneactiv_source_input, 1, 0, 1, 1)


        self.t01_horizontalLayout = QtWidgets.QHBoxLayout()
        self.t01_horizontalLayout.setObjectName("t01_horizontalLayout")



        self.t01_button_preprocessing_load_input = QtWidgets.QPushButton(self.tab01_preprocessing)
        self.t01_button_preprocessing_load_input.setObjectName("t01_button_preprocessing_load_input")
        self.t01_button_preprocessing_load_input.clicked.connect(self.load_source_dataframe)
        self.t01_horizontalLayout.addWidget(self.t01_button_preprocessing_load_input)
        self.t01_button_clear_dataset = QtWidgets.QPushButton(self.tab01_preprocessing)
        self.t01_button_clear_dataset.clicked.connect(self.clear_source_dataframe)
        self.t01_button_clear_dataset.setObjectName("t01_button_clear_dataset")
        self.t01_horizontalLayout.addWidget(self.t01_button_clear_dataset)
        self.gridLayout_2.addLayout(self.t01_horizontalLayout, 2, 0, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 1)


        self.t01_horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.t01_horizontalLayout_2.setObjectName("t01_horizontalLayout_2")

        self.t01_button_generate_tilt_angle = QtWidgets.QPushButton(self.tab01_preprocessing)
        self.t01_button_generate_tilt_angle.setEnabled(False)
        self.t01_button_generate_tilt_angle.setStyleSheet("")
        self.t01_button_generate_tilt_angle.setObjectName("t01_button_generate_tilt_angle")
        self.t01_horizontalLayout_2.addWidget(self.t01_button_generate_tilt_angle)

        self.t01_button_log_validation = QtWidgets.QPushButton(self.tab01_preprocessing)
        self.t01_button_log_validation.setEnabled(False)
        self.t01_button_log_validation.setObjectName("t01_button_log_validation")
        self.t01_button_log_validation.clicked.connect(lambda: LOGValidationPlot(self)._show(self.df))
        self.t01_horizontalLayout_2.addWidget(self.t01_button_log_validation)

        self.t01_button_actigraphy_validation = QtWidgets.QPushButton(self.tab01_preprocessing)
        self.t01_button_actigraphy_validation.setEnabled(False)
        self.t01_button_actigraphy_validation.setObjectName("t01_button_actigraphy_validation")
        self.t01_button_actigraphy_validation.clicked.connect(lambda: ACTValidationPlot(self)._show(self.df))
        self.t01_horizontalLayout_2.addWidget(self.t01_button_actigraphy_validation)


        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.t01_horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.t01_horizontalLayout_2, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 1)