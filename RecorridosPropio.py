# Tomaremos una lista con direcciones en formato Maps (Calle, Número, Departamento, Provincia) y sus respectivas 
# longitudes y latitudes, por cada elemento en Places tenemos una lista en Lat_long con latitud en [0] y 
# longitud en [1] 
# Ejemplo Laprida 145, Salta, Argentina

Places = ['Laprida 145, Salta, Argentina', ] 
Lat_long = [[-33.00295695869777, -58.54860002269008], ]


# Función por si se quieren exceptuar o quitar una dirección en el recorrido actual.

def Eliminar(cadena):
    try:
        index = Places.index(cadena)
        Places.pop(index)
        Lat_long.pop(index)
    except ValueError:
        raise Exception("La dirección ingresada no existe o está mal escrita")


# Generamos el diccionario para hacer el recorrido, este tendrá un ID como key, que poseera dentro la dirección y
# las latitudes y longitudes.

Num = list(range(len(Places)))
Direcciones = []

for i, h, z in zip(Num, Places, Lat_long):
    
    Direcciones.append([i, [h, z]])


Diccionarioformateado = dict(Direcciones)


# ACLARACION: SE OMITEN LAS DIRECCIONES UTILIZADAS POR UNA CUESTION DE PRIVACIDAD.

Diccionarioformateado = {
                            0: ['Rocamora 28, Gualeguaychú, Entre Ríos', [-33.013044167100624, -58.5214368253566]], 
                            1: ['9 de Julio, Salta, Argentina', [-33.00295695869777, -58.54860002269008]] }


# Llevamos nuestro diccionario al formato necesario, tendremos una ubicacion actual, el recorrido y la lista con 
# las distancias calculadas con el método de Manhattan. Iterativamente seleccionara los puntos mínimos que no estén 
# previamente seleccionados hasta completar el recorrido.

array = [Diccionarioformateado.get(i) for i in range(len(Diccionarioformateado))]
array = [array[i].pop(1)for i in range(len(array))]

actual = array[0]
distancia =[]
recorrido = []
recorrido.append(Diccionarioformateado[0][0])


while len(recorrido) != len(Diccionarioformateado):
    
    for h,i in enumerate(array):
            
            absoluta = abs(actual[0] - i[0]) + abs(actual[1] - i[1])
            distancia.append(absoluta)
            
    listaminimos = []
    
    for h, m in enumerate(distancia):
        
        if Diccionarioformateado[h][0] not in recorrido:
            listaminimos.append(m)
    
    minimo = min(listaminimos)
    indice = distancia.index(minimo)
    recorrido.append(Diccionarioformateado[indice][0])
    actual = array[indice]
    distancia.clear()
print(recorrido)


def Link(cadena):
   '''
   Está función recibe la lista recorrido obtenida, y le da el formato HTML necesario, devolviendo un link del 
   recorrido.
   '''
   base = "https://www.google.com/maps/dir/"
   formatodestinos = cadena

   fdestinos = ""
   for i in formatodestinos:
      fdestinos = fdestinos + i + "/"
      
      fdestinos = fdestinos.replace(" ","+")
      
      urlrecorrido = base + fdestinos
   print(urlrecorrido)
