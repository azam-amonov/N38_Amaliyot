import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Button with a parent widget
        topBtn = QPushButton(parent=self)
        topBtn.setFixedSize(100, 60)
        bottomBtn = QPushButton(
            text="Bottom",
            parent=self
        )
        bottomBtn.setFixedSize(100, 60)
        bottomBtn.setIconSize(QSize(40, 40))
        layout = QVBoxLayout()
        layout.addWidget(topBtn)
        layout.addWidget(bottomBtn)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())