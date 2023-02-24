#primero solictamos el nombre del usuaruio#
Nombre= input("Porfavor intrduzca su Nombre:  ")

peso= float(input(Nombre+" "+"Ingresa tu peso en kg: "))

Altura= float(input(Nombre+" "+"ingrese su altura en metros: "))

union= peso/ (Altura**2)



print("Tu índice de masa corporal es: {:.2f}".format(union))