import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TicTacToe")
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.buttons = []
        self.turn = 0

        for i in range(3):
            for j in range(3):
                button = QPushButton(" ")
                button.setFixedSize(70, 70)
                self.buttons.append(button)
                self.grid.addWidget(button, i, j)

                button.clicked.connect(lambda click, row=i, column=j: self.button_click(row, column))

    def button_click(self, row, column):
        clicked_button = self.buttons[row * 3 + column]
        self.turn += 1

        if self.turn % 2 == 0:
            clicked_button.setText('❌')
            clicked_button.setEnabled(False)
        else:
            clicked_button.setText('⭕️')
            clicked_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TicTacToe()
    win.show()

    app.exec()
