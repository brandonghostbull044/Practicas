diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#Podemos conocer las llaver con el método keys(). Es una buena práctica convertir estos resultados en tuplas
print(tuple(diccionario.keys()))

#Podemos conocer los valores de un diccionario con el método values()
print(tuple(diccionario.values()))

#Podemos obtener las keys con sus respectivos valores con el método items()
print(tuple(diccionario.items()))
