import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QPushButton, QCheckBox, QButtonGroup,
                               QHBoxLayout, QVBoxLayout)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle('Layout Test')
        self.displayWidgets()
        self.label.setAlignment(Qt.AlignHCenter)
        self.show()
    
    def displayWidgets(self):
        # create label and button widgets
        title = QLabel("Evening poll")
        title.setFont(QFont('Arial', 17))
        question = QLabel("How was your day?")
        
        # creating a horizontal layout for the title
        title_h_box = QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()
        
        # variants of choice
        ratings = ["Horrible", "Meh..", "Fine", "Great"]

        ratings_h_box = QHBoxLayout()  # distance between widgets in horizontal layout
        ratings_h_box.setSpacing(80)

        ratings_h_box.addStretch()
        for rating in ratings:
            rate_label = QLabel(rating, self)
            ratings_h_box.addWidget(rate_label)
        ratings_h_box.addStretch()

        cb_h_box = QHBoxLayout()
        cb_h_box.setSpacing(100)

        # creating a container for QCheckBox group
        scale_bg = QButtonGroup(self)

        cb_h_box.addStretch()
        for index in range(len(ratings)):
            checkbox = QCheckBox(str(index), self)
            cb_h_box.addWidget(checkbox)
            scale_bg.addButton(checkbox)
        cb_h_box.addStretch()

        # set the function of selection variant processing
        scale_bg.buttonClicked.connect(self.checkboxClicked)

        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)
        
        # creating a vertical layout, step-by-step adding widgets
        # and elements h_box layout
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(ratings_h_box)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(2)
        v_box.addWidget(self.label)
        v_box.addWidget(close_button)
        self.setLayout(v_box)
    
    def checkboxClicked(self, cb):
        self.label.setText(f"Chose: {cb.text()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) 
