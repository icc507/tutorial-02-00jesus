#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
# Lectura de elementos
t = input().split()

inverso = t[::-1]
tupla = tuple(int(indice) if indice.isdigit() else indice for indice in inverso)

print(tupla)

