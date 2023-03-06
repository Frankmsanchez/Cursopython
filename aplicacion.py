from functools import reduce

lista=[1,2,3,4,5,6,7,8,9,10,11,12]

def sum_add_elementos(Lst):
   add_numeros = list(filter(lambda x: x % 2 !=0 ,Lst))
   suman_add = reduce(lambda x,y: x+y,add_numeros)
   return suman_add

resultado = sum_add_elementos(lista)
print(resultado) 

