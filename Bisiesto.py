print('"Programa que te dice si si es bisiesto o no"')

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

print(es_bisiesto(2020))


print("El programa ha finalizado")