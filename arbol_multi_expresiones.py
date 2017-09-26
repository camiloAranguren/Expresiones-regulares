import re
import sys
patronVar = re.compile("^[a-z]{1}[a-zA-Z0-9_]*$")
patronSig = re.compile("^[+*/-]{1}$")
patronSig2 = re.compile("^[=]{1}$")
patronNum = re.compile("[0-9]*$")
class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

class Pila:
    def __init__(self):
        self.pila=[]        
    def apilar(self,x):
      # funcion para agregar un elemento a la pila
        self.pila.append(x)
      # print "se apilo correctmente"
    def desapilar(self):
      # funcion para eliminar un elemento de la pila
       if (self.pila != []):
      # print "se desapilo"
        return self.pila.pop()
       else: 
        return "Lista vacia"
    

def evaluar(arbol):
    try:
      if(arbol.valor == '+'):
         return (evaluar(arbol.izq) + evaluar(arbol.der))
      if(arbol.valor == '-'):
         return (evaluar(arbol.izq) - evaluar(arbol.der))
      if(arbol.valor == '*'):
         return (evaluar(arbol.izq) * evaluar(arbol.der))
      if(arbol.valor == '/'):
         return (evaluar(arbol.izq) / evaluar(arbol.der))   
      return int(arbol.valor)
    except AttributeError:
      return int(arbol)

def imprimir(arreglo):
    n = 0
   
    while (n < len(arreglo)):
      print arreglo[n]
      n = n+1

opcion = 1
j = 0
diccionario = []
expresiones = []
while(int(opcion) == 1):
   cadena = raw_input("Ingrese una cadena:")
   lista = cadena.split(" ")
   pila= Pila()
   tam = len(lista)
   i = 0
   while(i < tam):
      if (patronNum.match(lista[i]) == None):
        if(patronSig.match(lista[i])):
           exp = ['operdor',lista[i]]
           expresiones.append(exp)
           der = pila.desapilar()
           izq = pila.desapilar()
           nodo = Nodo(lista[i],izq,der) 
           pila.apilar(nodo)
        elif(patronSig2.match(lista[i])):
           exp = ['operdor',lista[i]]
           expresiones.append(exp)
           x = [lista[i -1], str(evaluar(pila.desapilar()))]
           diccionario.append(x)
           print "el resultado de la expresion es: " + diccionario[j][0] + " = " + diccionario[j][1]
        else:
           if (patronVar.match(lista[i])):
               exp = ['variable',lista[i]]
               expresiones.append(exp)
               n = 0
               while (n < len(diccionario)):
                   if (diccionario[n][0] == lista[i]):
                       pila.apilar(diccionario[n][1])
                   n = n+1
           else: 
                imprimir(expresiones)
                print "el token " + lista[i]+" no es valido"
                sys.exit()
      else:
         exp = ['numero',lista[i]]
         expresiones.append(exp)
         
         pila.apilar(lista[i])
      i = i+1
   j = j+1
   opcion = raw_input("ingrese el 1 si desea agregar una nueva linea o 0 de lo contrario:")

print("proceso terminado")
imprimir(expresiones)




