"""
a -> Función principal (Decorador)
b -> Función a decorar
c -> Función decorada

a(b) _> c
"""
def funcion_a(funcion_b):
    def funcion_c():
        print('Antes del llamado.')
        funcion_b()
        print('Después del llamado.')

    return funcion_c

@funcion_a
def saludar():
    print('Nos encontramos en una función')

saludar()