import pickle

class vehiculo:
    def __init__(self,marca,modelo,color):
        self.marca= marca
        self.modelo=modelo
        self.color=color
        
    def __str__(self):
        return f"Vehículo {self.marca} {self.modelo} del año {self.color}"
        
mi_vehiculo = vehiculo ("toyota","Lancer","Amarillo")

with open('vehiculo.pkl',"wb") as archivo:
    pickle.dump(mi_vehiculo,archivo)

with open('vehiculo.pkl','rb') as archivo:
    vehiculo_cargado = pickle.load(archivo)

print(vehiculo_cargado)