archivo = open("abrir archivos.txt" , "r")

####

lista_nom0 = archivo.readline()        #se recuperan los datos de la primera línea del archivo

lista_nom0 = lista_nom0.rstrip(",")    #se quita la última coma del STRING para poder armar la LISTA
lista_nom0 = lista_nom0.split(",")     #se divide el STRING por comas para que se transforme en LISTA

cambiar0 = " " + lista_nom0[0]         #agrega un espacio al primer elemento de la LISTA para que quede alineado
lista_nom0.remove(lista_nom0[0])       #remueve el primer elemento de la lista
lista_nom0.insert(0 , cambiar0)        #inserta el primer elemento modificado en CAMBIAR0

####

lista_nom1 = archivo.readline()        #lee la segunda linea del archivo

lista_nom1 = lista_nom1.split(",")     #convierte la linea (que es un STRING) en una LISTA

cambiar1 = " " + lista_nom1[0]         #agrega un espacio al primer elemento de la LISTA para que quede alineado
lista_nom1.remove(lista_nom1[0])       #remueve el primer elemento de la lista
lista_nom1.insert(0 , cambiar1)       #inserta el primer elemento modificado en CAMBIAR0    


####

personas = "Personas:"
lugares = "Lugares:"
print("")
print(personas.title(), lugares.title().rjust(50," "))
print("")

for indice in range(0, len(lista_nom0)):                        #obtiene los numerós de INDICE de todos los elementos de LISTA_NOM0
 print(lista_nom0[indice], lista_nom1[indice].rjust(50," "))    #al ejecutar la ITERACIÓN de LISTA_NOM0 en si misma y en LISTA_NOM1
                                                                #se obtienen cada uno de los elementos con el mismo número de INDICE
                                                                #en dos LISTAS diferentes.




















