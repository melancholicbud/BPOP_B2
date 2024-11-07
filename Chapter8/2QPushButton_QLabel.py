from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
def __init__(self):
    super().__init__() # calling a constructor base class QWidget
    self.label = QLabel(self)
    self.button = QPushButton('Ok', self)
    self.initializeUI()

def initializeUI(self):
    self.setGeometry(100, 100, 400, 300) # size of widgets
    self.setWindowTitle('Hello World with QT')
    name_label = QLabel(self)
    name_label.setText('Press the button')
    name_label.move(60, 30) # position QLabel on the widget
    button = QPushButton('Ok', self) # set the method of the class instance to be called when the button is pressed
    button.clicked.connect(self.buttonClicked)
    button.move(80, 70) # QPushButton on widget
    self.show()

def buttonClicked(self):
    self.label.setText("Hooray!")
    self.button.setText("^_^")
    

