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
            df = pd.read_excel(file_name, sheet_name=sheet_name)
            return df
        
        else:
            df = pd.DataFrame(columns= ["Id", "Titulo", "Categoria", "Contenido"])
            df.to_excel(file_name, sheet_name=sheet_name, index= False)
            return df
    except Exception as e:
        print(f"error al cargar archivo de notas {e}")


def agregar_notas(titulo, categoria, contenido):
    #Agregar una nueva nota a la hoja de cálculo
    df = cargar_notas()
    Nueva_nota = pd.DataFrame({
        "Id" : [df.shape[0] +1],
        "Titulo" : [titulo],
        "Categoria" : [categoria],
        "Contenido" : [contenido]
    })

    df = pd.concat([df, Nueva_nota], ignore_index= True)
    df.to_excel(file_name, sheet_name=sheet_name, index= False)
    print("La nota se agrego Exitosamente")


def mostrar_notas():
    df = cargar_notas()

    if df.empty:
        print("Aún no hay notas en el archivo")
        
    else:
        print(f"\n{df}\n")


def filtrar_categoria():
    df = cargar_notas()

    if df.empty:
        print("No hay notas registradas aún")
        return
    
    while True:
        categoria = input("ingresa la categoria a buscar: ")

        if categoria in df["Categoria"].values:
            df_categoria = df[df["Categoria"] == categoria]
            print(f"\n{df_categoria}\n")
            break
        elif categoria == "":
            print("No escribiste ninguna categoria ingresa una categoría valida por favro")
        else:
            print("No hay categorias con ese nombre, por favor ingresa una categoría valida")
            break


def filtro_por_titulo():
    df = cargar_notas()

    if df.empty:
        print("No hay notas registradas aún")
        return
    
    while True:
        titulo = input("ingresa el titulo a buscar: ")

        if titulo in df["Titulo"].values:
            df_titulo = df[df["Titulo"] == titulo]
            print(f"\n{df_titulo}\n")
            break

        elif titulo == "":
            print("No escribiste ningun titulo ingresa una categoría valida por favor")

        else:
            print("No hay categorias con ese nombre, por favor ingresa una categoría valida")
            break


if __name__ == "__main__":
    while True:
        print("\nGestor de Notas en Excel\n")
        print("1. Mostar las notas")
        print("2. Agregar Nota")
        print("3. Filtrar por categoria")
        print("4. Filtrar por Titulo")
        print("5. Salir")

        opcion = int(input("ingresa el numero correspondiente a la opción que desee: \n"))

        if opcion == 1:
            mostrar_notas()

        elif opcion == 2:
            titulo = input("agrega el titulo a la nota: ")
            categoria = input("agrega la categoria a la que quieres que pertenezca la nota: ")
            contenido = input("agrega el contenido de la nota: ")
            agregar_notas(titulo, categoria, contenido)

        elif opcion == 3:
            filtrar_categoria()

        elif opcion == 4:
            filtro_por_titulo()

        elif opcion == 5:
            print("Esta saliendo del gestor de notas, gracias por usar")
            break

        else:
            print("opcion invalida")
