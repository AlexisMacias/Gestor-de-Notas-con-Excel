import pandas as pd
import os
import numpy as np

#Nombre del archivo y la hoja 
file_name = "Notas.xlsx"
sheet_name = "Hoja1"

def cargar_notas():
    #Cargar las notas desde la ruta que se le de, comprobando que si exista primeramente
    try:
        #Cargar el archivo
        if os.path.exists(file_name):
            pd.read_excel(file_name, sheet_name=sheet_name)
        
        else:
            df = pd.DataFrame(columns= ["Id", "Título", "Cátegoria", "Contenido"])
            df.to_excel(file_name, sheet_name=sheet_name, index= False)
            return df
    except Exception as e:
        print(f"error al cargar archivo de notas {e}")


def agregar_notas(titulo, categoria, contenido):
    #Agregar una nueva nota a la hoja de cálculo
    df = cargar_notas()
    Nueva_nota = pd.DataFrame({
        "id" : [df.shape[0] +1],
        "Titulo" : [titulo],
        "Categorio" : [categoria],
        "Contenido" : [contenido]
    })

    df = pd.concat([df, Nueva_nota], ignore_index= True)
    df.to_excel(file_name, sheet_name=sheet_name, index= False)
    print("La nota se agrego Exitosamente")
    
