#Para declarar un diccionario es necesario hacer uso de las llaves {}. Los valores contenidos no hacen uso del sistema de index, al contrario hacen uso de llaves, las cuales definimos nosotros. Las llaves pueden ser strings, números, tuplas, etc., y su valor va después de unos puntos dobles. También podemos definirlos con la función dict()

#Desde la versión 3.7 de Python los diccionarios respetan el órden de los elemementos de como fueron asignados

diccionario = {"total": 55, "descuento": True, "subtotal": 15 }

diccionari2 = { "total": 55, 10: "Curso de Python", (1,2,3): True }

diccionario3 = dict( total = 55, name = "Brandon" )

#Los diccionarios son modificables y pueden ser reasignados.
diccionario["total"] = 45 
print(diccionario["total"])

#Podemos obtener todas las llaves de nuestro diccionario con el método .keys()
print(diccionario.keys())

#Podemos obtener los valores de los diccionarios con el método .values()
print(diccionario.values())

#Para recorrer todas las keys y sus respectivos valores hacemos uso del método .items()
for key, value in diccionario.items():
    print(key, value)

#Para llamar una key que no existe hacemos uso de la función get()
"""calificaciones = usuario.get('calificaciones', [])
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)"""


#Podemos agregar keys con a los diccionarios de la misma manera que reasignamos valores, haciendo uso de las llaves [], recordando que las keys no se pueden modificar en tiempo de ejecución, sólo sus valores. SI la llave que estamos introduciendo no existe, la crea, si ya existe sólo resigna su valor

elementos = {}
elementos['nombre'] = 'Cody'
elementos[(1,2,3)] = True
print(elementos)

#También podemos conocer la longitud de un diccionario con la función len()

print(len(elementos))

#AL introducir llaves duplicadas con diversos valores, la llave duplicada va a reasignar su valor con el  último asignado y sólo creará una llave.
elementos2 = {'a': 1, 'b': 2, 'c': 3, 'a': 5}
print(elementos2)