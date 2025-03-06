class Schedule:
    classroom = ""
    confirmed = False
    type = ""
    day = 0
    start = ""
    end = ""

    def __init__(self, aula, confirmado, tipo, dia, start, fin):
        self.classroom = aula; self.confirmed = confirmado; self.type = tipo; self.day = dia; self.start = start; self.end = fin

    def __str__(self):
        return self.classroom + "\n" + str(self.confirmed) + "\n" + self.type + "\n" + str(self.day) + "\n" + self.start + "\n" + self.end
                    