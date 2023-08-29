#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
# Lectura de las dos tuplas
teclado1 = input().split()
teclado2 = input().split()

tupla1 = []
tupla2 = []
for elemento in teclado1:
    if elemento.isdigit():
        tupla1.append(int(elemento))
    else:
        tupla1.append(elemento)
tupla2 = []
for elemento in teclado2:
    if elemento.isdigit():
        tupla2.append(int(elemento))
    else:
        tupla2.append(elemento)

salida = tuple(tupla2 + tupla1 + tupla2)
print(salida)
