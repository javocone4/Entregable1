import csv
import requests
import time
import json
import string
import os
import errno

contador_palabras = {} # Inicializamos el diccionario que cuenta las palabras
while True :
    URL = "https://thesimpsonsquoteapi.glitch.me/quotes"
    data = requests.get(url = URL)
    quote = data.json()
  # Cogemos la quote y el personaje del JSON recibido y la guardamos en info_general
    frase = quote[0]['quote']
    personaje = quote[0]['character']
    words = frase.split() #Sparamos str en lista
#Conteo de palabras
    #Vamos añadiendo las palabras que hemos encontrado al diccionario por medio del bucle
    for word in words:
      value = 1
      word = word.translate(str.maketrans('', '', string.punctuation))
      if word not in contador_palabras:
        contador_palabras[word] = value
        
      value = words.count(word)
      contador_palabras[word] += value

    info_general = [personaje, frase]
# Creamos fichero de texto donde vamos almacenando la cuenta de palabras
    with open ('/Users/javier/Documents/GitHub/Entregable1/Lisa/CuentaPalabras.txt', 'w') as cuentapalabras:
      for clave, valor in contador_palabras.items():
        cuentapalabras.write(f"\n{clave}: {valor}")

    personaje: str = quote[0]['character']
    frase: str = quote[0]['quote']
    URL_imagen:str = quote[0]['image']
#DESCARGA DE LA IMAGEN
    
    imagen = requests.get(URL_imagen).content
  
    try:
        os.mkdir(f"/Users/javier/Documents/GitHub/Entregable1/Lisa/{personaje}")
        imagen_local = f"/Users/javier/Documents/GitHub/Entregable1/Lisa/{personaje}/{personaje}.png" 


        if personaje == 'Homer Simpson':
            my_dict = {"frase": frase, "nombre": personaje}
            with open(f"/Users/javier/Documents/GitHub/Entregable1/Lisa/{personaje}/{personaje}.csv" , 'a') as f:  # You will need 'wb' mode in Python 2.x
                a = csv.DictWriter(f, my_dict.keys())
                a.writerow(my_dict)

        elif personaje == 'Lisa Simpson':
            my_dict3 = {"frase": frase, "nombre": personaje}
            with open(f'/Users/javier/Documents/GitHub/Entregable1/Lisa/{personaje}/{personaje}.csv', 'a') as h:  # You will need 'wb' mode in Python 2.x
                a = csv.DictWriter(h, my_dict3.keys())
                a.writerow(my_dict3)

        my_dict2 = {"frase": frase, "nombre": personaje}
        with open('/Users/javier/Documents/GitHub/Entregable1/Lisa/general.csv', 'a') as g:  # You will need 'wb' mode in Python 2.x
            a = csv.DictWriter(g, my_dict2.keys())
            a.writerow(my_dict2)


        with open(imagen_local, 'wb') as handler:
            handler.write(imagen) 

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    time.sleep(30)



  