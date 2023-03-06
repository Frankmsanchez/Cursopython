with open ('Archivo.txt', 'w') as archivo:
  archivo.write('Hola soy Frank')


with open('archivo.txt','r') as archivo:
    contenido = archivo.read()
    print(contenido)    

archivo.close()