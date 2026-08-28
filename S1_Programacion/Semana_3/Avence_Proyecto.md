1. Análisis Organizacional
Empresa / Organización: Autotransportes "Transportes González"

Área de Impacto Operativo: Operaciones y Liquidación de Fletes

Descripción de la Necesidad Operativa:

Actualmente, el cálculo de la ganancia y la rentabilidad por viaje se realiza manualmente deduciendo del pago bruto del flete los viáticos, los sueldos de los choferes y el consumo de diésel. Este proceso manual genera imprecisiones en los montos finales debido a la fluctuación del precio del combustible y la falta de estandarización en los viáticos según el destino. Se requiere un software que agilice, estandarice y garantice la exactitud en el cálculo de costos y la evaluación del margen de ganancia por ruta.

2. Definición del Problema y Reglas de Negocio
Problemática Técnica
Carece de una herramienta que automatice y desglose de forma inmediata los costos operativos que se generan contra el ingreso bruto por viaje, lo que provoca que los cálculos de ganancia se hagan a mano y se pierda tiempo o haya errores al cotizar.

Reglas de Negocio
Base del cálculo: Todo cálculo de ganancia y rentabilidad está basado en el ingreso bruto proporcionado por el flete de la ruta elegida.

Gastos operativos: Los costos a evaluar contra el pago bruto son:

Diésel: Calculado dividiendo la distancia de la ruta entre el rendimiento del camión (3.5 km/l) y multiplicándolo por el precio del diésel del día ingresado por el usuario.

Sueldo del chofer: Monto fijo asignado según la ruta seleccionada.

Viáticos del chofer: Calculados multiplicando la cuota fija diaria ($750) por el número de días/viajes estipulados para la ruta.

Ganancia neta: Se obtiene restando del pago bruto (flete) el gasto total de diésel, los viáticos y el sueldo del chofer.

Rentabilidad porcentual y clasificación: El sistema calcula el porcentaje de ganancia libre sobre el flete ((ganancia / flete) * 100) y muestra un mensaje según el resultado:

50% o más: Ruta con excelente margen.

40% a 49%: Ruta con margen moderado.

35% a 39%: Ruta con margen bajo.

Validación y Comparación: El sistema no permite avanzar si se elige una opción fuera de rango (1 a 3) y al final permite comparar las rentabilidades obtenidas para indicar qué ruta dejó el mayor margen.

3. Listado de Requerimientos Funcionales
Selección de ruta y captura de datos: El sistema debe mostrar un menú interactivo para que el usuario elija la ruta a realizar (Querétaro, Oaxaca o Huatulco), la cual ya tiene asignada su distancia, flete bruto y sueldo del chofer. Además, pedirá ingresar únicamente el precio actual del diésel del día.

Validación de entradas: El programa debe validar que la opción del menú sea correcta (entre 1 y 3). Si se ingresa una opción no válida, debe mostrar un mensaje de error y volver a pedirla.

Cálculo de costos y ganancias: Con base en la distancia de la ruta seleccionada y el rendimiento del camión (3.5 km/l), el sistema debe calcular el consumo de diésel, los viáticos totales según los días del viaje y restarlo al flete para obtener la ganancia neta en dinero.

Evaluación de rentabilidad: El sistema debe calcular el porcentaje de rentabilidad de la ruta ((ganancia / flete) * 100) y mostrar su clasificación cualitativa (excelente margen si es >= 50%, margen moderado si es >= 40% o margen bajo si es >= 35%).

Menú interactivo y repetición: El programa debe permitir al usuario realizar múltiples cotizaciones consecutivas de forma continua hasta que este decida finalizar escribiendo "NO".

Comparación de rutas: Al terminar de cotizar, el sistema debe preguntar al usuario si desea comparar la rentabilidad de las rutas procesadas e imprimir en pantalla cuál de ellas obtuvo el mayor porcentaje de margen.

4. Clasificación de Datos
4.1. Datos de entrada (Solicitados al usuario)
opcion_menu (int / entero): Opción seleccionada por el usuario en el menú interactivo (1 para Querétaro, 2 para Oaxaca, 3 para Huatulco).

Precio_diesel (float / decimal): Precio actual por litro de combustible ingresado en el día ($/L).

continuacion (str / cadena de texto): Respuesta del usuario ("NO" u otra tecla) para decidir si realiza otra cotización o rompe el ciclo.

Comparacion (str / cadena de texto): Respuesta del usuario ("SI" o "NO") para decidir si desea ejecutar el módulo final de comparación.

4.2. Datos de proceso y constantes (Definidos en el sistema o calculados)
distancia1, distancia2, distancia3 (int / entero): Distancia total en kilómetros fijada para cada ruta (440 km, 900 km y 1500 km).

flete1, flete2, flete3 (int / entero): Pago bruto del flete asignado a cada ruta ($14,000, $36,000 y $42,000).

viaje1, viaje2, viaje3 (int / entero): Días/viajes estipulados por ruta para el cálculo de viáticos (1, 2 y 3).

sueldo_chofer1, sueldo_chofer2, sueldo_chofer3 (int / entero): Pago base asignado al operador por ruta ($1,500, $3,500 y $6,000).

recorrido (float / decimal): Rendimiento fijo del camión en kilómetros por litro (3.5 km/l).

viaticos (int / entero): Cuota fija de viáticos por día ($750).

distancia_viaje1, distancia_viaje2, distancia_viaje3 (float / decimal): Litros de diésel requeridos para la ruta (distancia / recorrido).

gasto_diesel1, gasto_diesel2, gasto_diesel3 (float / decimal): Gasto total en combustible (distancia_viaje * Precio_diesel).

gasto_chofer1, gasto_chofer2, gasto_chofer3 (float / decimal): Múltiplo acumulado de viáticos por días de viaje (viaticos * viaje).

4.3. Datos de salida y resultados
ganancia1, ganancia2, ganancia3 (float / decimal): Ganancia neta libre en dinero tras restar del flete el diésel, viáticos y sueldo del chofer.

rentabilidad1, rentabilidad2, rentabilidad3 (float / decimal): Porcentaje de rentabilidad obtenido sobre el flete ((ganancia / flete) * 100).

5. Operadores del Lenguaje y Justificación
5.1. Operadores Aritméticos
División (/):

Se utiliza en dos momentos clave:

Para calcular los litros de diésel requeridos dividiendo la distancia total entre el rendimiento fijo del camión (3.5 km/l).

Para calcular la rentabilidad dividiendo la ganancia entre el flete.

Ejemplo de aplicación:

distancia_viaje1 = (distancia1 / recorrido)
rentabilidad1 = (ganancia1 / flete1) * 100
Multiplicación (*):

Se utiliza para calcular los costos operativos en dinero multiplicando las unidades por sus tarifas o precios.

Ejemplo de aplicación:

gasto_diesel1 = distancia_viaje1 * Precio_diesel
gasto_chofer1 = viaticos * viaje1
Suma (+):

Se aplica para consolidar los viáticos acumulados y el sueldo base del chofer.

Ejemplo de aplicación:

(gasto_chofer1 + sueldo_chofer1)
Resta (-):

Se utiliza para calcular la ganancia neta restándole al pago bruto del flete el costo del diésel y los gastos del chofer.

Ejemplo de aplicación:

ganancia1 = flete1 - gasto_diesel1 - (gasto_chofer1 + sueldo_chofer1)
5.2. Operadores Relacionales
Mayor o igual que (>=) y Menor o igual que (<=):

Se utiliza para validar que la opción elegida en el menú no sea inválida y para evaluar los rangos del porcentaje de rentabilidad (evaluando si es >= 50%, >= 40% o >= 35%).

Ejemplo de aplicación:

if opcion_menu >= 4 or opcion_menu <= 0:
if rentabilidad1 >= 50:
Igualdad (==):

Se utiliza para identificar qué ruta procesar en el if/elif y para verificar si el usuario desea terminar el programa o realizar comparaciones.

Ejemplo de aplicación:

elif opcion_menu == 2:
if continuacion == "NO":
Mayor que (>):

Se aplica en el módulo final para determinar cuál de las tres rutas obtuvo una rentabilidad estrictamente superior a las demás.

Ejemplo de aplicación:

if rentabilidad1 > rentabilidad2 and rentabilidad1 > rentabilidad3:
5.3. Operadores Lógicos
Ó Lógico (or):

Se utiliza en la validación del menú para detectar si el número ingresado por el usuario está fuera del rango permitido (menor/igual a 0 o mayor/igual a 4).

Ejemplo de aplicación:

if opcion_menu >= 4 or opcion_menu <= 0:
Y Lógico (and):

Se utiliza en la comparación final para validar que una ruta sea simultáneamente más rentable que las otras dos.

Ejemplo de aplicación:

elif rentabilidad2 > rentabilidad1 and rentabilidad2 > rentabilidad3:
6. Estructuras de Control y Justificación
6.1. Estructuras Condicionales
Condicional Múltiple (if / elif / else):

Se utiliza en tres momentos del programa:

Selección de ruta: Para ejecutar las fórmulas de cálculo de la ruta elegida (opcion_menu == 1, opcion_menu == 2 u opcion_menu == 3).

Clasificación del margen: Para evaluar el porcentaje de rentabilidad obtenido e imprimir el mensaje correspondiente ("Ruta con excelente margen", "Ruta con margen moderado" o "Ruta con margen bajo").

Comparación final: Para evaluar cuál de las tres rutas tuvo un porcentaje de rentabilidad mayor que las otras dos.

Ejemplo de aplicación:

if rentabilidad1 >= 50:
    print("\nRuta con excelente margen\n")
elif rentabilidad1 >= 40:
    print("\nRuta con margen moderado\n")
elif rentabilidad1 >= 35:
    print("\nRuta con margen bajo\n")
6.2. Estructuras Iterativas / Ciclos
Ciclo Indefinido (while True):

Se usa para controlar el flujo del programa en dos partes:

Ciclo Principal: Mantiene corriendo el programa para hacer varias cotizaciones seguidas hasta que el usuario escriba "NO" para salir.

Ciclo de Validación: Valida que el usuario elija una ruta correcta (del 1 al 3). Si ingresa un número incorrecto, se repite la pregunta hasta que ponga una opción válida y se ejecute el break.

Ejemplo de aplicación:

while True:
    while True:
        opcion_menu = int(input(" Que ruta vas a realizar? (\n1.Queretaro,\n2.Oaxaca,\n3.Huatulco)\n   "))
        if opcion_menu >= 4 or opcion_menu <= 0:
            print("Ruta no valida, ingrese una ruta correcta\n ")
        else:
            break