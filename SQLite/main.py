import sqlite3

conn = sqlite3.connect("Miaplicacion.db")

conn.execute('''CREATE TABLE Alumnos(id INTEGER PRIMARY KEY, Nombre TEXT NOT NULL, Apellido TEXT NOT NULL)''')

conn.execute("INSERT INTO Alumnos(id,Nombre,Apellido)VALUES (1,'Frank','Mora') ")
conn.execute("INSERT INTO Alumnos(id,Nombre,Apellido)VALUES (2,'Jose','rojas') ")
conn.execute("INSERT INTO Alumnos(id,Nombre,Apellido)VALUES (3,'Abner','rodriguez') ")
conn.execute("INSERT INTO Alumnos(id,Nombre,Apellido)VALUES (4,'Maria','fonseca') ")
conn.execute("INSERT INTO Alumnos(id,Nombre,Apellido)VALUES (5,'Alejandra','medrano') ")
conn.execute("INSERT INTO Alumnos(id,Nombre,Apellido)VALUES (6,'Julio','Marin') ")
conn.execute("INSERT INTO Alumnos(id,Nombre,Apellido)VALUES (7,'Rachel','monge') ")
conn.execute("INSERT INTO Alumnos(id,Nombre,Apellido)VALUES (8,'Marco','Astua') ")

conn.commit()

consult_nombre= 'Frank'

selector=conn.execute(f"SELECT * FROM Alumnos WHERE Nombre=?",(consult_nombre,))

for row in selector:
     print(f"id:{row[0]},Nombre:{row[1]}, Apellido:{row[2]}")


conn.close()