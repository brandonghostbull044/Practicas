titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'

#Para buscar un string dentro de otro string hacemos uso del método count, el cual recibe como argumento el string que queremos buscar dentro del otro string. Este método retornará la cantidad de coincidencias que encuentre en el string que estamos buscando

contador = titulo_curso.count('Python')
print(contador)

#Otra manera de validar si existe es con la palabra reservada in. ESta palabra retornará un valor booleano. Por defecto el uso de mayúculas y minúsculas sí importa, para insensibilizar el uso de mayúsculas y minúculas usamos el método .lower()
print('python' in titulo_curso)
print('python' in titulo_curso.lower())

#También podemos validar si una palabra no existe en un string con las palabras reservadas not in 
print('Python' not in titulo_curso.lower())

#Podemos validar si un string se encuentra al principio o al final de otro string con las palabras reservadas startswith y endswith
print(titulo_curso.startswith('Curso'))
print(titulo_curso.endswith('Curso'))