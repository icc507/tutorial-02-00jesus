#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]

def arbolTrinario(numero):
    return [numero, [], [], []]

def insertaEnArbolTrinario(arbol, numero):
    if arbol == []:
        arbol += arbolTrinario(numero)
    elif numero == arbol[0]:
        arbol[2].append(numero)
    elif numero <= arbol[0]:
        if arbol[1] == []:
            arbol[1] = arbolTrinario(numero)
        else:
            insertaEnArbolTrinario(arbol[1], numero)
    else:
        if arbol[3] == []:
            arbol[3] = arbolTrinario(numero)
        else:
            insertaEnArbolTrinario(arbol[3], numero)


arbol = []

teclado = (input().split())

for numero in teclado:
    insertaEnArbolTrinario(arbol, int(numero))

print(arbol)
