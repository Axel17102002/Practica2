# Imprime una tabla con los datos de cada jugador de una ronda
def imprimir_tabla(round):
    # Línea divisoria para separar la tabla
    line = "-"*60
    print("Jugador    Kills    Asistencias    Muertes    MVPs    Puntos")
    print(line)
    # Imprimimos los datos de cada jugador
    for player, data in round.items():
        print(f'{player:10} {data["kills"]:6} {data["assists"]:12} {data["deaths"]:8} {data["MVP"]:6} {data["points"]:7}')
    print(line)

#Ordena de manera decreciente los datos del diccionario según el puntaje   
def sorting_player_stats(round):
    def get_points(player):
        return player[1]["points"]
    return sorted(round.items(), key = get_points, reverse = True) #ordena de mayor a menor

# Importamos las constantes definidas externamente para calcular los puntajes
from const import KILL, ASISTENCIA, MUERTE

# Crea las estadísticas de una ronda a partir de los datos del enunciado
def create_stats(round):
    round_stats = {}
    #Calculamos el mejor jugador de la ronda, es una funcion interna que solo usa la funcion crear_estadistica
    def calcular_MVP(est_rond):
        max_points = -1
        mvp_player = -1
        for player, data in est_rond.items(): 
            if data["points"] > max_points:
                max_points = data["points"]
                mvp_player = player
        return mvp_player
        #Devulve el nombre del mejor jugador(MVP)
   
    # Recorremos cada jugador de la ronda para calcular sus estadísticas
    for player, data in round.items():

        kills = data["kills"]
        assists = data["assists"]
        deaths = 1 if data["deaths"] else 0 # Convertimos booleano a 1 o 0
        
        #Calculamos los puntos con las constantes predefinidas
        points = kills * KILL + assists * ASISTENCIA + deaths * MUERTE

        #Cargamos los datos de cada jugador 
        round_stats[player] ={
            "kills": kills,
            "assists": assists,
            "deaths": deaths,
            "MVP": 0,
            "points": points
            
        }
    # Calculamos el MVP de la ronda y lo marcamos
    mvp_player = calcular_MVP(round_stats)
    round_stats[mvp_player]["MVP"] = 1

    round_stats = dict(sorting_player_stats(round_stats))
    return round_stats #Devolvemos las estadisticas de la ronda


# Esta función acumula los totales por jugador a lo largo de las rondas
def estadisticas_totales(round_stats,total_stats): 
    # Si el jugador no está en el diccionario total lo inicializamos con todos los datos en 0
    for player, data in round_stats.items():
        if player not in total_stats:
            total_stats[player] = {
            "kills": 0,
            "assists": 0,
            "deaths": 0,
            "MVP": 0,
            "points": 0
    }
        # Sumamos las estadísticas de esta ronda al total
        total_stats[player]["kills"] += data["kills"]
        total_stats[player]["assists"] += data["assists"]
        total_stats[player]["deaths"] += data["deaths"]
        total_stats[player]["MVP"] += data["MVP"]
        total_stats[player]["points"] += data["points"]

    