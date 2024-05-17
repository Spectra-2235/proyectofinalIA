# Importar la biblioteca CSV
import csv

# Declarar listas y variables
materia=[]
primerDia=[]
sdoDia=[]
inicioClase=[]
finClase=[]
seEntenido=[]

listaDeValores=[]
datosTotales=36
datos_si= 16
datos_no=20

# Definir función para leer datos desde el archivo CSV
def leer_datos():
    global entendimientoclases_sdoDia, entendimientoclases_sdoDia
    with open('DataSet_utilizar.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)  # Saltar la primera fila (encabezados)

        for row in csv_reader:
            # Leer datos y almacenar en listas respectivas
            materia.append(row[0])
            primerDia.append(row[1])
            sdoDia.append(row[2])
            inicioClase.append(row[3])
            finClase.append(row[4])
            seEntenido.append(row[5])

# Definir función para calcular estadísticas
def sacar_stats():
    # Inicializar contadores para diferentes variables
    n = 0
    n1, n2, n3, n4, n5, n6,n7,n8,n9,n10,n11,n12 = 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0

    # Estadísticas para la variable 'materia'
    for i in materia:
        if i == 'Inteligencia de Negocios' and seEntenido[n] == 'si':
            n1 += 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and seEntenido[n] == 'si':
            n2 += 1
        if i == 'Topico I' and seEntenido[n] == 'si':
            n3 += 1
        if i == 'Administración de proyectos de software' and seEntenido[n] == 'si':
            n4 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and seEntenido[n] == 'si':
            n5 += 1
        if i == 'Ingles VI' and seEntenido[n] == 'si':
            n6+=1
        if i == 'Inteligencia de Negocios' and seEntenido[n] == 'no':
            n7+= 1
        if i == 'Sistemas Inmersos y de realidad aumentada' and seEntenido[n] == 'no':
            n8 += 1
        if i == 'Topico I' and seEntenido[n] == 'no':
            n9 += 1
        if i == 'Administración de proyectos de software' and seEntenido[n] == 'no':
            n10 += 1
        if i == 'Pruebas y aseguramiento de la calidad de software' and seEntenido[n] == 'no':
            n11 += 1
        if i == 'Ingles VI' and seEntenido[n] == 'no':
            n12 += 1
        n += 1
    # Almacenar resultados en listaDeValores
    listaDeValores.extend([n1, n2, n3, n4, n5, n6,n7,n8,n9,n10,n11,n12])

    # Estadísticas para la variable 'inicioClase'
    n = 0
    n1, n2 = 0, 0
    for i in inicioClase:
        if (i == '07:00' or i== '8:00' or i == '09:00' or i== '10:00' or i=='11:00') and seEntenido[n] == 'si':
            n1 += 1
        if (i == '07:00' or i== '8:00' or i == '09:00' or i=='10:00' or i=='11:00') and seEntenido[n] == 'no':
            n2 += 1
        n += 1
    listaDeValores.extend([n1, n2])

    # Estadísticas para la variable 'FinClase'
    n = 0
    n1, n2 = 0, 0,
    for i in finClase:
        if (i == '09:00' or i=='10:00' or i == '11:00' or i == '01:00' or i=='02:00') and seEntenido[n] == 'si':
            n1 += 1

        if (i == '09:00' or i=='10:00' or i == '11:00' or i == '01:00' or i=='02:00') and seEntenido[n] == 'no':
            n2 += 1
        n += 1
    listaDeValores.extend([n1, n2])

    # Estadísticas para la variable 'primerDia'
    n = 0
    n1, n2, n3, n4, n5, n6, n7, n8 = 0, 0, 0, 0, 0, 0, 0, 0

    for i in primerDia:
        if i == 'Lunes' and seEntenido[n] == 'si':
            n1 += 1
        if i == 'Martes' and seEntenido[n] == 'si':
            n2 += 1
        if i == 'Miercoles' and seEntenido[n] == 'si':
            n3 += 1
        if i == 'Jueves' and seEntenido[n] == 'si':
            n4 += 1
        if i == 'Lunes' and seEntenido[n] == 'no':
            n5 += 1
        if i == 'Martes' and seEntenido[n] == 'no':
            n6 += 1
        if i == 'Miercoles' and seEntenido[n] == 'no':
            n7 += 1
        if i == 'Jueves' and seEntenido[n] == 'no':
            n8 += 1
        n += 1
    listaDeValores.extend([n1, n2, n3, n4, n5, n6, n7, n8])

    # Estadísticas para la variable 'SegundoDia'
    n = 0
    n1, n2, n3, n4, n5, n6, n7, n8 = 0, 0, 0, 0, 0, 0, 0, 0

    for i in sdoDia:
        if i == 'Lunes' and seEntenido[n] == 'si':
            n1 += 1
        if i == 'Martes' and seEntenido[n] == 'si':
            n2 += 1
        if i == 'Miercoles' and seEntenido[n] == 'si':
            n3 += 1
        if i == 'Jueves' and seEntenido[n] == 'si':
            n4 += 1
        if i == 'Lunes' and seEntenido[n] == 'no':
            n5 += 1
        if i == 'Martes' and seEntenido[n] == 'no':
            n6 += 1
        if i == 'Miercoles' and seEntenido[n] == 'no':
            n7 += 1
        if i == 'Jueves' and seEntenido[n] == 'no':
            n8 += 1
        n += 1
    listaDeValores.extend([n1, n2, n3, n4, n5, n6, n7, n8])

    # Estadísticas para la variable 'seEntendio'
    n = 0
    n1, n2 = 0, 0
    for i in materia:
        if seEntenido[n] == 'si':
            n1 += 1
        if seEntenido[n] == 'no':
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
    a = input("Selecciona la materia: 1: Inteligencia de Negocios, 2: Sistemas Inmersos y de Realidad Aumentada, 3: Topico I, 4: Administración de Proyectos de Software, 5: Pruebas y Aseguramiento de la Calidad de Software, 6: Ingles VI. ")
    b = input(
        "Selecciona el dia que quieras ver: 1: Lunes, 2: Martes, 3: Miercoles, 4: Jueves. " )

    c = input( "Selecciona el horario de la clase: 1: 7:00-9:00 , 2: 7:00-10:00 , 3: 8:00-11:00, 4: 08:00-11:00, 5: 8:00-01:00, 6: 09:00-10:00, 7: 09:00-11:00, 8: 09:00-1:00, 9: 10:00-11:00, 10: 10:00-12:00, 11: 11:00-01:00, 12: 11:00-02:00. ")

   # Llamar a la función 'Calcular' con los datos ingresados por el usuario
    Calcular(a, b, c, si, no)

# Definir función para calcular probabilidades
def Calcular(n1, n2, n3, n4, n5, sis, non):
    datos_si, datos_no = sis, non
    global listaDeValores, datos_totales

    # Inicializar variables para probabilidades
    si, no = 0, 0
    suma = 0
    p_si, p_no = 0, 0

    # Calcular probabilidades para la variable 'materia'
    if n1 == "1":
        prob_si = listaDeValores[0] / datos_totales
        prob_no = listaDeValores[6] / datos_totales
    if n1 == "2":
        prob_si = listaDeValores[1] / datos_totales
        prob_no = listaDeValores[7] / datos_totales
    if n1 == "3":
        prob_si = listaDeValores[2] / datos_totales
        prob_no = listaDeValores[8] / datos_totales
    if n1 == "4":
        prob_si = listaDeValores[3] / datos_totales
        prob_no = listaDeValores[9] / datos_totales
    if n1 == "5":
        prob_si = listaDeValores[4] / datos_totales
        prob_no = listaDeValores[10] / datos_totales
    if n1 == "6":
        prob_si = listaDeValores[5] / datos_totales
        prob_no = listaDeValores[11] / datos_totales

    # Calcular probabilidades para la variable 'primerDia y sdodia'
    if n2 == "1":
        prob_si *= listaDeValores[12] / datos_totales
        prob_no *= listaDeValores[20] / datos_totales
    if n2 == "2":
        prob_si *= listaDeValores[13] / datos_totales
        prob_no *= listaDeValores[21] / datos_totales
    if n2 == "3":
        prob_si *= listaDeValores[14] / datos_totales
        prob_no *= listaDeValores[22] / datos_totales
    if n2 == "4":
        prob_si *= listaDeValores[15] / datos_totales
        prob_no *= listaDeValores[23] / datos_totales

 # Calcular probabilidades para la variable 'inicioClase y finClase'
    if n3 == "1":
        prob_si *= listaDeValores[38] / datos_totales
        prob_no *= listaDeValores[39] / datos_totales
    if n3 == "2":
        prob_si *= listaDeValores[40] / datos_totales
        prob_no *= listaDeValores[41] / datos_totales
    if n3 == "3":
        prob_si *= listaDeValores[42] / datos_totales
        prob_no *= listaDeValores[43] / datos_totales
    if n3 == "4":
        prob_si *= listaDeValores[44] / datos_totales
        prob_no *= listaDeValores[45] / datos_totales
    if n3 == "5":
        prob_si *= listaDeValores[46] / datos_totales
        prob_no *= listaDeValores[47] / datos_totales
    if n3 == "6":
        prob_si *= listaDeValores[48] / datos_totales
        prob_no *= listaDeValores[49] / datos_totales
    if n3 == "7":
        prob_si *= listaDeValores[50] / datos_totales
        prob_no *= listaDeValores[51] / datos_totales
    if n3 == "8":
        prob_si *= listaDeValores[52] / datos_totales
        prob_no *= listaDeValores[53] / datos_totales
    if n3 == "9":
        prob_si *= listaDeValores[54] / datos_totales
        prob_no *= listaDeValores[55] / datos_totales
    if n3 == "10":
        prob_si *= listaDeValores[56] / datos_totales
        prob_no *= listaDeValores[57] / datos_totales
    if n3 == "11":
        prob_si *= listaDeValores[58] / datos_totales
        prob_no *= listaDeValores[59] / datos_totales
    if n3 == "12":
        prob_si *= listaDeValores[60] / datos_totales
        prob_no *= listaDeValores[61] / datos_totales

    # Calcular probabilidades finales
    si *= 0.5
    no *= 0.5
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
    print("Si tiene mas de 50% se aprendio lo suficientes, en caso de que sea menor a 50% no aprendio lo suficiente.")
    print("Probabilidad de los que entendieron: ", round(p_si, 2))
    print("Probabilidad de los que no entendieron: ", round(p_no, 2))


# Leer datos del archivo CSV

leer_datos()

# Calcular estadísticas
sacar_stats()








































