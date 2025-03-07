from Service import ScrapingSubject

def execute():
    list = ScrapingSubject.execute()
    listSTR = []
    for elem in list:
        listSTR.append(elem.__str__())
    return listSTR

