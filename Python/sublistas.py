lista_cursos = ['Python', 'Java', 'Django', 'Ruby', 'Laravel', 'C#']
#sublista = [startindex:endindex(noinclude)]
sub_lista = lista_cursos[0:3]
sub_lista2 = lista_cursos[2:]
sub_lista3 = lista_cursos[:4]
#Podemos crear listas a partir de saltos entre ellas, agregandso un tercer valor
sub_lista4 = lista_cursos[1:6:2]
#Podemos invertir la lista con el tercer valor
sub_lista5 = lista_cursos[::-1]

print(sub_lista)
print(sub_lista2)
print(sub_lista3)
print(sub_lista4)
print(sub_lista5)