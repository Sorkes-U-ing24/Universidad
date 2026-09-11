#tuplas
def tuplas():
    numeros=(28, 62, 98, 43, 51)
    nuevos_numeros=()

    for i in range (len(numeros)):
        if i==2:
            print(f"tercer elemento {numeros[i]}")
            
            numeros=list(numeros)
    for i in range (2):
        captura_numeros=int(input("ingresa otro numero "))
        nuevos_numeros=nuevos_numeros+(captura_numeros,)

    numeros=tuple(numeros)
    lista_tupla=(nuevos_numeros+numeros)
    lista_hecha=list(lista_tupla)
    lista_ordenada=sorted(lista_tupla)
    tupla_nueva=tuple(lista_ordenada)
    print(f"tupla ordenada {tupla_nueva}")

    def suma_tupla(suma):
        suma_numeros=0
        for i in range(len(suma)):
            suma_numeros+=suma[i]
            return suma_numeros
        
    jojolion=suma_tupla(tupla_nueva)

    print(f"suma de la tupla es: {jojolion}")

#Diccionario
def diccionario():
    
    contactos={
        "paulo": "889-653-424-524",
        "jose": "337-452-781-921",
        "jorge": "332-951-731-545"
    }

    nuevo_nombre = input("Nombre del nuevo contacto: ")
    nuevo_telefono = input("Teléfono del nuevo contacto: ")

    contactos[nuevo_nombre] = nuevo_telefono

    for  clave in contactos:
         print(clave)

    def buscar_telefono(diccionario, contacto):
        return diccionario.get(contacto, "Contacto no encontrado ")

    nombre_a_buscar = input("Nombre a buscar: ")
    telefono_encontrado = buscar_telefono(contactos, nombre_a_buscar)
    print(f"Teléfono de {nombre_a_buscar}: {telefono_encontrado}")


    
