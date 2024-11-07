import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit,
                               QLineEdit, QPushButton, QCheckBox,
                               QGridLayout, QVBoxLayout, QMainWindow, QMessageBox)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Slot, Signal

class ToDoListWidget(QWidget):
    doneSignal = Signal(str, str)  # creating a signal
    warningSignal = Signal(str)

    def __init__(self, parent=None):
        super(ToDoListWidget, self).__init__(parent)
        self.dictToDo = {}
        self.dayMeet = []
        self.initializeUI()
        for checkbox in self.dictToDo:
            checkbox.clicked.connect(self.itIsDone)
    
    def initializeUI(self):
        main_grid = QGridLayout()
        todo_title = QLabel("To-Do List for Today")
        todo_title.setFont(QFont('Arial', 24))
        todo_title.setAlignment(Qt.AlignCenter)
        
        mustdo_label = QLabel("Need to-do")
        mustdo_label.setFont(QFont('Arial', 20))
        mustdo_label.setAlignment(Qt.AlignCenter)
        
        appts_label = QLabel("Planned meetings")
        appts_label.setFont(QFont('Arial', 20))
        appts_label.setAlignment(Qt.AlignCenter)
        
        # Створення сітки
        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5, 5, 5, 5)
        mustdo_grid.addWidget(mustdo_label, 0, 0, 1, 2)
        
        for position in range(1, 15):
            checkbox = QCheckBox()
            checkbox.setObjectName(str(position))
            linedit = QLineEdit("")
            linedit.setMinimumWidth(200)
            mustdo_grid.addWidget(checkbox, position, 0)
            mustdo_grid.addWidget(linedit, position, 1)
            self.dictToDo[checkbox] = linedit
        
        # Секція для зустрічей
        morning_label = QLabel("Morning")
        morning_label.setFont(QFont('Arial', 16))
        noon_label = QLabel("Afternoon")
        noon_label.setFont(QFont('Arial', 16))
        evening_label = QLabel("Evening")
        evening_label.setFont(QFont('Arial', 16))
        
        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5, 5, 5, 5)
        evening_entry = QTextEdit()
        noon_entry = QTextEdit()
        morning_entry = QTextEdit()
        appt_v_box.addWidget(appts_label)
        appt_v_box.addWidget(morning_label)
        appt_v_box.addWidget(morning_entry)
        appt_v_box.addWidget(noon_label)
        appt_v_box.addWidget(noon_entry)
        appt_v_box.addWidget(evening_label)
        appt_v_box.addWidget(evening_entry)
        self.dayMeet = [morning_entry, noon_entry, evening_entry]
        
        main_grid.addWidget(todo_title, 0, 0, 1, 2)
        main_grid.addLayout(mustdo_grid, 1, 0)
        main_grid.addLayout(appt_v_box, 1, 1)
        self.setLayout(main_grid)
    
    def itIsDone(self):
        sender = self.sender()
        if not self.dictToDo[sender].text():
            sender.setChecked(False)
            self.warningSignal.emit(sender.objectName()) 
            return 
        if sender.isChecked(): 
            self.doneSignal.emit(sender.objectName(), self.dictToDo[sender].text())
    
    @Slot() 
    def clearToDoList(self): 
        for entry in self.dayMeet: 
            entry.clear()
        for checkbox, edit in self.dictToDo.items(): 
            checkbox.setChecked(False) 
            edit.setText("")

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.todo = ToDoListWidget() 
        self.todo.doneSignal.connect(self.itIsDone) 
        self.todo.warningSignal.connect(self.warningDone) 
        self.initializeUI()
    
    def initializeUI(self): 
        self.setWindowTitle('To-Do List') 
        close_button = QPushButton("Close") 
        close_button.clicked.connect(self.close) 
        clear_button = QPushButton("Clean") 
        clear_button.clicked.connect(self.todo.clearToDoList) 
        
        v_box = QVBoxLayout() 
        v_box.addWidget(self.todo) 
        v_box.addWidget(clear_button) 
        v_box.addWidget(close_button) 
        
        widget = QWidget(self) 
        widget.setLayout(v_box) 
        self.setCentralWidget(widget) 
        self.setMaximumHeight(500) 
        self.show()

    @Slot(str, str) 
    def itIsDone(self, number, description): 
        QMessageBox().information(self, "Attention!", 
                                  f'Case {description} #{number} is done!', 
                                  QMessageBox.Ok, QMessageBox.Ok)
    
    @Slot(str) 
    def warningDone(self, number): 
        QMessageBox().warning(self, "Attention!", f"Case №{number} not fulfilled!", 
                              QMessageBox.Ok, QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
