viajes = {}       #funciona con el archivo vc.txt

class viajero:
    nombre =""
    lugar = ""
    fecha = ""
    comentarios= ""

def ing_dat():
    global nomviaj
    global viaje
    viaje = viajero()
    viaje.nombre = nomviaj

    print("Usted ingreso el nombre: " + viaje.nombre)
    print("")
    global lugviaj
    lugviaj = input("Ingrese el lugar al que viajó: ")
    print("")

    viaje.lugar = lugviaj

    print("Usted ingreso el lugar: " + viaje.lugar)
    print("")
    global comviaj
    comviaj = input("Ingrese un comentario sobre su experiencia: ")
    print("")

    viaje.comentarios = comviaj

    print("Usted ingreso el comentario: " + viaje.comentarios)
    print("")

def com_cambio():
    global consultacorr
    consultacorr = input("Desea corregir el comentario (ingrese s para SI y n para NO): ")
    print("")

    if consultacorr == "s":
        global corregircom
        corregircom = input("Por favor ingrese su nuevo comentario: ")
        print("")

        global viaje
        viaje.comentarios = corregircom

        print("El texto corregido es: " + viaje.comentarios)
        print("")
        global viajes
        viajes[viaje.nombre] = [viaje.nombre, viaje.lugar, corregircom]

    if consultacorr == "n":
        print(viaje.nombre)                              #muestra el elemento NOMBRE de la CLASE viajero (viaje es un tipo de elemento viajero)
        print("")
        print(viaje.lugar)                               #muestra el elemento LUGAR de la CLASE viajero (viaje es un tipo de elemento viajero)
        print("")
        print(viaje.comentarios)                         #en esta secuencia se mostro en pantalla cada uno de los atributos que componen el OBJETO
        global nomviaj                                   #VIAJE que es de tipo VIAJERO
        global lugviaj
        global comviaj                                                 
        viajes[nomviaj] = [nomviaj, lugviaj, comviaj]    #se agrega una CLAVE (que es el nombre de la persona) al DICCIONARIO VIAJES, junto a 
                                                        #un VALOR que es una lista compuesta por el nombre del LUGAR y el COMENTARIO sobre el mismo.

def guardado():              #### REVISAR EL GUARDADO, AHORA TIENE QUE INCLUIR LISTAS CON LISTAS DENTRO          
    print("")
    print(viajes[nomviaj])      #muestro en pantalla la CLAVE dentro del diccionario VIAJES, que es el nombre de la persona que viajo 
    print("")                   #ingresado en el INPUT NOMVIAJ. Al llamar la CLAVE también muestra los datos (VALORES)
    print(viajes[nomviaj][0])   #como el VALOR de la CLAVE es una lista, llamo al primer elemento de esa lista que es el LUGAR al que viajó
    print("")                   #la persona en cuestion
    print(viajes[nomviaj][1])   
    print("")

    guardar = input("Ingrese el NOMBRE de ARCHIVO con el que desea guardar los datos: ") + ".txt"
    print("")
    print(guardar)
    
    archivo = open(guardar , "a")
    viajestr = (("") + viajes[viaje.nombre][0] + "/" + viajes[viaje.nombre][1] + "/" + viajes[viaje.nombre][2] + "\n" + (""))
    archivo.write(viajestr)
    archivo.close()
    print(viajestr)

        

archivoc = input("Si desea recuperar información anterior sobre viajes ingrese el nombre de archivo: ") + ".txt"
print("")

try:                                      #VERIFICA si el comando que sigue genera un ERROR
    cargar = open(archivoc, "r")          #Abre el archivo para ser manipulado
except:                                   #Genera una excepción que puede ser un mensaje de texto, en este caso se colocó PASS
    pass                                  #para que simplemente pase por alto el ERROR

try:
    lista = cargar.read().splitlines()        #Separa las LINEAS del ARCHIVO de forma que conformen una LISTA
except:
    pass

try:
    for it in range(0 , len(lista)):          #Obtiene el RANGO de la lista (es decir la cantidad de elementos que contiene)
        lista[it] = lista[it].split("/")      #ITERA la lista (recorre sus elementos) para cambiar cada uno de sus ELEMENTOS quitandoles 
        viajes [lista[it][0]] = lista [it]    # el simbolo "/".      
except:                                       #ITERA el PRIMER ELEMENTO (0) de cada una de las LISTAS que integran la LISTA colocandolos
    pass                                      #como CLAVES en el DICCIONARIO VIAJES. También ingresa las LISTAS integrantes de la LISTA
                                              #principal (datos del viajero) como VALORES para las CLAVES. 


presnom = sorted(viajes)                  #convierte las CLAVES del DICCIONARIO en una LISTA ORDENADA de forma ascendente. Escribiendo
                                          # LIST devuelve las CLAVES del DICCIONARIO en LISTA sin ordenar.
for viajeros in presnom:                  #Itera la lista PRESNOM derivada del DICCIONARIO VIAJES mostrando cada una de sus CLAVES
    print(viajeros)
      

#for v, d in viajes.items():              #Itera tanto las CLAVES como los VALORES del DICCIONARIO VIAJES
    #print(v, d)   

#for l in viajes.values():                #Itera los VALORES del DICCIONARIO VIAJES
    #print(l[1])                          #Al consistir los VALORES en LISTAS se puede selección por número de INDICE que elemento de la
                                         #LISTA se desea mostrar   
print("")

nomviaj = input("Ingrese su nombre y apellido: ")
print("")
    
if nomviaj in viajes:
    print("Usted ya ingreso anteriormente datos de un viaje")
    print("")
    for ya_cargados in viajes[nomviaj]:
        print(ya_cargados)
        print("")
    consulta_ioc = input("Si desea ingresar un nuevo viaje ingrese i, si desea cambiar uno existente ingrese c: ") 
    if consulta_ioc == "i":
        ag_list = list(viajes[nomviaj])
        print(ag_list)
        ing_dat()
        nuevo_dest_str = viaje.nombre + "|" + viaje.lugar + "|" + viaje.comentarios
        nuevo_dest_list = nuevo_dest_str.split("|")
        lista_viajes = []
        lista_viajes.append(ag_list)
        lista_viajes.append(nuevo_dest_list)
        print(lista_viajes)
        com_cambio()
        guardado()
else:
    ing_dat()

print("")

com_cambio()

guardado()
  