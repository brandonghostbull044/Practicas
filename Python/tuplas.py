#Las tuplas son inmutables. Se especifican con los paréntesis. Pueden almancenar todo tipo de datos además de listas y otras tuplas. Sirven solo de consulta y la ventaja que tienen sobre las listas es que son más rápidas al momento de obtener valores +.
tupla = ('String', 10, 15.4, True, [1, 2, 3, 4], ['hola mundo', 3])
print(tupla)
#Los indices de los elementos de las tuplas al igual que en las listas comienza en 0
print(tupla[1])
#Al igual que en las listas también podemos crear subtuplas
subtupla = tupla[0::2]
print(subtupla)