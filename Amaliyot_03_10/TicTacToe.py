from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout
import sys


class TicTacTacWin(QWidget):
    def __init__(self):
        super().__init__()
        self.vLayout = QVBoxLayout()
        self.grid = QGridLayout()
        self.resetButton = QPushButton("Reset")

        self.vLayout.addLayout(self.grid)
        self.vLayout.addWidget(self.resetButton)

        self.setLayout(self.vLayout)
        self.buttonList = []
        self.turn = 0

        self.resetButtonPressed()

        self.resetButton.clicked.connect(self.resetButtonPressed)

        for row in range(3):
            for column in range(3):
                button = QPushButton(" ")
                button.setFixedSize(80, 80)
                self.buttonList.append(button)
                self.grid.addWidget(button, row, column)

                button.clicked.connect(lambda click, r=row, c=column: self.pressedButton(r, c))

    def pressedButton(self, row, column):
        cl_btn = self.buttonList[row * 3 + column]
        self.turn += 1

        if self.turn % 2 == 0:
            cl_btn.setText("X")
            cl_btn.setStyleSheet("background-color: green")
            cl_btn.setEnabled(False)

        else:
            cl_btn.setText("0")
            cl_btn.setStyleSheet("background-color: yellow")
            cl_btn.setEnabled(False)

    def resetButtonPressed(self):
        for i in self.buttonList:
            i.setEnabled(True)
            i.setStyleSheet("background-color: white")
            i.setText(" ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TicTacTacWin()
    win.show()
    app.exec()
