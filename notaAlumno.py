class Alumno:
  def __init__(self,nombre,nota):
   self.nombre = nombre
   self.nota = nota

  def imprimir(self):
    print("Nombre:",self.nombre)
 
  def Nota(self):
     if self.nota >=7:
       print(f"Felicidades has aprobado su nota: {self.nota}")

     else:
        print(f"Lo siento no has aprobado su nota: {self.nota}")


Alumno1 = Alumno('Frank',7)
Alumno1.imprimir()
Alumno1.Nota()