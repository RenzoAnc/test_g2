""""
Practicando
"""
print('Este es un script de práctica')

Cadena1 = 'hoy es Un bonito día. '
Cadena2 = 'es muy Probable que Tengamos una buena Entrevista.'

CadenaT = Cadena1 + Cadena2

print('La cadena original es: ', CadenaT)
a = CadenaT.upper()
print("La cadena aplicando el método 'upper' es: ", a)
b = CadenaT.lower()
print("La cadena aplicando el método 'lower' es: ", b)
c = CadenaT.title()
print("La cadena aplicando el método 'title' es: ", c)
d = CadenaT.capitalize()
print("La cadena aplicando el método 'capitalize' es: ", d)
e = CadenaT.replace('es muy Probable','Aún así, no creo')
print(e)

"La aplicación del método lstrip"
Enunciado = input('Ingrese lo que está pensando con espacios en blanco al inicio y al final: ')

"""
def espaciosblanco_inicio(Cadena):
    x_i = 0
    for elemento in Cadena:
        if elemento == " ":
            x_i += 1
        elif elemento != " ":
            break
    return x_i
"""


def espaciosblanco_inicio_final(Cadena):
    x_i = 0
    x_f = 0
    y = 0
    for elemento in Cadena:
        if elemento == " " and y == 0:
            x_i += 1
        elif elemento != " ":
            y += 1
            pass
        elif elemento == " " and y!= 0:
            x_f += 1
    return x_i, x_f


"Aplicación del método lstrip"

[inicio, final] = espaciosblanco_inicio_final(Enunciado)


print('La cantidad de espacios en blanco al inicio es: ', inicio)
print('La cadena es:',Enunciado)
x = Enunciado.lstrip()
[inicio, final] = espaciosblanco_inicio_final(x)
print('La cantidad de espacios en blanco al inicio despues de aplicar lstrip es: ', inicio)
print('La cadena final es:', x)

"Aplicación del método rstrip"

print('La cantidad de espacios en blanco al final es: ', final)
print('La cadena es:',x)
x_2 = x.rstrip()
[inicio, final] = espaciosblanco_inicio_final(x_2)
print('La cantidad de espacios en blanco al final despues de aplicar rstrip es: ', final)
print('La cadena final es:', x_2)



Archivo1 = open('hola.txt','r')
datos_l = list(Archivo1.read())
datos_s = "".join(datos_l)
print(datos_s)
y = datos_s.split()
print(y)

#Método 1:
print('Hola. Me llamo {} y tengo {} años.'.format('Juan','23'))

#Método 2:
nombre = 'Juan'
edad = '23'
print(f'Hola. Me llamo {nombre} y tengo {edad} años.')

#Método 3:

print(f'Hola. Me llamo {nombre} y tengo {edad} años.'.format(edad='23',nombre = 'Juan'))

#Abriremos el archivo Linux.txt que se encuentra en la carpeta GNU.

Archivo = open('GNU/Linux.txt','r')
Archivo_l = list(Archivo)
Archivo_s = "".join(Archivo_l)
print(type(Archivo_s))
print(Archivo_s)
indice = Archivo_s.find("compuesto")
indice2 = Archivo_s.find("Linux")
print(indice)
print(indice2)

CadenaInicial = 'Hola a todos. Mi nombre es... y estudié en ...'
#Imprimir valores de la cadena dentro de un rango específico.
#Se hará uso del método find.

indice = CadenaInicial.find("Mi")
print(CadenaInicial[indice:len(CadenaInicial):2])
print(indice)














print(Archivo.read())


















Archivo1.close()





Cadena = 'asdasd adsadsad asdasda asdasmmoksadnoamsd'
Cadena2 = Cadena.split()
print(Cadena2)























