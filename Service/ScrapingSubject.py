import requests
from bs4 import BeautifulSoup
from Entity import Subject

def execute():
    url = "https://gestiondocente.info.unlp.edu.ar/reservas/consulta/xmateria"
    list = []
    result = requests.get(url)

    if result.status_code == 200:
        soup = BeautifulSoup(result.text, "html.parser") #, "html.parser"

        options = soup.find("select", id="reservas_consultaxmateria_materia").findAll("option")
    
        for item in options:
            value = item["value"]
            name = item.get_text()
            list.append(Subject.Subject(value, name))
    
    return list