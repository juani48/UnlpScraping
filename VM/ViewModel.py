from UseCase import UseCaseGetSubjects
from UseCase import UseCaseGetSchedules


class ViewModel:

    def __init__(self):
        self.unselected_subject_list = []
        self.selected_subject_list = []
        self.load = False

    def loadSubject(self):
        if not self.load:
            self.load = True
            self.unselected_subject_list = UseCaseGetSubjects.execute()
            return self.unselected_subject_list
        else:
            print("Ya cargadas")
            return []

    def selectSubject(self, index):
        item = self.unselected_subject_list[index]
        del self.unselected_subject_list[index]

        self.selected_subject_list.append(item) 

    def unselectSubject(self, index):
        item = self.selected_subject_list[index]
        del self.selected_subject_list[index]

        self.unselected_subject_list.append(item)

    def loadSchedules(self):
        values = []
        for i in range(0, len(self.selected_subject_list)):
            value = int(self.selected_subject_list[i].split()[0])
            values.append(value)
        
        list = UseCaseGetSchedules.execute(values)
        for i in list:
            for j in i:
                print(j)
            print("---")

