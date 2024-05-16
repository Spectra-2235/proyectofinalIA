# Importar la biblioteca CSV
import csv

# Declarar listas y variables
materia=[]
primerDia=[]
sdoDia=[]
inicioClase=[]
finClase=[]
entedendimientoClase_primerDia=[]
entendimientoclases_sdoDia=[]

listaDeValores=[]
datosTotales=48
datos_excelente= 17
datos_Poco=16
datos_Normal=15

# Definir función para leer datos desde el archivo CSV
def leer_datos():
    global entendimientoclases_sdoDia, entendimientoclases_sdoDia
    with open('Dataset.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)  # Saltar la primera fila (encabezados)

        for row in csv_reader:
            # Leer datos y almacenar en listas respectivas
            materia.append(row[0])
            primerDia.append(row[1])
            sdoDia.append(row[2])
            inicioClase.append(row[3])
            finClase.append(row[4])
            entedendimientoClase_primerDia.append(row[5])
            entendimientoclases_sdoDia.append(row[6])

# Definir función para calcular estadísticas
def sacar_stats():
    # Inicializar contadores para diferentes variables
    n = 0
    n1, n2, n3, n4, n5, n6, n7, n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,n31,n32,n33,n34,n35,n36 = 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    # Estadísticas para la variable 'dia'
    for i in materia:
        if i == 'Inteligencia de Negocios' and entedendimientoClase_primerDia[n] == 'Excelente':
            n1 += 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and entedendimientoClase_primerDia[n] == 'Excelente':
            n2 += 1
        if i == 'Topico I' and entedendimientoClase_primerDia[n] == 'Excelente':
            n3 += 1
        if i == 'Administración de proyectos de software' and entedendimientoClase_primerDia[n] == 'Excelente':
            n4 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and entedendimientoClase_primerDia[n] == 'Excelente':
            n5 += 1
        if i == 'Ingles VI' and entedendimientoClase_primerDia[n] == 'Excelente':
            n6 += 1
        if i == 'Inteligencia de Negocios' and entedendimientoClase_primerDia[n] == 'Normal':
            n7 += 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and entedendimientoClase_primerDia[n] == 'Normal':
            n8 += 1
        if i == 'Topico I' and entedendimientoClase_primerDia[n] == 'Normal':
            n9 += 1
        if i == 'Administración de proyectos de software' and entedendimientoClase_primerDia[n] == 'Normal':
            n10 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and entedendimientoClase_primerDia[n] == 'Normal':
            n11 += 1
        if i == 'Ingles VI' and entedendimientoClase_primerDia[n] == 'Normal':
            n12 += 1
        if i == 'Inteligencia de Negocios' and entedendimientoClase_primerDia[n] == 'Poco':
            n13 += 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and entedendimientoClase_primerDia[n] == 'Poco':
            n14 += 1
        if i == 'Topico I' and entedendimientoClase_primerDia[n] == 'Poco':
            n15 += 1
        if i == 'Administración de proyectos de software' and entedendimientoClase_primerDia[n] == 'Poco':
            n16 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and entedendimientoClase_primerDia[n] == 'Poco':
            n17 += 1
        if i == 'Ingles VI' and entedendimientoClase_primerDia[n] == 'Poco':
            n18 += 1

        if i == 'Inteligencia de Negocios' and entendimientoclases_sdoDia[n] == 'Excelente':
            n19 += 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and entendimientoclases_sdoDia[n] == 'Excelente':
            n20 += 1
        if i == 'Topico I' and entendimientoclases_sdoDia[n] == 'Excelente':
            n21 += 1
        if i == 'Administración de proyectos de software' and entendimientoclases_sdoDia[n] == 'Excelente':
            n22 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and entendimientoclases_sdoDia[n] == 'Excelente':
            n23 += 1
        if i == 'Ingles VI' and entendimientoclases_sdoDia[n] == 'Excelente':
            n24 += 1
        if i == 'Inteligencia de Negocios' and entendimientoclases_sdoDia[n] == 'Normal':
            n25 += 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and entendimientoclases_sdoDia[n] == 'Normal':
            n26 += 1
        if i == 'Topico I' and entendimientoclases_sdoDia[n] == 'Normal':
            n27 += 1
        if i == 'Administración de proyectos de software' and entendimientoclases_sdoDia[n] == 'Normal':
            n28 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and entendimientoclases_sdoDia[n] == 'Normal':
            n29 += 1
        if i == 'Ingles VI' and entendimientoclases_sdoDia[n] == 'Normal':
            n30 += 1
        if i == 'Inteligencia de Negocios' and entendimientoclases_sdoDia[n] == 'Poco':
            n31 += 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and entendimientoclases_sdoDia[n] == 'Poco':
            n32 += 1
        if i == 'Topico I' and entendimientoclases_sdoDia[n] == 'Poco':
            n33 += 1
        if i == 'Administración de proyectos de software' and entendimientoclases_sdoDia[n] == 'Poco':
            n34 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and entendimientoclases_sdoDia[n] == 'Poco':
            n35 += 1
        if i == 'Ingles VI' and entendimientoclases_sdoDia[n] == 'Poco':
            n36 += 1
        n += 1
    # Almacenar resultados en listaDeValores
    listaDeValores.extend([n1, n2, n3, n4, n5, n6, n7, n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,n31,n32,n33,n34,n35,n36])

    # Estadísticas para la variable 'inicioClase'
    n = 0
    n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0
    for i in inicioClase:
        if (i == '07:00' or i == '09:00' or i=='11:00') and entedendimientoClase_primerDia[n] == 'Excelente':
            n1 += 1

        if (i == '07:00' or i == '09:00' or i=='11:00') and entedendimientoClase_primerDia[n] == 'Normal':
            n2 += 1

        if (i == '07:00' or i == '09:00' or i=='11:00') and entedendimientoClase_primerDia[n] == 'Poco':
            n3 += 1

        if (i == '07:00' or i == '09:00' or i=='11:00') and entendimientoclases_sdoDia[n] == 'Excelente':
            n4 += 1

        if (i == '07:00' or i == '09:00' or i=='11:00') and entendimientoclases_sdoDia[n] == 'Normal':
            n5 += 1

        if (i == '07:00' or i == '09:00' or i=='11:00') and entendimientoclases_sdoDia[n] == 'Poco':
            n6 += 1
        n += 1
    listaDeValores.extend([n1, n2, n3, n4, n5, n6])

    # Estadísticas para la variable 'FinClase'
    n = 0
    n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0
    for i in finClase:
        if (i == '09:00' or i == '11:00' or i == '01:00') and entedendimientoClase_primerDia[n] == 'Excelente':
            n1 += 1

        if (i == '09:00' or i == '11:00' or i == '01:00') and entedendimientoClase_primerDia[n] == 'Normal':
            n2 += 1

        if (i == '09:00' or i == '11:00' or i == '01:00') and entedendimientoClase_primerDia[n] == 'Poco':
            n3 += 1

        if (i == '09:00' or i == '11:00' or i == '01:00') and entendimientoclases_sdoDia[n] == 'Excelente':
            n4 += 1

        if (i == '09:00' or i == '11:00' or i == '01:00') and entendimientoclases_sdoDia[n] == 'Normal':
            n5 += 1

        if (i == '09:00' or i == '11:00' or i == '01:00') and entendimientoclases_sdoDia[n] == 'Poco':
            n6 += 1
        n += 1
    listaDeValores.extend([n1, n2, n3, n4, n5, n6])

    # Estadísticas para la variable 'primerDia'
    n = 0
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10,n11,n12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0

    for i in primerDia:
        if i == 'Lunes' and entedendimientoClase_primerDia[n] == 'Excelente':
            n1 += 1
        if i == 'Martes' and entedendimientoClase_primerDia[n] == 'Excelente':
            n2 += 1
        if i == 'Lunes' and entedendimientoClase_primerDia[n] == 'Normal':
            n3 += 1
        if i == 'Martes' and entedendimientoClase_primerDia[n] == 'Normal':
            n4 += 1
        if i == 'Lunes' and entedendimientoClase_primerDia[n] == 'Poco':
            n5 += 1
        if i == 'Martes' and entedendimientoClase_primerDia[n] == 'Poco':
            n6 += 1

        if i == 'Lunes' and entendimientoclases_sdoDia[n] == 'Excelente':
            n7 += 1
        if i == 'Martes' and entendimientoclases_sdoDia[n] == 'Excelente':
            n8 += 1
        if i == 'Lunes' and entendimientoclases_sdoDia[n] == 'Normal':
            n9 += 1
        if i == 'Martes' and entendimientoclases_sdoDia[n] == 'Normal':
            n10 += 1
        if i == 'Lunes' and entendimientoclases_sdoDia[n] == 'Poco':
            n11 += 1
        if i == 'Martes' and entendimientoclases_sdoDia[n] == 'Poco':
            n12 += 1
        n += 1
    listaDeValores.extend([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10,n11,n12])

    # Estadísticas para la variable 'SegundoDia'
    n = 0
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for i in sdoDia:
        if i == 'Miercoles' and entedendimientoClase_primerDia[n] == 'Excelente':
            n1 += 1
        if i == 'Jueves' and entedendimientoClase_primerDia[n] == 'Excelente':
            n2 += 1
        if i == 'Miercoles' and entedendimientoClase_primerDia[n] == 'Normal':
            n3 += 1
        if i == 'Jueves' and entedendimientoClase_primerDia[n] == 'Normal':
            n4 += 1
        if i == 'Miercoles' and entedendimientoClase_primerDia[n] == 'Poco':
            n5 += 1
        if i == 'Jueves' and entedendimientoClase_primerDia[n] == 'Poco':
            n6 += 1

        if i == 'Miercoles' and entendimientoclases_sdoDia[n] == 'Excelente':
            n7 += 1
        if i == 'Jueves' and entendimientoclases_sdoDia[n] == 'Excelente':
            n8 += 1
        if i == 'Miercoles' and entendimientoclases_sdoDia[n] == 'Normal':
            n9 += 1
        if i == 'Jueves' and entendimientoclases_sdoDia[n] == 'Normal':
            n10 += 1
        if i == 'Miercoles' and entendimientoclases_sdoDia[n] == 'Poco':
            n11 += 1
        if i == 'Jueves' and entendimientoclases_sdoDia[n] == 'Poco':
            n12 += 1
        n += 1
    listaDeValores.extend([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12])

    # Estadísticas para la variable 'entedendimientoClase_primerDia'
    n = 0
    n1, n2,n3 = 0, 0,0
    for i in entedendimientoClase_primerDia:
        if entedendimientoClase_primerDia[n] == 'Excelente':
            n1 += 1
        if entedendimientoClase_primerDia[n] == 'Normal':
            n2 += 1
        if entedendimientoClase_primerDia[n]=='Poco':
            n3+=1
        n += 1

    # Estadísticas para la variable 'entendimientoclases_sdoDia'
    n = 0
    n1, n2, n3 = 0, 0, 0
    for i in entendimientoclases_sdoDia:
        if entendimientoclases_sdoDia[n] == 'Excelente':
            n1 += 1
        if entendimientoclases_sdoDia[n] == 'Normal':
            n2 += 1
        if entendimientoclases_sdoDia[n] == 'Poco':
            n3 += 1
        n += 1

    # Actualizar variables globales
    datos_excelente, datos_Normal, datos_Poco = n1, n2,n3
    datosTotales = int(n1 + n2+n3)

    # Asegurarse de que no haya valores cero en listaDeValores
    k = 0
    for i in listaDeValores:
        if i == 0:
            listaDeValores[k] = 1
        k += 1

    # Llamar a la función 'pedir' con los datos calculados
    pedir(datos_excelente, datos_Normal,datos_Poco)


# Definir función para solicitar datos al usuario y calcular probabilidades
def pedir(Excelente, Normal,Poco):
    a = input("Selecciona la calificación de las materias que quieras ver: 1: Lunes y Martes, 2: Miercoles y Jueves")
    b = input(
        "Selecciona El Inicio de Clase: 1: 7:00, 2: 9:00, 3: 11:00 ")
    c = input(
        "Selecciona El Fin de la Clase: 1: 9:00, 2: 11:00, 3: 01:00")


    # Llamar a la función 'Calcular' con los datos ingresados por el usuario
    Calcular(a, b, c, Excelente, Normal,Poco)

# Definir función para calcular probabilidades
def Calcular(n1, n2, n3, n4, n5, excelente, normal,poco):
    datos_excelente, datos_Normal,datos_Poco = excelente, normal,poco
    global listaDeValores, datos_totales

    # Inicializar variables para probabilidades
    excelente, normal,poco = 0, 0,0
    suma = 0
    p_excelente, p_normal,p_poco = 0, 0,0

    # Calcular probabilidades para la variable 'Materia'


    #---------------- Inicio Clase ----------------

    # ---------------- Fin Clase ------------------

    # ---------------- Primer Clase ---------------

    # ---------------- Segundo Clase ---------------





# Leer datos del archivo CSV
leer_datos()

# Calcular estadísticas
sacar_stats()





















