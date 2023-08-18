#Metodos

#split. Genera un lista a partir de un string. Por defecto cada espacio en el string delimita un elemento en la lista. Si queremos delimitar los elementos con algún otro caracter debemos pasar como argumento a la función split el caracter con el que queremos delimitar
lenguajes = 'Python Ruby Java Rust C++ C'
lenguajes_2 = 'Python-Ruby-Java-Rust-C++-C'

listado_lenguajes = lenguajes.split()
print(listado_lenguajes)
listado_lenguajes_2 = lenguajes_2.split('-')
print(listado_lenguajes_2)

#Podemos especificar el número de veces que va a delimitar el string en elementos, dándo.e un segundo valor el cual será el número de veces que queremos delimitar
listado_lenguajes_3 = lenguajes_2.split('-', 2)
print(listado_lenguajes_3)


#join. Genera un string a partir de una lista. El caracter o caracteres que coloquemos dentro del string será con el que separe cada elemento de la lista en el string
lenguajes_list = ['Python', 'Ruby', 'Java', 'Rust', 'C++', 'C']

string_lenguajes = ' '.join(lenguajes_list)
string_lenguajes_2 = '-'.join(lenguajes_list)
print(string_lenguajes)
print(string_lenguajes_2)