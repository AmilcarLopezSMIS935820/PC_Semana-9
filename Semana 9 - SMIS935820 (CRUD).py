import sqlite3 #Importando Librería de SQL Lite

conexion = sqlite3.connect("ControlVacunas.db") #Abriendo la conexión con BD

#Actualizando un registro
conexion.execute("UPDATE vacunas set nombre='Katerin', apellido='Molina', edad=20, sexo='Mujer', telefono='4591-1268', direccion='San Salvador, San Salvador', vacunas=2 where id_persona=6")

conexion.commit()

#Borrando un registro
conexion.execute("DELETE from vacunas where id_persona=6;")
conexion.commit()

#Cerrando conexión a BD
conexion.close()
