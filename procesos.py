import os
from os import remove
import numpy as np
import re, math
from collections import Counter


Word = re.compile(r'\w+')
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = Word.findall(text)
     return Counter(words)



def distanciaCoseno(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine = get_cosine(vector1, vector2)
    return round(cosine,2)

def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return round(float(len(c)) / (len(a) + len(b) - len(c)),2)

def eliminarArchivo(nombre):
    dirname = os.path.dirname(__file__)
    remove(dirname+'/data'+str(nombre))
    
def buscarArchivos():
    dirname = os.path.dirname(__file__)
    contenido = os.listdir(dirname+'/data')
    return contenido

def leerArchivo(name):
    contenido = []
    dirname = os.path.dirname(__file__)
    with open(dirname+'/data'+str(name),"r") as archivo:
        for linea in archivo:
            contenido.append(linea)
    return contenido

def comparar(archivos):
    matriz = []
    archivos = archivos.split(',')
    for i in range(0,len(archivos)):
        respuesta=[]
        for j in range(0,len(archivos)):
            respuesta.append(distanciaCoseno(str(leerArchivo(archivos[i])),str(leerArchivo(archivos[j]))))
        matriz.append(respuesta)
    return matriz

def compararJacard(archivos):
    matriz = []
    archivos = archivos.split(',')
    for i in range(0,len(archivos)):
        respuesta=[]
        for j in range(0,len(archivos)):
            respuesta.append(get_jaccard_sim(str(leerArchivo(archivos[i])),str(leerArchivo(archivos[j]))))
        matriz.append(respuesta)
    return matriz
   


