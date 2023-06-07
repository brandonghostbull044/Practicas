lista_cursos = ['Python', 'Java', 'Django', 'Ruby', 'Laravel', 'C#']
print(len(lista_cursos))
lista_cursos2 = ['C', 'C++', 'Angular', 'React']

#Añadir elemento al final de la lista
lista_cursos.append('MongoDB')

print(lista_cursos)
print(len(lista_cursos))

#Añadir elemento en un idnice específico
lista_cursos.insert(2, 'JavaScript')
print(lista_cursos)
print(len(lista_cursos))

#Podemos extender una lista con otra lista
lista_cursos.extend(lista_cursos2)
print(lista_cursos)
print(len(lista_cursos))


#Podemos eliminar elementos de las listas
lista_cursos.remove('MongoDB')
print(lista_cursos)
print(len(lista_cursos))

del lista_cursos[0]
print(lista_cursos)
print(len(lista_cursos))

#Podemos eliminar todos los elementos de una lista
lista_cursos.clear()
print(lista_cursos)
print(len(lista_cursos))
