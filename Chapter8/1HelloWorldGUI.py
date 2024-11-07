import sys
from PySide6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # calling a constructor base QWidget class
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300) # size of widget
        self.setWindowTitle('Hello World with QT')
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())