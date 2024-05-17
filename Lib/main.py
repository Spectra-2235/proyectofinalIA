# Importar la biblioteca CSV
import csv

# Declarar listas y variables
materia=[]
primerDia=[]
sdoDia=[]
inicioClase=[]
finClase=[]
seEntendio=[]

listaDeValores=[]
datosTotales=36
datos_si= 16
datos_no=20

# Definir función para leer datos desde el archivo CSV
def leer_datos():
    global entendimientoclases_sdoDia, entendimientoclases_sdoDia
    with open('DataSet_utilizar.csv', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)  # Saltar la primera fila (encabezados)

        for row in csv_reader:
            # Leer datos y almacenar en listas respectivas
            materia.append(row[0])
            primerDia.append(row[1])
            sdoDia.append(row[2])
            inicioClase.append(row[3])
            finClase.append(row[4])
            seEntendio.append(row[5])



# Definir función para calcular estadísticas
def sacar_stats():
    # Inicializar contadores para diferentes variables
    n = 0
    n1, n2, n3, n4, n5, n6,n7,n8,n9,n10,n11,n12 = 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0

    # Estadísticas para la variable 'materia'
    for i in materia:
        if i == 'Inteligencia de Negocios' and seEntendio[n] == 'si':
            n1 += 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and seEntendio[n] == 'si':
            n2 += 1
        if i == 'Topico I' and seEntendio[n] == 'si':
            n3 += 1
        if i == 'Administración de proyectos de software' and seEntendio[n] == 'si':
            n4 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and seEntendio[n] == 'si':
            n5 += 1
        if i == 'Ingles VI' and seEntendio[n] == 'si':
            n6+=1
        if i == 'Inteligencia de Negocios' and seEntendio[n] == 'no':
            n7+= 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and seEntendio[n] == 'no':
            n8 += 1
        if i == 'Topico I' and seEntendio[n] == 'no':
            n9 += 1
        if i == 'Administración de proyectos de software' and seEntendio[n] == 'no':
            n10 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and seEntendio[n] == 'no':
            n11 += 1
        if i == 'Ingles VI' and seEntendio[n] == 'no':
            n12 += 1
        n += 1
    # Almacenar resultados en listaDeValores
    listaDeValores.extend([n1, n2, n3, n4, n5, n6,n7,n8,n9,n10,n11,n12])

    # Estadísticas para la variable 'inicioClase'
    n = 0
    n1, n2,n3,n4 = 0, 0,0,0
    for i in inicioClase:
        if (i == '07:00' or i== '8:00' or i == '09:00') and seEntendio[n] == 'si':
            n1 += 1
        if( i== '10:00' or i=='11:00') and seEntendio[n] == 'si':
            n2+=1
        if (i == '07:00' or i== '8:00' or i == '09:00' ) and seEntendio[n] == 'no':
            n3 += 1
        if (i == '10:00' or i == '11:00') and seEntendio[n] == 'no':
            n4 += 1
        n += 1
    listaDeValores.extend([n1, n2,n3,n4])

    # Estadísticas para la variable 'FinClase'
    n = 0
    n1, n2,n3,n4= 0, 0,0,0
    for i in finClase:
        if (i == '09:00' or i=='10:00' or i == '11:00') and seEntendio[n] == 'si':
            n1 += 1

        if( i == '01:00' or i=='02:00') and seEntendio[n] == 'si':
            n2 += 1

        if (i == '09:00' or i=='10:00' or i == '11:00') and seEntendio[n] == 'no':
            n3 += 1

        if (i == '01:00' or i == '02:00') and seEntendio[n] == 'no':
            n4 += 1
        n += 1
    listaDeValores.extend([n1, n2,n3,n4])

    # Estadísticas para la variable 'primerDia'
    n = 0
    n1, n2, n3, n4, n5, n6, n7, n8 = 0, 0, 0, 0, 0, 0, 0, 0

    for i in primerDia:
        if i == 'Lunes' and seEntendio[n] == 'si':
            n1 += 1
        if i == 'Martes' and seEntendio[n] == 'si':
            n2 += 1
        if i == 'Miercoles' and seEntendio[n] == 'si':
            n3 += 1
        if i == 'Jueves' and seEntendio[n] == 'si':
            n4 += 1
        if i == 'Lunes' and seEntendio[n] == 'no':
            n5 += 1
        if i == 'Martes' and seEntendio[n] == 'no':
            n6 += 1
        if i == 'Miercoles' and seEntendio[n] == 'no':
            n7 += 1
        if i == 'Jueves' and seEntendio[n] == 'no':
            n8 += 1
        n += 1
    listaDeValores.extend([n1, n2, n3, n4, n5, n6, n7, n8])

    # Estadísticas para la variable 'SegundoDia'
    n = 0
    n1, n2, n3, n4, n5, n6, n7, n8 = 0, 0, 0, 0, 0, 0, 0, 0

    for i in sdoDia:
        if i == 'Lunes' and seEntendio[n] == 'si':
            n1 += 1
        if i == 'Martes' and seEntendio[n] == 'si':
            n2 += 1
        if i == 'Miercoles' and seEntendio[n] == 'si':
            n3 += 1
        if i == 'Jueves' and seEntendio[n] == 'si':
            n4 += 1
        if i == 'Lunes' and seEntendio[n] == 'no':
            n5 += 1
        if i == 'Martes' and seEntendio[n] == 'no':
            n6 += 1
        if i == 'Miercoles' and seEntendio[n] == 'no':
            n7 += 1
        if i == 'Jueves' and seEntendio[n] == 'no':
            n8 += 1
        n += 1
    listaDeValores.extend([n1, n2, n3, n4, n5, n6, n7, n8])

#---------------------------------------------------------------------------------------------------

  # Estadísticas para la variable 'seEntendio'
    n = 0
    n1, n2 = 0, 0
    for i in materia:

        if seEntendio[n] == 'si':
            n1 += 1
        if seEntendio[n] == 'no':
            n2 += 1

        n += 1

    # Actualizar variables globales
    datos_si, datos_no = n1, n2
    datos_totales = int(n1 + n2)

    # Asegurarse de que no haya valores cero en listaDeValores
    k = 0
    for i in listaDeValores:
        if i == 0:
            listaDeValores[k] = 1
        k += 1

    # Llamar a la función 'pedir' con los datos calculados
    pedir(datos_si, datos_no)


# Definir función para solicitar datos al usuario y calcular probabilidades
def pedir(si, no):
    a = input("Selecciona la materia: 1: Inteligencia de Negocios, 2: Sistemas Inmersos y de Realidad Aumentada, 3: Topico I, 4: Administración de Proyectos de Software, 5: Pruebas y Aseguramiento de la Calidad de Software, 6: Ingles VI : ")
    b = input("Selecciona el primer día de la materia: 1: Lunes, 2: Martes, 3: Miercoles, 4: Jueves: ")
    c = input("Selecciona el segundo día de la materia: 1: Lunes, 2: Martes, 3: Miercoles, 4: Jueves: ")
    d = input("Selecciona el horario de inicio de la clase: 1: Entre 7:00 - 11:00: 2: 11:00 - 01:00, 3: 1:00 - 2:00 ")
    e = input("Selecciona el horario de fin de la clase: 1: Entre 9:00 - 11:00, 2: 11:00-2:00 ")


    Calcular(a,b,c,d,e,si,no)

def Calcular(n1, n2, n3, n4, n5,sis, non):
    datos_si, datos_no = sis, non
    global listaDeValores, datosTotales

    # Inicializar variables para probabilidades
    si, no = 0, 0
    suma = 0
    p_si, p_no = 0, 0


    print(len(listaDeValores))

    # Calcular probabilidades para la variable 'Materia'
    if n1 == "1":
        si = listaDeValores[0] / datosTotales
        no = listaDeValores[6] / datosTotales
    elif n1 == "2":
        si = listaDeValores[1] / datosTotales
        no = listaDeValores[7] / datosTotales
    elif n1 == "3":
        si = listaDeValores[2] / datosTotales
        no = listaDeValores[8] / datosTotales
    elif n1 == "4":
        si = listaDeValores[3] / datosTotales
        no = listaDeValores[9] / datosTotales
    elif n1 == "5":
        si = listaDeValores[4] / datosTotales
        no = listaDeValores[10] / datosTotales
    elif n1 == "6":
        si = listaDeValores[5] / datosTotales
        no = listaDeValores[11] / datosTotales

    # ---------------Primer Dia de clases -----------
    if n2 == "1":
        si *= listaDeValores[12] / datosTotales
        no *= listaDeValores[16] / datosTotales
   # -------------Segunda Dia de Clases ----------------
    if n3 == "1":
        si *= listaDeValores[20] / datosTotales
        no *= listaDeValores[24] / datosTotales
    # -----------------Inicio de Clase-----------------
    if n4 == "1":
        si *= listaDeValores[28] / datosTotales
        no *= listaDeValores[32] / datosTotales

    # ----------------Fin de Clase----------------
    if n5 == "1":
        si *= listaDeValores[31] / datosTotales
        no *= listaDeValores[35] / datosTotales

    # Calcular probabilidades finales
    suma = si + no

    # Calcular probabilidades normalizadas
    p_si = (si / suma) * 100
    p_no = (no / suma) * 100

    # Imprimir resultados
    print(listaDeValores)
    print(si)
    print(no)
    print(suma)
    print("Calculando...")
    print("Si tiene más de 50% se aprendió lo suficiente, en caso de que sea menor a 50% no se aprendió lo suficiente.")
    print("Probabilidad de los que entendieron: ", round(p_si, 2))
    print("Probabilidad de los que no entendieron: ", round(p_no, 2))




# Leer datos del archivo CSV
leer_datos()


# Calcular estadísticas
sacar_stats()







































