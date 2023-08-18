mensaje = 'Hola mundo!'
print(mensaje)

#Para alinear string hacemos uso de los siguientes strings. Se añade como argumento un número entero que representa el número de espacios que se agregan

mensaje = mensaje.ljust(5)
print(mensaje, '.')
mensaje = mensaje.rjust(20)
print(mensaje)
mensaje = mensaje.center(40)
print(mensaje)

