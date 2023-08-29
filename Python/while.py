numero = 123456789
contador = 0
while numero >= 1:
    contador += 1
    numero = numero / 10
    print(f'El contador va en: {contador}')
else:
    print(f'Terminó el contador con {contador} digitos')