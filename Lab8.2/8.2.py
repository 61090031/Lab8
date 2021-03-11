import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtPrintSupport import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(400, 330)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.canvas = Canvas()
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.clicked.connect(self.canvas.clear_drawing)

        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.clear_btn)


if __name__ == "__main__":
    sys.exit(main())