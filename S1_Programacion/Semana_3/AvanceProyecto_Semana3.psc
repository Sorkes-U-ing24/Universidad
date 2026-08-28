Algoritmo AvanceProyecto_Semana3
	// Variables y constantes iniciales
	opcion_menu <- 0
	Precio_diesel <- 0.0
	distancia1 <- 440
	flete1 <- 14000
	viaje1 <- 1
	sueldo_chofer1 <- 1500
	distancia2 <- 900
	flete2 <- 36000
	viaje2 <- 2
	sueldo_chofer2 <- 3500
	distancia3 <- 1500
	flete3 <- 42000
	viaje3 <- 3
	sueldo_chofer3 <- 6000
	recorrido <- 3.5
	viaticos <- 750
	rentabilidad1 <- 0.0
	rentabilidad2 <- 0.0
	rentabilidad3 <- 0.0
	ganancia1 <- 0.0
	ganancia2 <- 0.0
	ganancia3 <- 0.0
	continuacion <- ''
	Comparacion <- ''
	// Ciclo principal de cotizaciones
	Repetir
		// Ciclo de validación de menú
		Repetir
			Escribir 'Que ruta vas a realizar? (1.Queretaro, 2.Oaxaca, 3.Huatulco)'
			Leer opcion_menu
			Si opcion_menu>=4 O opcion_menu<=0 Entonces
				Escribir 'Ruta no valida, ingrese una ruta correcta'
			FinSi
		Hasta Que opcion_menu>=1 Y opcion_menu<=3
		Escribir 'A como esta el diesel el dia de hoy?'
		Leer Precio_diesel
		Si opcion_menu==1 Entonces
			distancia_viaje1 <- distancia1/recorrido
			gasto_diesel1 <- distancia_viaje1*Precio_diesel
			gasto_chofer1 <- viaticos*viaje1
			ganancia1 <- flete1-gasto_diesel1-(gasto_chofer1+sueldo_chofer1)
			rentabilidad1 <- (ganancia1/flete1)*100
			Si rentabilidad1>=50 Entonces
				Escribir 'Ruta con excelente margen'
			SiNo
				Si rentabilidad1>=40 Entonces
					Escribir 'Ruta con margen moderado'
				SiNo
					Si rentabilidad1>=35 Entonces
						Escribir 'Ruta con margen bajo'
					FinSi
				FinSi
			FinSi
			Escribir 'La ganancia de esta ruta es: $', ganancia1, ' de ', flete1
		SiNo
			Si opcion_menu==2 Entonces
				distancia_viaje2 <- distancia2/recorrido
				gasto_diesel2 <- distancia_viaje2*Precio_diesel
				gasto_chofer2 <- viaticos*viaje2
				ganancia2 <- flete2-gasto_diesel2-(gasto_chofer2+sueldo_chofer2)
				rentabilidad2 <- (ganancia2/flete2)*100
				Si rentabilidad2>=50 Entonces
					Escribir 'Ruta con excelente margen'
				SiNo
					Si rentabilidad2>=40 Entonces
						Escribir 'Ruta con margen moderado'
					SiNo
						Si rentabilidad2>=35 Entonces
							Escribir 'Ruta con margen bajo'
						FinSi
					FinSi
				FinSi
				Escribir 'La ganancia de esta ruta es: ', ganancia2, ' de ', flete2
			SiNo
				Si opcion_menu==3 Entonces
					distancia_viaje3 <- distancia3/recorrido
					gasto_diesel3 <- distancia_viaje3*Precio_diesel
					gasto_chofer3 <- viaticos*viaje3
					ganancia3 <- flete3-gasto_diesel3-(gasto_chofer3+sueldo_chofer3)
					rentabilidad3 <- (ganancia3/flete3)*100
					Si rentabilidad3>=50 Entonces
						Escribir 'Ruta con excelente margen'
					SiNo
						Si rentabilidad3>=40 Entonces
							Escribir 'Ruta con margen moderado'
						SiNo
							Si rentabilidad3>=35 Entonces
								Escribir 'Ruta con margen bajo'
							FinSi
						FinSi
					FinSi
					Escribir 'La ganancia de esta ruta es: ', ganancia3, ' de ', flete3
				FinSi
			FinSi
		FinSi
		Escribir 'Quiere realizar otra cotizacion? (Presiona Enter para continuar, responde NO para cerrar)'
		Leer continuacion
		continuacion <- Mayusculas(continuacion)
	Hasta Que continuacion=='NO'
	// Módulo de comparación
	Escribir 'Quieres comparar la rentabilidad de las rutas? (SI/NO)'
	Leer Comparacion
	Comparacion <- Mayusculas(Comparacion)
	Si Comparacion=='SI' Entonces
		Si rentabilidad1>rentabilidad2 Y rentabilidad1>rentabilidad3 Entonces
			Escribir 'El que tiene un mayor margen es la Ruta Toluca-Queretaro'
		SiNo
			Si rentabilidad2>rentabilidad1 Y rentabilidad2>rentabilidad3 Entonces
				Escribir 'El que tiene mayor margen es la Ruta Toluca-Oaxaca'
			SiNo
				Si rentabilidad3>rentabilidad1 Y rentabilidad3>rentabilidad2 Entonces
					Escribir 'El que tiene mayor margen es la Ruta Toluca-Huatulco'
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
