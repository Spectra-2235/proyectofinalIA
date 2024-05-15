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

