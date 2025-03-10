import requests
from Entity import Schedule


def _create_schedule(reservation, _name):
    name = _name
    classroom = reservation["aula"]
    confirmed = reservation["confirmada"]
    type = reservation["tipo"]
    day = reservation["dia"]
    start = reservation["horaInicio"]["h"] + ":" + reservation["horaInicio"]["m"] 
    end = reservation["horaFin"]["h"] + ":" + reservation["horaInicio"]["m"]
    return Schedule.Schedule(name, classroom, confirmed, type, day, start, end)


def execute(value, name):
    url = f"https://gestiondocente.info.unlp.edu.ar/reservas/consulta/xmateria/data/{value}"
    list = []
    result = requests.get(url)

    if result.status_code == 200:
        json = result.json()["reservas"]
    
        for elem in json:
            list.append(_create_schedule(elem, name))
    return list