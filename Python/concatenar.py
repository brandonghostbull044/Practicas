#LOs strings una vez creados no se pueden modificar. Pero si podemos formar strings a partir de otros strings
nombre = 'Brandon'
apellido = 'León González'

nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

#Otra manera de concatenar strings es con el símbolo % y la letra s: %s
nombre_completo_2 = 'Mr. %s %s %s.' %(nombre, apellido, 'Pérez')
print(nombre_completo_2)

#format. Para este método hacemos uso de placeholders '{}'
nombre_completo_3 = 'Mr. {} {} {} {}.'.format(nombre, apellido, 'Ratón', 'Pérez')
print(nombre_completo_3)

#Con el método format también podemos nombrar los placeholders y hacer uso de parámetros en el método
nombre_completo_4 = 'Mr. {apellido} {nombre} {apodo}'.format(nombre=nombre, apellido=apellido, apodo='GhostBull')
print(nombre_completo_4)

#Los FStrings nos permiten generar nuevos strings a partir de otros utilizando interpolación. Se identifican colocando una f antes del string base

nombre_completo_5 = f'Mr. {nombre} {apellido} {"GhostBull"}'
print(nombre_completo_5)