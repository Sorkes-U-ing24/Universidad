#Cesar Gonzalez Ochoa
# 27/08/2026

# Avance proyecto Semana 3

# Variables que define el consultador

opcion_menu=0

Precio_diesel=0

#Ruta 1: Toluca-Queretaro ida y regreso
distancia1=440
flete1=14000
viaje1=1
sueldo_chofer1=  1500

#Ruta 2: Toluca-Oaxaca ida y regreso
distancia2=900
flete2=36000
viaje2=2
sueldo_chofer2=3500

#Ruta 3: Toluca-Huatulco ida y regreso
distancia3=1500
flete3=42000
viaje3=3
sueldo_chofer3=6000

#Rendimiento del camion
recorrido=3.5
viaticos=750

#Extras
rentabilidad1=0
rentabilidad2=0
rentabilidad3=0
ganancia1=0
ganancia2=0
ganancia3=0

# Codigo
while True:
     while True:
        opcion_menu=int(input(" Que ruta vas a realizar? (\n1.Queretaro,\n2.Oaxaca,\n3.Huatulco)\n   "))
        if opcion_menu >=4 or opcion_menu <=0:
           print("Ruta no valida, ingrese una ruta correcta\n ")
        else:   
    
           break  
     Precio_diesel=float(input("A como esta el diesel el dia de hoy?\n "))
        
     if opcion_menu==1:
      distancia_viaje1=(distancia1/recorrido)
      gasto_diesel1=distancia_viaje1*Precio_diesel
      gasto_chofer1=viaticos*viaje1
      ganancia1=flete1-gasto_diesel1-(gasto_chofer1+sueldo_chofer1)
      rentabilidad1=(ganancia1/flete1)*100
      if rentabilidad1>=50:
          print("\nRuta con excelente margen\n")
      elif rentabilidad1>=40:
          print("\nRuta con margen moderado\n")
      elif rentabilidad1>=35:
          print("\nRuta con margen bajo\n")    
      print(f"La ganancia de esta ruta es: ${ganancia1:.2f} de {flete1} \n")
        
     elif opcion_menu==2:
      distancia_viaje2=(distancia2/recorrido)
      gasto_diesel2=distancia_viaje2*Precio_diesel
      gasto_chofer2=viaticos*viaje2
      ganancia2=flete2-gasto_diesel2-(gasto_chofer2+sueldo_chofer2)
      rentabilidad2=(ganancia2/flete2)*100
      if rentabilidad2>=50:
          print("\nRuta con excelente margen\n")
      elif rentabilidad2>=40:
          print("\nRuta con margen moderado\n")
      elif rentabilidad2>=35:
          print("\nRuta con margen bajo\n") 
      print(f"\nLa ganancia de esta ruta es: {ganancia2:.2f} de {flete2}\n")
          
     elif opcion_menu==3:   
      distancia_viaje3=(distancia3/recorrido)
      gasto_diesel3=distancia_viaje3*Precio_diesel
      gasto_chofer3=viaticos*viaje3
      ganancia3=flete3-gasto_diesel3-(gasto_chofer3+sueldo_chofer3)
      rentabilidad3=(ganancia3/flete3)*100
      if rentabilidad3>=50:
          print("\nRuta con excelente margen\n")
      elif rentabilidad3>=40:
          print("\nRuta con margen moderado\n")
      elif rentabilidad3>=35:
          print("\nRuta con margen bajo\n") 
      print(f"\nLa ganancia de esta ruta es: {ganancia3:.2f} de {flete3}\n")
     continuacion=input("\nQuiere realizar otra cotizacion?\nPresiona Enter para continuar.\nReesponde NO, para cerrar el programa\n").upper()
     if continuacion=="NO":
        break
Comparacion=input("\nQuieres comparar la rentabilidad de las rutas?\n").upper()
if Comparacion=="SI":
    if rentabilidad1>rentabilidad2 and rentabilidad1>rentabilidad3:
        print("\n El que tiene un mayor margen es la Ruta Toluca-Queretaro\n " )
    elif rentabilidad2>rentabilidad1 and rentabilidad2>rentabilidad3:
        print(" \n El que tiene mayor margen es la Ruta Toluca-Oaxaca\n")
    elif rentabilidad3>rentabilidad1 and rentabilidad3>rentabilidad2:
        print("\n El que tiene mayor margen es la Ruta Toluca-Huatulco\n")
elif Comparacion=="NO":
    print("")
