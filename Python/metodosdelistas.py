lista = [1, 3, 4, 6, 34, 98, 23, 11, 45, 32]
print(lista)

#Podemos ordenar la lista de menor a mayor 
lista.sort()
print(lista)

#Podemos ordenar la lista de mayor a menor
lista.sort(reverse=True)
print(lista)

#Conocer el numero menor
lista.sort()
print(lista[0])

print(min(lista))

#Conocer el numero mayor
lista.sort()
print(lista[-1])

print(max(lista))

#Conocer si un elemento se encuentra o no en la lista
print(6 in lista)
print(10 in lista)
print(6 not in lista)
