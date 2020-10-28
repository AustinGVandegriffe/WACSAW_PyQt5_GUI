from __future__ import print_function

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QPushButton, QWidget, QVBoxLayout, QVBoxLayout

import os, sys
import datetime as dt

import numpy as np
import pandas as pd
EMPTY_DF = pd.DataFrame({0:[None]})

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas,FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.widgets as mwidgets
from matplotlib.widgets import RectangleSelector, SpanSelector