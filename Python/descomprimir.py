numeros = (1, 2, 3, 4)

#Podemos asignar valores a múltiples variables a partir de una tupla
uno, dos, tres, cuatro = numeros
#Si nuestro numero de elementos en la tupla supera a nuestro número de variables, podemos asignarle un asterisco a la última para que obtenga los valores restantes
unoo, *resto = numeros
#También podemos omitir el resto de valores con un asterisco y guión bajo
unooo, *_ = numeros
#O podemos omitir algunos intermedios, poniendo después el número de variables que queremos en las que queremos obtener los últimos valores
unoooo, *_, tress, cuatroo = numeros
#Podemos omitir un número específico de intermedios 
print(uno)
print(dos)
print(tres)
print(cuatro)
print(unoo)
print(resto)
print(unooo)
print(unoooo)
print(tress)
print(cuatroo)