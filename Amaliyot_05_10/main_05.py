from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QHBoxLayout, QGridLayout,
                             QCheckBox, QMessageBox, QLineEdit, QComboBox,
                             QTextEdit, QLabel)
from googletrans import Translator
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Google Translate")
        self.setFixedSize(350, 400)


        # Vertical layout!
        vLayout = QVBoxLayout()
        vLayout2 = QVBoxLayout()

        # Horizontal layout
        hLayout = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout3 = QHBoxLayout()

        # PushButton
        translateButton = QPushButton("Translate")

        # Combo box
        self.fromLanguageComboBox = QComboBox()
        self.fromLanguageComboBox.addItems(["uz", "en", "ru"])

        self.toLanguageComboBox = QComboBox()
        self.toLanguageComboBox.addItems(["uz", "en", "ru"])

        # Line Edit
        lineEdit = QLineEdit()

        # TextEdit
        textEdit = QTextEdit()

        # Label
        label = QLabel("Text")
        label.setFixedSize(310, 250)
        label.setStyleSheet("background-color : yellow")

        # SetLayouts
        self.setLayout(vLayout)
        vLayout.addLayout(hLayout)
        hLayout.addWidget(self.fromLanguageComboBox)
        hLayout.addWidget(self.toLanguageComboBox)

        vLayout.addWidget(lineEdit)
        vLayout.addWidget(label)
        vLayout.addWidget(translateButton)

    def translateText(self):
        fromLangText = self.fromLanguageComboBox.currentText()
        toLangText = self.toLanguageComboBox.currentText()

    


    def message(self):
        pass

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = Window()
    # window.show()
    # app.exec()
    # Create an instance of the Translator class
    translator = Translator()

    # Use the translate method to translate text
    result = translator.translate(text="Salom", src="uz", dest="en")

    # Print the translation result
    print(result.text)
