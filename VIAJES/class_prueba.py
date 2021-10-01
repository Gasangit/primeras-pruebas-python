# Con esta prueba intento convertir cada uno de los VALORES de un DICCIONARIO en STRINGS guardables y luego recuperables para volver
# a ensamblar el mencionado DICCIONARIO.


viajes = {
    "Juan Ponce" : [["Juan Ponce", "Madrid", "Una ciudad impresionante"] , ["Juan Ponce", "Livorno", "Gente maravillosa"]] ,
    "Yamila Bogado" : [["Yamila Bogado", "Yellowstone", "Gran riqueza natural"] , ["Yamila Bogado", "Mauritania", "Totalmente exotico y distinto"]] ,
    "Jazmín Navas" : ["Jazmín Navas", "Ciudad del Cabo", "Un lugar totalmente diferente para conocer"] ,
    "Ismael Goitia" : ["Ismael Goitia", "Paramaribo", "Totalmente diferente a todo lo que conocí hasta ahora"]
}


print(viajes["Juan Ponce"][0][0])
print(viajes["Juan Ponce"][0][0][0])    # ESTA LISTA QUE CONTIENE OTRAS DOS, RECIEN LLEGA AL PRIMER CARACTER DEL PRIMER ELEMENTO EN EL
print("")                               # TERCER NIVEL.-

                                        # COMPARACIÓN ENTRE LA "PROFUNDIDAD" DE LA PRIMERA LLAVE Y LA SEGUNDA.

print(viajes["Jazmín Navas"][0][0])     # ENTRANDO DOS NIVELES EN LA LISTA SE LLEGA AL PRIMER CARACTER DEL PRIMER ELEMENTO DE LA LISTA,.
print(viajes["Jazmín Navas"][0][0][0])  # COMO NO HAY UN TERCER NIVEL VUELVE A REPETIR EL PRIMER CARACTER DEL PRIMER ELEMENTO DE LA 
print("")                               # #LISTA.-

for it_vk in viajes:  # ESTA ITERACIÓN TRAE COMO RESULTADO LAS CLAVES DEL DICCIONARIO VIAJES.-
    #print(it_vk)  
    print("")
    if viajes[it_vk][0][0] != viajes[it_vk][0][0][0]:    # COMO UNA LLAVE TIENE LISTAS DENTRO DE UNA LISTA Y LAS OTRAS SOLO UNA LISTA 
                                                         # INDEPENDIENTE, TIENEN DIFERENTE "PROFUNDIDAD".-
        # for cant_list in range(0 , len(viajes[it_vk])):  # ESTO CUENTA LOS ELEMENTOS QUE CONTIENEN LAS LISTAS DE CADA UNA DE LAS LLAVES
            # print(cant_list)
            # print(viajes[it_vk][cant_list])
            print("")
            
            guar_str_0 = "'" + str(viajes[it_vk]) + "'" + "\n"
            
        
            print(guar_str_0)
            print("")

    if viajes[it_vk][0][0] == viajes[it_vk][0][0][0]:
            guar_str = "/".join(viajes[it_vk]) + "\n"
            print(guar_str)
            print("")

arch_nom = input("Ingrese el nombre de archivo con el que quiere guardar los datos: ") + ".txt"
archivo = open(arch_nom, "w")
guard_definitivo = (guar_str_0 + guar_str)
archivo.write(guard_definitivo)