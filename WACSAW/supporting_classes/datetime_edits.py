from ..imports import *





class DateTimeEditStart(QtWidgets.QDateTimeEdit):
    def __init__(self, parent=None, main_window=None):
        self.main_window = main_window
        super().__init__(parent)
    def focusOutEvent(self, event: QtGui.QFocusEvent):
        if self.main_window.set_end_to_start:
            self.main_window.date_time_edit_end.setDateTime(self.dateTime())
        super(QtWidgets.QDateTimeEdit,self).focusOutEvent(event)

class DateTimeEditEnd(QtWidgets.QDateTimeEdit):
    def __init__(self, parent=None, main_window=None):
        self.main_window = main_window
        super().__init__(parent)
    def focusOutEvent(self, event: QtGui.QFocusEvent):
        if self.dateTime() < self.main_window.date_time_edit_start.dateTime():
            self.setDateTime(self.main_window.date_time_edit_start.dateTime())
        super(QtWidgets.QDateTimeEdit,self).focusOutEvent(event)