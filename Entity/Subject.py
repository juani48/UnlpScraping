class Subject:
    value = 0
    name = ""

    def __init__(self, value, name):
        self.value = value
        self. name = name

    def __str__(self):
        return str(self.value) + " - " + self.name
    