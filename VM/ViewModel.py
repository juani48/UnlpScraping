from UseCase import UseCaseGetSubjects
from UseCase import UseCaseGetSchedules


class ViewModel:

    def __init__(self):
        self.unselected_subject_list = []
        self.selected_subject_list = []
        self.loadSubject()

    def getSelected(self):
        return self.selected_subject_list
    def getUnselected(self):
        return self.unselected_subject_list

    def loadSubject(self):
        self.load = True
        self.unselected_subject_list = UseCaseGetSubjects.execute()

    def select(self, text, select):
        # subject selected
        if select:
            index = self.unselected_subject_list.index(text)
            item = self.unselected_subject_list[index]
            del self.unselected_subject_list[index]
            self.selected_subject_list.append(item)
        # subject unselected
        else:
            index = self.selected_subject_list.index(text)
            item = self.selected_subject_list[index]
            del self.selected_subject_list[index]
            self.unselected_subject_list.append(item)

    def loadSchedules(self):
        values = []
        names = []
        for i in range(0, len(self.selected_subject_list)):
            value = int(self.selected_subject_list[i].split()[0])
            name = str(self.selected_subject_list[i].split("-")[1].split("(")[0])
            name = name.replace(" ", "", 1)
            values.append(value)
            names.append(name)
        return UseCaseGetSchedules.execute(values, names)

    def searchSubject(self, string):
        list = []
        string = string.lower()
        for elem in self.getUnselected():
            if string in elem.lower() and elem not in list:
                list.append(elem)
        return list

        

