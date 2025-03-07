### UI imports
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QStackedLayout, QLabel
#from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


from VM import ViewModel

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setMinimumHeight(700)
        self.setMinimumWidth(1000)
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

## Declaracion de ventanas
    def subjectsWindow(self):
        self.subjects_window = QWidget()

        VLayout = QVBoxLayout()
        HButtonLayout = QHBoxLayout()
        HSubjectListLayout = QHBoxLayout()

        self.unselected_subject_list = QListWidget(self)
        self.unselected_subject_list.clicked.connect(self.selectSubject)

        self.selected_subject_list = QListWidget(self)
        self.selected_subject_list.clicked.connect(self.unselectSubject)


        buttonCM = QPushButton(text="Cargar materias")
        buttonCM.clicked.connect(self.loadSubject)

        buttonCH = QPushButton(text="Cargar horarios")
        buttonCH.clicked.connect(self.loadSchedules)

        HSubjectListLayout.addWidget(self.unselected_subject_list)
        HSubjectListLayout.addWidget(self.selected_subject_list)

        HButtonLayout.addWidget(buttonCM)
        HButtonLayout.addWidget(buttonCH)

        VLayout.addLayout(HSubjectListLayout)
        VLayout.addLayout(HButtonLayout)

        self.subjects_window.setLayout(VLayout)

    def schedulesWindow(self):
        self.schedules_window = QWidget()

        label = QLabel("Label")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        HLayout = QHBoxLayout()
        HLayout.addWidget(label)

        self.schedules_window.setLayout(HLayout)


## Declaracion de funciones 
    def loadSubject(self):
        list = self.ViewModel.loadSubject()
        for i in range(0, len(list)):
            self.unselected_subject_list.insertItem(i, list[i])

    def loadSchedules(self):
        ##self.ViewModel.loadSchedules()
        self.stacked_layout.setCurrentIndex(1)

    def selectSubject(self):
        item = self.unselected_subject_list.takeItem(self.unselected_subject_list.currentRow())
        self.selected_subject_list.addItem(item)
        self.ViewModel.selectSubject(self.unselected_subject_list.currentRow())

    def unselectSubject(self):
        item = self.selected_subject_list.takeItem(self.selected_subject_list.currentRow())
        self.unselected_subject_list.addItem(item)
        self.ViewModel.selectSubject(self.selected_subject_list.currentRow())


if __name__ in "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    app.exec()