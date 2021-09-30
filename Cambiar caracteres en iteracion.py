lugares = ["Viena", "Managua", "San Salvador de Jujuy", "Bangladesh"]

for l in lugares:
    print(l +" es lindo")

print("")
print(type(lugares[1]))
print("")



conteo = (len(lugares))                             #Cuenta los elementos en la LISTA lugares
print(conteo)                                       #
print(lugares[int(conteo) -1].rstrip("esh"))        #Ubica el ultimo elemento de la lista y le resta uno para obtener su número de INDICE ya que la
                                                    #indización de una Lista comienza contando desde 0
                                                    #con RSTRIP se eliminan los caracteres detallados entre parentesis


print(lugares[int(len(lugares) - 1)].rstrip("esh")) #También puede escribirse así

                                            














