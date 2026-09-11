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

#excepciones
def excepciones():
    

    try:
        num_excepcion1=int(input("ingresa un numero "))
        num_excepcion2=int(input("ingresa un numero ")) 
        suma_excepcion=num_excepcion1+num_excepcion2
        division_excepcion=num_excepcion1/num_excepcion2
        print(f"suma es {suma_excepcion}")
        print(f"la division es {division_excepcion} ")
    except ValueError:
        print("ingresa un valor numerico ")
    except ZeroDivisionError:
        print("no puedes ingresar el valor 0 ")

#strings
def strings():
    mensaje=" maldito codigo castroso "

    print(f"longitud del mensaje{len(mensaje)}")

    mensaje_nuevo=mensaje.upper()

    print(f" mensaje en mayusculas {mensaje_nuevo}")

    mensaje_modificado= mensaje_nuevo.replace("MALDITO", "BENDITO").replace("CASTROSO", "RECONFORTANTE")

    print(f"mensaje modificado {mensaje_modificado}")

    def conteo(mensajito):
        palabras= mensajito.split()
        return len(palabras)

    mensajito=input("ingresa un nuevo mensaje ")

    palabras_totales=conteo(mensajito)

    print(f"cantidad de palabras que contiene el nuevo mensaje {palabras_totales}")

    
