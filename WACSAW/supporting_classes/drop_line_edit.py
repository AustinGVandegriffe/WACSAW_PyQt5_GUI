from ..imports import *

class DropLineEdit(QLineEdit):
    def __init__(self, parent=None, ensure_dir=False, ensure_file=False):
        super().__init__(parent)
        self.ensure_dir = ensure_dir
        self.ensure_file = ensure_file

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    t_url = url.toLocalFile()
                    if self.ensure_file:
                        if os.path.isfile(t_url):
                            self.setText(t_url)
                    elif self.ensure_dir:
                        if os.path.isdir(t_url):
                            self.setText(t_url)
                    else:
                        self.setText(t_url)
                    break
        else:
            pass