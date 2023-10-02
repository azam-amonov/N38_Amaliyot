from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtWidgets import QPushButton, QCheckBox
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python")
        self.button = QPushButton("Push me")
        self.button.setFixedSize(100, 100)
        self.button.clicked.connect(self.button_pressed)


    def button_pressed(self):
        if self.button.isChecked():
            print("Button is checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
