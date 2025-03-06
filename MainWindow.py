### UI imports
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QListWidgetItem, QHBoxLayout, QVBoxLayout, QCheckBox
#from PyQt6.QtGui import QFont
#from PyQt6.QtCore import Qt
from pyqt_checkbox_list_widget.checkBoxListWidget import CheckBoxListWidget

### UseCase imports
from UseCase import UseCaseGetSubjects

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setMinimumHeight(500)
        self.setMinimumWidth(700)
        self.setWindowTitle("Home") # Titulo de la ventan

        self.createElements()
        self.show()
        
    def createElements(self):

        VLayout = QVBoxLayout()
        HLayout = QHBoxLayout()

        self.subject_list = QListWidget(self)
        self.subject_list.clicked.connect(self.selectSubject)

        #self.check_subject_list = CheckBoxListWidget()
        #self.check_subject_list.activated.connect(self.selectSubject)

        buttonCM = QPushButton(text="Cargar materias")
        buttonCM.clicked.connect(self.loadSubject)

        buttonCH = QPushButton(text="Cargar horarios")
        buttonCH.clicked.connect(self.loadSchedules)

        HLayout.addWidget(buttonCM)
        HLayout.addWidget(buttonCH)

        VLayout.addWidget(self.subject_list)
        #VLayout.addWidget(self.check_subject_list)
        VLayout.addLayout(HLayout)

        self.setLayout(VLayout)
        
    
    def loadSubject(self):
        list = UseCaseGetSubjects.execute()
        i = 0
        for elem in list:
            item = QListWidgetItem()
            item.setText(elem.__str__())
            self.subject_list.insertItem(i, item)
            i = i +1

    def loadSchedules(self):
        pass

    def selectSubject(self):
        print(self.subject_list.currentItem().text())


if __name__ in "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    app.exec()