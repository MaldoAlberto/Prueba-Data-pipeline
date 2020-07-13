#!/bin/bash
# -*- coding: utf-8 -*-
import time
import unittest
def prueba():
	#Verificar la existencia del archivo
	import os
	namepath = '/home/mb.csv' # se descarga el archivo en la ruta namepath
	if os.path.exists(namepath):
	  os.remove(namepath) # se actualiza el archivo, es decir, si existe se reemplaza por otro 

	# Descargar el archivo del metrobus
	import wget
	url = 'https://datos.cdmx.gob.mx/explore/dataset/prueba_fetchdata_metrobus/download/?format=csv&timezone=America/Mexico_City&lang=es&use_labels_for_header=true&csv_separator=%2C' #link del archivo
	wget.download(url,namepath) #sentencia para descargar el archivo

	# Leer el archivo
	import pandas as pd
	df = pd.read_csv(namepath) # se lee el archivo en u ndataframe
	
	
	# indica en geographic_poiint  la columna que tiene las coordenadas para cada instancia
	coords = df["geographic_point"]

	# Identificar a partir de la posicion a que alcaldia pertenece
	from geopy.geocoders import Nominatim # se hace uso de una ibreria llamada geopy
	import certifi
	from six.moves import urllib
	def uo(args, **kwargs):
		return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)
	geolocator = Nominatim()
	geolocator.urlopen = uo # indica po medio de una solicitud http la posicion en el mapa de esas coordenadas dando una serie de datos como pais, estado, ciudad, alcaldia, colonia, calle, codigo postal  

	alcaldia = []
	for i in coords: # se genera una lista de las alcaldias de cada instancia
		try:
			location = geolocator.reverse(i, language='en')
			li = list(location.address.split(","))
			alcaldia.append(li[len(li)-4]) # se alamcena la alcaldia
			#print(k)
			
		except:
			alcaldia.append("") # en caso contrario no se considera alaldia alguna.
	df['alcaldia'] = alcaldia


	# se almacena en Mongodb
	from flask import Flask
	from flask_graphql import GraphQLView
	from pymongo import MongoClient
	import graphene

	client =  MongoClient("mongodb+srv://toto:toto@clustertest.pyelj.mongodb.net/toto?retryWrites=true&w=majority") # dirección de mi base de datos
	db = client['toto']
	collection = db['toto']
	df.reset_index(inplace=True)
	data_dict = df.to_dict("records")
	collection.insert_many(data_dict)

	#se repite el proceso
	return True
	time.sleep(3600) # una hora
