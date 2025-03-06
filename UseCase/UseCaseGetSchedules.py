from Service import ScrapingSchedule

def execute(values):
    list = []

    for value in values:
        list.append(ScrapingSchedule.execute(value))
    return list