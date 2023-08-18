lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

#Podemos usar la función zip para combinar los valores de una lista y una tupla, podemos combinar las que queramos. Al combinar elementos con un número de valores distintos a los otros, los valores restantes no serán tomado en cuenta en la compresión
resultado = zip(tupla, lista)

#Al descomprimir en tuplamobtenemos subtuplas, y el orden de las agrupaciones dependerá de cual elemento pongamos al principio y cual al final al momento de comprimir
resultado2 = tuple(resultado)

print(resultado)
print(resultado2)