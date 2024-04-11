#ALUMNO : JAVIER IVAN ALMADA 
#PROGRAMACION PRIMER CUATRIMESTRE
#TURNO DIV 111 TURNO MAÑANA.

"""
UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.
Las posibles aplicaciones son las siguientes:

Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son: 
nombre del empleadoX
edad (no menor a 18)X
género (Masculino - Femenino - Otro)X
tecnologia (IA, RV/RA, IOT)  X
B) Cargar por terminal 10 encuestas.
C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
"""

contador_masc_ia_iot_25a50 = 0 #CONTADOR MASCULINO IA IOT 25 A 50 AÑOS
contador_no_ia = 0 #CONTADOR NO IA
mayor_edad_m = 0 #MAYOR EDAD MASCULINO
nombre_mayor_edad = "" #NOMBRE DEL MAYOR DE EDAD
tec_mayor_edad_masc = "" #TECNOLOGIA DEL MAYOR DE EDAD MASCULINO
no_ia_contador = 0 #CONTADOR NO IA

for _ in range(10):
    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha():
        nombre = input("Ingrese su nombre correctamente: ") #VALIDO NOMBRE CON ISALPHA

    edad = input("Ingrese su edad (mayor de 18): ")
    while not edad.isdigit() or int(edad) < 18: 
        edad = input("Ingrese una edad válida (mayor de 18): ") #VALIDO EDAD Y SOLO NUMEROS

    edad = int(edad) #CONVIERTO EDAD EN ENTERO

    genero = input("Ingrese su género (masculino, femenino u otro): ").lower() #USO LOWER PARA QUE MAYUS Y MINUS SEAN IGUAL
    while genero not in ("masculino", "femenino", "otro"):
        genero = input("Ingrese su género correctamente: ").lower()
    
    tecnologia = input("Ingrese una de estas tres tecnologías (IA, RVRA o IOT): ").upper() #USO UPPER PARA mayusculas
    while tecnologia not in ("IA", "RVRA", "IOT"):
        tecnologia = input("Ingrese una tecnología válida: ").upper()

    if genero == "masculino" and (tecnologia == "IA" or tecnologia == "IOT") and 25 <= edad <= 50: #1er ejercicio
        contador_masc_ia_iot_25a50 += 1

    if tecnologia != "IA" and (genero != "femenino" or 33 <= edad <= 40): #2do ejercicio
        contador_no_ia += 1

    if genero == "masculino" and edad > mayor_edad_m: #3er ejercicio
        mayor_edad_m = edad
        nombre_mayor_edad = nombre
        tec_mayor_edad_masc = tecnologia

no_ia_porcentaje = (contador_no_ia / 10) * 100 #porcentaje

print(f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive: {contador_masc_ia_iot_25a50}")
print(f"Porcentaje de empleados que no votaron por IA, cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40: {no_ia_porcentaje}%")
print(f"Nombre y tecnología de género masculino con mayor edad: {nombre_mayor_edad}, {tec_mayor_edad_masc}")
