#FlavioCea_PGY1121_009_d
import funciones as fn
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

asientos = np.zeros((),int)

while True:
    os.system("cls")
    print("Bienvenido")
    ver_menu=fn.ver_menu()
    opc=fn.validar_opcion()
    if opc==1:
        fn.comprar_ent()
    elif opc==2:
        fn.ver_asientos()
    elif opc==3:
        fn.ver_asistentes()
    elif opc==4:
        fn.ver_ganancias
    else:
        fn.salir()