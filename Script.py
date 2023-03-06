paises = input ("Ingresa una lista de paises separalos por comas:  ")

lista_paises = [paises.strip() for paises in paises.split(',')]

Paises_uno= set(lista_paises)

paises_sorted = sorted(list(Paises_uno))

print(",".join(paises_sorted))