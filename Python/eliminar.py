diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(diccionario)

#Podemos eliminar elementos de los diccionarios con la palabra reservada del, introduciendo la key del elemento que queremos eliminar dentro de las llaves []

del diccionario['a']
print(diccionario)
print(len(diccionario))

#Otra manera de hacerlo es con el método pop()
diccionario.pop('c')
print(diccionario)

#Podemos eliminar todos los elementos de un diccionario con el método clear()
diccionario.clear()
print(diccionario)
