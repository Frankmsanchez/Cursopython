from typing import Self


class vehiculo:
    def __init__(self,color,ruedas ,puertas):
     self.color = color
     self.ruedas =ruedas
     self.puertas= puertas
 
class Coche(vehiculo):
    def __init__(self ,color, ruedas, puertas,velocidad,cilindrada):
         super().__init__(color, ruedas, puertas)
         self.velocidad= velocidad
         self.Cilindrada= cilindrada 


cocheprueba = Coche("azul",2,2,140,5000)
print(f"El coche es de color :{cocheprueba.color}, tiene:{cocheprueba.ruedas},{cocheprueba.puertas},puertas , una velocidad de :{cocheprueba.velocidad}Km/h y una cilindrada de :{cocheprueba.Cilindrada}cc ")