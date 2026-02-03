"""🟢 Proyecto 1 – Gestor de tareas (CLI)
Qué hace
- Crear ✅, listar ✅, completar ✅  y eliminar tareas
- Guardar tareas en archivo (json o txt)
- Recuperar estado al reiniciar
Evalúa
- Listas y diccionarios
- Funciones
- Condicionales
- Archivos
- Flujo del programa
Aprobado si
- No se pierden los datos
- El código está modularizado
- No hay variables globales innecesarias"""
import json
import os

def cargar_tareas(leerlista):
    try:
        with open(leerlista, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    

def crear_tarea():
    tareas=[]
    print("-----TITULO DE LA TAREA-----")
    titulo=input()
    print("-----Descripcion de la tarea-----")
    descripcion=input()
    nueva_tarea={
        "titulo":titulo,
        "descripcion":descripcion,
        "complete":False
    }
    if os.path.exists("lista_tareas.json"):
        try:
            tareas=cargar_tareas("lista_tareas.json")
            if not isinstance(tareas, list): #pregunta si la instancia es algo en especial con la segunda variable
                tareas = [tareas] 
        except (json.JSONDecodeError, ValueError):
            tareas = []
    else:
        tareas = []

    tareas.append(nueva_tarea)
    
    with open("lista_tareas.json", "w") as f:
        json.dump(tareas, f, indent=4)
    print("¡Tarea guardada con éxito!")

def listar(tareasLeer):
    lista=cargar_tareas(tareasLeer)
    for tarea in lista:
        print("{}\n\t{}".format(tarea["titulo"],tarea["descripcion"]))
    
        
def completar():
    lista=cargar_tareas("lista_tareas.json")
    listar("lista_tareas.json")
    opc=input("-- QUE TAREA QUIERE COMPLETAR --")
    for tarea in lista:
            if tarea["titulo"]==opc:
                if os.path.exists("tareas_completadas.json"):
                    try:
                        tareas=cargar_tareas("tareas_completadas.json")
                        if not isinstance(tareas, list): #pregunta si la instancia es algo en especial con la segunda variable
                            tareas = [tareas] 
                    except (json.JSONDecodeError, ValueError):
                        tareas = []
                else:
                    tareas = []
                tarea_completada={
                    "titulo":tarea["titulo"],
                    "descripcion":tarea["descripcion"],
                    "complete":True
                }
                tareas.append(tarea_completada)

                with open("tareas_completadas.json", "w") as f:
                    json.dump(tareas, f, indent=4)
                eliminar(opc)
                return print("¡Tarea completada con éxito!")

def eliminar(opc):
    tareas=cargar_tareas("lista_tareas.json")
    index=0
    for tarea in tareas:       
        if tarea["titulo"]==opc:
            if os.path.exists("lista_tareas.json"):
                try:
                    if not isinstance(tareas, list): #pregunta si la instancia es algo en especial con la segunda variable
                        tareas = [tareas] 
                except (json.JSONDecodeError, ValueError):
                    tareas = []
            del tareas[index]
            with open("lista_tareas.json", "w") as f:
                json.dump(tareas, f, indent=4)
            return print("¡Tarea eliminada con éxito!")
        index=index+1
    print("La tarea no existe intente de nuevo")

def main():
    while True:
        opcion=input("---SELECCIONA UNA OPCION---\
            \n 1) Crear tarea nueva\
            \n 2) Ver tareas\
            \n 3) Completar tarea\
            \n 4) Eliminar tarea\" \
            \n 5) Tareas completadas\
            \n 6) Salir")
        if opcion=="1":
            crear_tarea()
        elif opcion=="2":
            listar("lista_tareas.json")
        elif opcion=="3":
            completar()
        elif opcion=="4":
            listar("lista_tareas.json")
            opc=input("Que tarea quieres eliminar:")
            eliminar(opc)
        elif opcion=="5":
            listar("tareas_completadas.json")
        elif opcion=="6":
            return
        else:
            print("Opcion no valida escoga una nueva")
            
    

if __name__ == "__main__":
    main()