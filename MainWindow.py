### UI imports
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QStackedLayout, QTableWidget, QTableWidgetItem, QLineEdit
#from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


from VM import ViewModel

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setMinimumHeight(700)
        self.setMinimumWidth(1200)
        self.setWindowTitle("UNLP Scraping") # Titulo de la ventan
        
        ## init ViewModel
        self.ViewModel = ViewModel.ViewModel() 

        ## init first window
        self.subjectsWindow() 

        ## init second window
        self.schedulesWindow() 

        ## init windows manager
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.subjects_window)
        self.stacked_layout.addWidget(self.schedules_window)

        self.setLayout(self.stacked_layout)
        self.show()
        self.setList()

## Declaracion de ventanas
    def subjectsWindow(self):
        self.subjects_window = QWidget()

        VLayout = QVBoxLayout()
        HSubjectListLayout = QHBoxLayout()

        self.unselected_subject_list = QListWidget(self)
        self.unselected_subject_list.clicked.connect(self.selectSubject)

        self.selected_subject_list = QListWidget(self)
        self.selected_subject_list.clicked.connect(self.unselectSubject)

        subjectButton = QPushButton(text="Cargar horarios")
        subjectButton.clicked.connect(self.loadSchedules)

        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.searchSubject)

        HSubjectListLayout.addWidget(self.unselected_subject_list)
        HSubjectListLayout.addWidget(self.selected_subject_list)

        VLayout.addWidget(self.lineEdit)
        VLayout.addLayout(HSubjectListLayout)
        VLayout.addWidget(subjectButton)

        self.subjects_window.setLayout(VLayout)

    def schedulesWindow(self):
        self.schedules_window = QWidget()

        self.table = QTableWidget(29, 5, self)
        
        self.table.setHorizontalHeaderLabels(["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])
        self.table_row = []
        val = 8
        for i in range(29):
            if i % 2 != 0:
                if val < 10:
                    self.table_row.append("0"+str(val)+":30")
                else:
                    self.table_row.append(str(val)+":30")
                val+=1
            else:
                if val < 10:
                    self.table_row.append("0"+str(val)+":00")
                else:
                    self.table_row.append(str(val)+":00")
        self.table.setVerticalHeaderLabels(self.table_row)

        button = QPushButton(text="Volver")
        button.clicked.connect(self.goBack)

        VLayout = QVBoxLayout() 
        VLayout.addWidget(self.table)
        VLayout.addWidget(button)

        self.schedules_window.setLayout(VLayout)

## Declaracion de funciones 
    def loadSubject(self):
        list = self.ViewModel.loadSubject()
        for i in range(0, len(list)):
            self.unselected_subject_list.insertItem(i, list[i])

    def loadMatrix(self, matrix, schedule_item):
        if len(matrix) == 0:
            matrix.append(schedule_item)
        else:
            for i in range(len(matrix)):
                if matrix[i][0] == schedule_item[0] and matrix[i][1] == schedule_item[1]:
                    matrix[i][2] = matrix[i][2] + "\n--------\n" + schedule_item[2]
                    return matrix
            
            matrix.append(schedule_item)
        return matrix

    def loadSchedules(self):
        self.stacked_layout.setCurrentIndex(1)
        
        schedules = self.ViewModel.loadSchedules()
        matrix = []
        for list in schedules:
            for elem in list:
                confirmed_text = ""
                if elem.confirmed:
                    confirmed_text = "Confirmada"
                else:
                    confirmed_text = "Sin confirmar"
                schedule_item = [self.table_row.index(elem.start), elem.day, str(elem.subject) + "\nINICIO - "+ str(elem.type) + " - " + confirmed_text]
                matrix = self.loadMatrix(matrix, schedule_item)

                schedule_item = [self.table_row.index(elem.end), elem.day, str(elem.subject)+ "\nFIN - "+ str(elem.type) + " - " + confirmed_text]
                matrix = self.loadMatrix(matrix, schedule_item)

        for elem in matrix:
            item = QTableWidgetItem()
            text = str(elem[2])
            item.setText(text)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(elem[0], elem[1], item)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()


    def goBack(self):
        self.stacked_layout.setCurrentIndex(0)
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.takeItem(i, j)

    def selectSubject(self):
        item = self.unselected_subject_list.currentItem()
        self.ViewModel.select(item.text(), True)
        self.setList()

    def unselectSubject(self):
        item = self.selected_subject_list.currentItem()
        self.ViewModel.select(item.text(), False)
        self.setList()
    
    def setList(self):
        selected = self.ViewModel.getSelected()
        unselected = []
        if len(self.lineEdit.text()) != 0:
            text = self.lineEdit.text()
            unselected = self.ViewModel.searchSubject(text)
        else:
            unselected = self.ViewModel.getUnselected()
        self.selected_subject_list.clear()
        self.unselected_subject_list.clear()
        for i in range(len(selected)):
            self.selected_subject_list.insertItem(i, selected[i])
        for i in range(len(unselected)):
            self.unselected_subject_list.insertItem(i, unselected[i])
    
    def searchSubject(self):
        self.unselected_subject_list.clear()
        text = self.lineEdit.text()
        list = []
        if len(text) == 0:
            list = self.ViewModel.getUnselected()
        else:
            list = self.ViewModel.searchSubject(text)
        for i in range(len(list)):
            self.unselected_subject_list.insertItem(i, list[i])

if __name__ in "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    app.exec()