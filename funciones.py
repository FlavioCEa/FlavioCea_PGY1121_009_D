#Funciones
import os
import time
import numpy as np

contador_entradas=0
acumulador_entradas=0
precio_silver=50000
precio_gold=80000
precio_platinum=120000


lista_filas=[]
lista_columnas=[]
lista_ruts=[]
lista_nombres=[]
lista_entradas=[]
lista_cant=[]

asientos = np.zeros((),int)



#Funciones complementarias


def ver_asientos():
    print("ASIENTOS")
    for x in range(10):
        print(f"FILA {x+1}:", end="  ")
        for y in range(10):
            print(f"{y+1}:{asientos} ", end=" ")
        print()
    print("Columnas|1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10  |")

def ver_menu():
    print("""\t\tMENú
    \t1. Comprar entradas
    \t2. Ubicaciones Disponibles
    \t3. lista de asistentes
    \t4. Ganancias
    \t5. Salir""")

def validar_opcion():
    while True:
        try:
            opc=int(input("Ingrese una opcion del menú: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR!! DEBE INGRESAR SOLO OPCIONES DEL MENÚ")
        except:
            print("ERROR!! SOLO DEBE INGRESAR NÚMEROS ENTEROS")

def validar_cantidad_entr():
    while True:
        try:    
            cant=int(input("Cuantas entadas desea comprar tiene un limite de 1-3: "))
            if cant>=1 and cant<=3:
                lista_cant.append(cant)
                return cant
            else:
                print("Debes comprar de 1 a 3 entradas!!")
        except:
            print("ERROR!! DEBE INGRESAR SOLO NUMEROS ENTEROS")
        contador_entradas=contador_entradas+cant
def menu_precios():
    precio_silver=50000
    precio_gold=80000
    precio_platinum=120000
    global acumulador_entradas
    while True:
        try:
            opc_prec=int(input("Que opcion elige(indique numero 1,2 o 3): "))
            if opc_prec==1:
                acumulador_entradas=acumulador_entradas+precio_silver
                return opc_prec
            elif opc_prec==2:
                acumulador_entradas=acumulador_entradas+precio_gold
                return opc_prec
            elif opc_prec==3:
                acumulador_entradas=acumulador_entradas+precio_platinum
                return opc_prec
            else:
                print("Debe ingresar solo opciones del menu")
        except:
            print("ERROR!! DEBE INGRESAR SOLO NUMEROS ENTEROS")
def ver_precios():
     print("""Cual entrada desea comprar tiene 3 opciones:
                1. Silver = 50.000 $
                2. Gold = 80.000 $
                3. Platinum = 120.000 $""")
def validar_nombre():
    while True:
        nombre=input("Ingrese solo su primer nombre: ")
        if nombre.strip() and nombre.isalpha():
            lista_nombres.append(nombre)
            return nombre
        else:
            print("Debe ingresar solo su primer nombre sin espacios")

def ver_ganancias():
    ganancias=acumulador_entradas
    print(f"{ganancias}")
    return ganancias

def validar_fila():
    while True:
        try:
            print("COMPRAR ASIENTOS")
            fila=int(input("Ingrese la FILA: "))
            if fila>=1 and fila<=10:
                lista_filas.append(fila)
                return fila
            else:
                print("Ingrese un número de fila valido")
        except:
            print("ERROR!! DEBES INGRESAR SOLO NÚMEROS ENTEROS")
def validar_columna():
    while True:
        try:
            print("COMPRAR ASIENTOS")
            columna=int(input("Ingrese la COLUMNA: "))
            if columna>=1 and columna<=10:
                lista_columnas.append(columna)
                return columna
            else:
                print("Ingrese un número de columna valido")
        except:
            print("ERROR!! DEBES INGRESAR SOLO NÚMEROS ENTEROS")
def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese RUT(sin digito verficador): "))
            if rut>=1000000 and rut<=99999999:
                lista_ruts.append(rut)
                return rut
            else:
                print("Debes ingresar un RUT valido")
        except:
            print("ERROR!! DEBE INGRESAR SOLO NÚMEROS ENTEROS")
#Funciones Ejecutables


def comprar_ent():
    validar_cantidad_entr()
    ver_precios()
    menu_precios()
    validar_fila()
    validar_columna()
    validar_rut()
    validar_nombre()
def ver_asistentes():
    print(f"""Asistentes:""")
    lista_menor=[lista_nombres.sort()]
    lista_menor.reverse()
    print(f"Asistentes: {lista_menor}")
def ganancias():
    ver_ganancias()
def salir():
    print("Adios y que disfrute de la funcion")
