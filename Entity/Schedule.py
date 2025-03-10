class Schedule:
    subject = ""
    classroom = ""
    confirmed = False
    type = ""
    day = 0
    start = ""
    end = ""

    def __init__(self, subject, classroom, confirmed, type, day, start, end):
        self.subject = subject; self.classroom = classroom; self.confirmed = confirmed; self.type = type; self.day = day; self.start = start; self.end = end

    def __str__(self):
        return self.classroom + "\n" + str(self.confirmed) + "\n" + self.type + "\n" + str(self.day) + "\n" + self.start + "\n" + self.end
                    