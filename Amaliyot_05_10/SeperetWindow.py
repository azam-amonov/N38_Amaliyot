from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main screen")
        self.vLayout = QVBoxLayout()
        self.setLayout(self.vLayout)

        self.buttonOne = QPushButton("Screen One")
        self.buttonTwo = QPushButton("Screen Two")
        self.buttonThree = QPushButton("Screen Three")

        self.vLayout.addWidget(self.buttonOne)
        self.vLayout.addWidget(self.buttonTwo)
        self.vLayout.addWidget(self.buttonThree)

        self.buttonOne.clicked.connect(self.firstScreen)
        self.buttonTwo.clicked.connect(self.secondScreen)
        self.buttonThree.clicked.connect(self.thirdScreen)

    def firstScreen(self):
        self.firstScreenInstance = FirstScreen()
        self.firstScreenInstance.show()

    def secondScreen(self):
        self.secondScreenInstance = SecondScreen()
        self.secondScreenInstance.show()

    def thirdScreen(self):
        self.thirdScreenInstance = ThirdScreen()
        self.thirdScreenInstance.show()

class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First screen")
        self.setStyleSheet("background-color: yellow")

class SecondScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second screen")
        self.setStyleSheet("background-color: black")

class ThirdScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Third screen")
        self.setStyleSheet("background-color: green")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
