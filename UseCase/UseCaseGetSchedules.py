from Service import ScrapingSchedule
from PyQt6.QtWidgets import QListWidget, QListWidgetItem

def execute(values):
    list = []
    for value in values:
        list.append(ScrapingSchedule.execute(value))
    return list