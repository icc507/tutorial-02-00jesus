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
def insertarEnArbol(arbol, valor):
	if not arbol:
		return [valor, [], [], []]

	inicialValor, nodoIzquierda, nodoMitad, nodoDerecha = arbol

	if valor == inicialValor:
		nodoMitad.append(valor)
	elif valor < inicialValor:
		nodoIzquierda = insertarEnArbol(nodoIzquierda, valor)
	else:
		nodoDerecha = insertarEnArbol(nodoDerecha, valor)

	return [inicialValor, nodoIzquierda, nodoMitad, nodoDerecha]


def arbolTrinario(numeros):
	root = None
	for numero in numeros:
		if root is None:
			root = [numero, [], [numero], []]
		else:
			root = insertarEnArbol(root, numero)
	return root


def mostrarArbol(arbol):
	return arbol

numeros = list(map(int, input().split()))
arbol = arbolTrinario(numeros)

print(mostrarArbol(arbol))


