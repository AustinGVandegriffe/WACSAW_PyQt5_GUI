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

from .imports import *

from .supporting_classes.drop_line_edit import *
from .supporting_classes.mpl_canvas import *
from .supporting_classes.datetime_edits import *

from .plotting_pages.ACT_Sleep_Validation import *
from .plotting_pages.LOG_Sleep_Validation import *

from .pages.main_page import *
from .pages.preprocessing_page import *