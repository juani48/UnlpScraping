### UI imports
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QStackedLayout, QLabel, QTableWidget, QTableWidgetItem
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
        self.setWindowTitle("Home") # Titulo de la ventan
        
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


        button = QPushButton(text="Cargar horarios")
        button.clicked.connect(self.loadSchedules)

        HSubjectListLayout.addWidget(self.unselected_subject_list)
        HSubjectListLayout.addWidget(self.selected_subject_list)

        VLayout.addLayout(HSubjectListLayout)
        VLayout.addWidget(button)

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
                    matrix[i][2] = matrix[i][2] + "\n----\n" + schedule_item[2]
                    return matrix
            
            matrix.append(schedule_item)
        return matrix

    def loadSchedules(self):
        self.stacked_layout.setCurrentIndex(1)
        
        schedules = self.ViewModel.loadSchedules()
        matrix = []
        for list in schedules:
            for elem in list:
                schedule_item = [self.table_row.index(elem.start), elem.day, str(elem.subject) + "\nINICIO - "+ str(elem.type) + "- Confirmado: " + str(elem.confirmed)]
                matrix = self.loadMatrix(matrix, schedule_item)

                schedule_item = [self.table_row.index(elem.end), elem.day, str(elem.subject)+ "\nFIN - "+ str(elem.type)]
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
        self.ViewModel.select(self.unselected_subject_list.currentRow(), True)
        self.setList()

    def unselectSubject(self):
        self.ViewModel.select(self.selected_subject_list.currentRow(), False)
        self.setList()
    
    def setList(self):
        selected = self.ViewModel.getSelected()
        unselected = self.ViewModel.getUnselected()
        self.selected_subject_list.clear()
        self.unselected_subject_list.clear()
        for i in range(len(selected)):
            self.selected_subject_list.insertItem(i, selected[i])
        for i in range(len(unselected)):
            self.unselected_subject_list.insertItem(i, unselected[i])


if __name__ in "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    app.exec()