#Josué Amílcar López Benítez SMIS935820

import sqlite3 #Importando Librería de SQL Lite

#Creación de la Base de Datos para el control de vacunas
conexion = sqlite3.connect("ControlVacunas.db") #Abre la conexión con BD

#Creación de la tabla "vacunas"...
try:
    #No se permiten campos nulos para evitar errores de inconsistencias
    conexion.execute("""CREATE TABLE vacunas (
    id_persona integer primary key autoincrement NOT NULL,
    nombre text NOT NULL,
    apellido text NOT NULL,
    edad integer NOT NULL,
    sexo text NOT NULL,
    telefono text NOT NULL,
    direccion text NOT NULL,
    vacunas integer NOT NULL
    )""")

    print("Se creo la tabla vacunas") #Se creo la tabla en la BD
    print("-------------------------------------------------------\n")
 
except sqlite3.OperationalError:
    print("La tabla vacunas ya existe") #No se creo la Tabla en la BD
    print("-------------------------------------------------------\n")



#Ingreso de los diez registros en la tabla vacunas...
#El campo id_persona lo hemos asignado como clave primaria y autoincrementable
#por lo tanto no lo definimos en los ingresos de los datos 

#Registro -| 01 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Rosa', 'Calix', 19, 'Mujer', '24877689', 'San Miguel,San Miguel', 1)")

#Registro -| 02 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Dayana', 'Vasquez', 19, 'Mujer', '7548-1963', 'Guatajiagua,Morazan', 2)")

#Registro -| 03 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Mariana', 'Campos', 19, 'Mujer', '6451-2376', 'Guatajiagua,Morazan', 2)")

#Registro -| 04 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Amilcar', 'Lopez', 19, 'Hombre', '7344-0004', 'Guatajiagua,Morazan', 1)")

#Registro -| 05 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Jaquelin', 'Bonilla', 19, 'Mujer', '4516-2389', 'San Francisco Gotera,Morazan', 1)")

#Registro -| 06 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Andres', 'Morales', 20, 'Hombre', '245-61791', 'San Simon,Morazan', 2)")

#Registro -| 07 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Yosselin', 'Tolentino', 21, 'Mujer', '4978-5721', 'San Salvador,San Salvador', 2)")

#Registro -| 08 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Cristobal', 'Torres', 20, 'Hombre', '2309-9146', 'San Francisco Gotera,Morazan', 1)")

#Registro -| 09 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Alexander', 'Martinez', 22, 'Hombre', '7542-2018', 'Guatajiagua,Morazan', 2)")

#Registro -| 10 |-
conexion.execute("INSERT INTO vacunas(nombre, apellido, edad, sexo, telefono, direccion, vacunas) \
                VALUES ('Karla', 'Guzman', 19, 'Mujer', '3224-5671', 'Guatajiagua,Morazan', 1)")


conexion.commit() #Confirmando el ingreso de los datos...



#Consultando datos
lista = conexion.execute("select id_persona, nombre, apellido, edad, sexo, telefono, direccion, vacunas from vacunas ORDER BY id_persona ASC")

for row in lista:
    print("ID_Persona = ", row[0])
    print("Nombre = ", row[1])
    print("Apellido = ", row[2])
    print("Edad = ", row[3])
    print("Sexo = ", row[4])
    print("Telefono = ", row[5])
    print("Dirección = ", row[6])
    print("Vacunas = ", row[7])
    print("-------------------------------------------------------\n")


conexion.close() #Cerrando conexión a la Base de Datos




