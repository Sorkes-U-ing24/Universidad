# Cesar Gonzalez Ochoa
# Al07322002
# 20/08/2026
# # Paso 1. Pedir numero de visitantes
PRECIO_MENOR=30
PRECIO_MAYOR=45
DESCUENTO_ADULTO_MAYOR=0.12
DESCUENTO_ESTUDIANTE=0.10
DESCUENTO_PROFESOR=0.10
COBRO_TOTAL= 0
while True: 
    visitantes=int(input("Cuantas personas van a entar?"))
    if visitantes <=0:
        print("Invalido, repetir.")
    else:   
        break   
    # paso 2. proceso de visitantes
for i in range(visitantes):
    while True:     
        edad=int(input("que edad tiene?"))    
        if edad<0:
            print("error, repetir")
            continue 
        break
    if edad<3:
        precio_base = 0
        print("Es menor, no paga")
        continue
    elif edad <=17:
        precio_base = PRECIO_MENOR
        print("menor de edad, paga 30")
    else    :
        precio_base = PRECIO_MAYOR
        print("mayor de edad, paga 45")

    rol = input(" tienes algun rol?(estuadiante / profesor / adulto mayor/ ninguno)")
    if precio_base >0:
        if rol == "adulto mayor":
            descuento = DESCUENTO_ADULTO_MAYOR
        elif rol == "estudiante":
            descuento = DESCUENTO_ESTUDIANTE
        elif  rol == "profesor":
            descuento = DESCUENTO_PROFESOR
        else:
            descuento = 0
        precio_final = precio_base-(precio_base*descuento)
        COBRO_TOTAL+=precio_final
        print(f"va a pagar: ${precio_final}")
    print (f"total:${COBRO_TOTAL}")
        

        