import requests

# Se utiliza la key necesaria para la utilización de APIs de Google Cloud Platform, la url de la API (también se
# puede utilizar la libreria de la API respectiva), los origenes y destinos. 

key = 'x' 
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
origenes = 'Avenida Rocamora 268, Gualeguaychú, Entre Ríos|San José 327, Gualeguaychú, Entre Ríos|Juan Jose Franco 964, Gualeguaychú, Entre Ríos'
destinos = origenes

# Definimos lo necesario, hacemos la request y lo pasamos a JSON.

r = (url + "&origins=" + origenes + "&destinations=" + destinos + "&key=" + key)
r = requests.get(url + "&origins=" + origenes + "&destinations=" + destinos + "&key=" + key)
r.json()

#Esto devuelve un JSON con la información respectiva de la combinación entre los origenes y destinos.