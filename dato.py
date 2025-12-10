import csv
import pathlib #alternativa puede ser libreria os

def leer_csv_login(ruta_archivo):
    ruta = pathlib.Path(ruta_archivo)
    datos = []
    with open(ruta,newline='',encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)# este devuelve como un diccionario, reader devuelve un string nomas

        for fila in lector:
            debe_funcionar = fila["debe_funcionar"].lower()  == "true"

            datos.append((fila["usuario"], fila["password"], fila["debe_funcionar"]))# traemos el dato antes, lo comparaamos y lo guardamoe en variable
            
    return datos

    #formatea la lista