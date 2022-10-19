# -*- coding: utf-8 -*-
"""Simpsons.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gXbkfk-G3zul0iqaQ2XSkfTlDc82EG1e

Entregable 1.
"""
import csv
import requests
import json
import time
import string
import os
import errno

ListGen = []
ListaHomer = []
ListaLisa = []


while True :
  URL = "https://thesimpsonsquoteapi.glitch.me/quotes"
  data = requests.get(url = URL)
  quote = data.json()


  personaje: str = quote[0]['character']
  frase: str = quote[0]['quote']
  URL_imagen:str = quote[0]['image']
#DESCARGA DE LA IMAGEN
  imagen_local = f"Lisa/{personaje}.png" 
  imagen = requests.get(URL_imagen).content
  
  
  

  if personaje == 'Homer Simpson':

    ListGen.append((personaje,frase))
      
    ListaHomer.append((personaje,frase))
   
  elif personaje == 'Lisa Simpson':

    ListGen.append((personaje,frase))
      
    ListaLisa.append((personaje,frase))

   
  ListGen.append((personaje,frase))

  my_dict2 = {"frase": frase, "nombre": personaje}
  with open('/Users/javier/Documents/GitHub/Entregable1/Lisa/general.csv', 'a') as g:  # You will need 'wb' mode in Python 2.x
    a = csv.DictWriter(g, my_dict2.keys())
    a.writerow(my_dict2)
    
  
  if personaje == 'Lisa Simpson':
    my_dict3 = {"frase": frase, "nombre": personaje}
    with open('/Users/javier/Documents/GitHub/Entregable1/Lisa/lisa.csv', 'a') as h:  # You will need 'wb' mode in Python 2.x
      a = csv.DictWriter(h, my_dict3.keys())
      a.writerow(my_dict3)
    

  if personaje == 'Homer Simpson':

    
    my_dict = {"frase": frase, "nombre": personaje}
    with open('/Users/javier/Documents/GitHub/Entregable1/Lisa/homer.csv', 'a') as f:  # You will need 'wb' mode in Python 2.x
     a = csv.DictWriter(f, my_dict.keys())
     a.writerow(my_dict) 
    
    
  try:
        os.mkdir(f"/Users/javier/Documents/GitHub/Entregable1/Lisa/{personaje}")
        imagen_local = f"/Users/javier/Documents/GitHub/Entregable1/Lisa/{personaje}/{personaje}.png" 
        
        with open(imagen_local, 'wb') as handler:
            handler.write(imagen) 
  except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
  

  time.sleep(0)



  