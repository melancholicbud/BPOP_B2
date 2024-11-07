import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)
from PySide6.QtCore import Qt

class MainWindow(QWidget) : # inherits QWidget
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.button = QPushButton('Cleaned', self)
        self.line_edit = QLineEdit(self)
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QLineEdit Test')
        QLabel("Input login", self).move(100, 10)
        name_label = QLabel("Login: ", self)
        name_label.move(70, 50)
        self.line_edit.setAlignment(Qt.AlignLeft) # align to left side
        self.line_edit.move(130, 50)
        self.line_edit.resize(200, 20)
        self.button.clicked.connect(self.clearEntries)
        self.button.move(160, 110)
        self.show()
    
    def clearEntries(self):
        # getting a pointer to object generating signal
        sender = self.sender()
        # checking, that this button is "Clear"
        if sender.text() == 'Clear':
            self.line_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())