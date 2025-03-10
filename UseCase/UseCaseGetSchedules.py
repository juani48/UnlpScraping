from Service import ScrapingSchedule
from PyQt6.QtWidgets import QListWidget, QListWidgetItem

def execute(values, names):
    list = []
    for i in range(len(values)):
        list.append(ScrapingSchedule.execute(values[i], names[i]))
    return list