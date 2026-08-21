Algoritmo UsoPlataformasDigitales
	// 1. Declaración de variables
	Definir nombre Como Cadena
	Definir p1, p2, p3, p4, p5 Como Real
	Definir total_horas, porcentaje Como Real
	// 2. Entrada de datos
	Escribir 'Ingresa tu nombre:'
	Leer nombre
	Escribir 'Horas en Redes Sociales:'
	Leer p1
	Escribir 'Horas en Mensajería:'
	Leer p2
	Escribir 'Horas en Streaming/Series:'
	Leer p3
	Escribir 'Horas en Videos (YouTube/TikTok):'
	Leer p4
	Escribir 'Horas en Videojuegos:'
	Leer p5
	// 3. Procesamiento / Cálculos
	total_horas <- p1+p2+p3+p4+p5
	porcentaje <- (total_horas/24)*100
	// 4. Salida de resultados
	Escribir '-----------------------------------'
	Escribir 'Usuario: ', nombre
	Escribir 'Tiempo total invertido: ', total_horas, ' horas.'
	Escribir 'Porcentaje del dia utilizado: ', porcentaje, '%'
	Escribir '-----------------------------------'
FinAlgoritmo
