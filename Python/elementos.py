diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

valor = diccionario['d']
print(valor)

#Haciendo uso de la palabra in podemos conocer si una llave se encuentra dentro del diccionario
print('z' in diccionario)

#Para obtener el valor de los elementos también podemos hacer uso del método get(). Con este método al intentar obtener el valor de una key que no existe no nos devolverá error, simplemente nos devolverá el valor None

valor2 = diccionario.get('a')
print(valor2)
valor3 = diccionario.get('z')
print(valor3)

#Podemos retornar un valor por defecto en caso de que la llave no exista, incluso puede ser un mensaje, separándolo con una coma de la key
valor4 = diccionario.get('y', 7)
print(valor4)

#Haciendo uso del método setdefault() podemos verificar si una key existe y de no existir se crea automáticamente, escribiendo el valor que vamos a añadir después de la key

valor5 = diccionario.setdefault('e', 5)
print(valor5)
print(diccionario)