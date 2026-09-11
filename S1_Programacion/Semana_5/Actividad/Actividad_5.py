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


    
