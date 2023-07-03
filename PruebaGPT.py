import itertools
import math

def calculate_distance(point1, point2):
    # Calcula la distancia de Manhattan entre dos puntos en un plano
    x1, y1 = point1
    x2, y2 = point2

    distance = abs(x2 - x1) + abs(y2 - y1)
    
    return distance

def calculate_total_distance(route, locations):
    # Calcula la distancia total de un recorrido dado una ruta y las ubicaciones
    total_distance = 0
    for i in range(len(route) - 1):
        location1 = locations[route[i]]
        location2 = locations[route[i + 1]]
        distance = calculate_distance(location1, location2)
        total_distance += distance
    return total_distance

def two_opt(route, locations):
    # Algoritmo 2-opt para mejorar la ruta
    best_route = route
    best_distance = calculate_total_distance(best_route, locations)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                new_distance = calculate_total_distance(new_route, locations)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_route = new_route
                    improved = True
        route = best_route

    return best_route, best_distance

# Ejemplo de uso
locations = {0: (-32.767885614827165, -58.731060345254896), 
             1: (-32.817013149904874, -59.43170916108848), 
             2: (-33.3149002535801, -59.5179832062202), 
             3: (-32.56723322753103, -58.578878459892714), 
             4: (-33.889057602127316, -58.202359871258324), 
             5: (-32.403682327398705, -58.41951772895256), 
             6: (-33.65119713562012, -58.492082006200306), 
             7: (-33.18051827552436, -58.99001741697835), 
             8: (-33.48693699480803, -57.98316800218268), 
             9: (-33.66470231520934, -58.735498982069565), 
             10: (-33.85374910666364, -59.17458595364147), 
             11: (-33.11306375837259, -59.03389910683172), 
             12: (-33.90727120585439, -59.51162010927947), 
             13: (-33.593258970032586, -58.00106109368794), 
             14: (-33.2759740164253, -58.81458378555352), 
             15: (-33.186765192266016, -57.748991586593135), 
             16: (-33.39740113136772, -59.09420500285579), 
             17: (-32.129109631368195, -58.491909966858785), 
             18: (-33.36019031856498, -58.610242411432004), 
             19: (-32.33437732191952, -58.23233126023716), 
             20: (-32.51883851063152, -59.29518787039548), 
             21: (-32.65890206808134, -59.46387848053976)}

# Definir la secuencia inicial de visitas
initial_route = list(range(len(locations)))
initial_route.append(0)     # Ejemplo de secuencia inicial

# Calcular la mejor ruta y distancia utilizando el algoritmo 2-opt
best_route, best_distance = two_opt(initial_route, locations)

# Imprimir resultados
print("Mejor ruta:", best_route)
print("Distancia total:", best_distance)
    
    