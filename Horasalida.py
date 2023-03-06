import pprint
import time

HoraActual =time.localtime().tm_hour

if HoraActual >= 19:
    print("Hora de salir")

else:
    horas_restantes = 19 - HoraActual
    minutos_resatntes = (horas_restantes*60)-time.localtime().tm_min
    segundos= (minutos_resatntes*60)-time.localtime().tm_min

print(f"Aun faltan {horas_restantes} horas, {minutos_resatntes} minutos y {segundos} segundos para irnos a casa.")