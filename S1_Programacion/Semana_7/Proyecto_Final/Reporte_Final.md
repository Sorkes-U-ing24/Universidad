# REPORTE ACADÉMICO FINAL: SISTEMA INTEGRAL DE AUTOMATIZACIÓN DE COSTOS Y GANANCIA NETA EN LOGÍSTICA DE TRANSPORTE (FASE II)

* **Materia:** Fundamentos de Programación / Programación Estructurada
* **Fecha de Entrega:** 25 de septiembre de 2026
* **Estudiante / Desarrollador:** César González Ochoa
* **Entorno de Aplicación:** Transportes Peralta (Operación exclusiva para Waldo's)

---

## 1. INTRODUCCIÓN Y PROBLEMÁTICA DE NEGOCIO

El presente proyecto surge de una necesidad operativa real dentro de **Transportes Peralta**, microempresa dedicada al transporte de carga terrestre donde me desempeño activamente, cubriendo rutas de distribución para la cadena de tiendas **Waldo's**.

Dentro de las actividades diarias, la responsabilidad de calcular las tarifas a cobrar, estimar el consumo de diésel, determinar los sueldos de los operadores y proyectar la ganancia neta de cada flete recae directamente en mi persona. Históricamente, estas estimaciones se realizaban de forma manual, lo que representaba un proceso lento, ineficiente y susceptible a errores de cálculo en momentos de alta carga de trabajo.

### Solución y Alcance
Para resolver esta problemática, diseñé un prototipo funcional de software estructurado que estandariza y automatiza todas las reglas financieras de la empresa. Aunque el presente documento constituye una entrega académica de evaluación, el sistema se construyó con un nivel de solidez operativo (*"anti-fallas"*) pensado para ser implementado formalmente en Transportes Peralta en el mediano plazo, agilizando la toma de decisiones al momento de despachar fletes.

---

## 2. REGLAS DE NEGOCIO Y MODELO MATEMÁTICO

El sistema realiza el cálculo de rentabilidad basándose en las variables reales con las que cotizamos los viajes para Waldo's:

### A. Cobro Total al Cliente
\[\text{Cobro Total} = \text{Tarifa Base Ruta} + \text{Recargo por Rampa}\]

Si la unidad requiere rampa de descarga, se aplica un recargo obligatorio del **25%** sobre la tarifa base de la ruta (0.25 × Tarifa Base). De lo contrario, el recargo es de \$0.00.

### B. Pago al Chofer / Operador
\[\text{Pago Chofer Final} = \text{Pago Base Chofer Ruta} \times \text{Factor Chofer Camión}\]

Ajusta el sueldo base en función de la complejidad de la unidad asignada (factores de 1.05, 1.10, etc.).

### C. Costo de Combustible (Diésel)
\[\text{Rendimiento Ajustado (km/L)} = \frac{2.8 \text{ km/L}}{\text{Factor Diésel Camión}}\]

\[\text{Litros Estimados} = \frac{\text{Kilómetros de la Ruta}}{\text{Rendimiento Ajustado}}\]

\[\text{Costo Diésel Total} = \text{Litros Estimados} \times \text{Precio Diésel por Litro}\]

### D. Costos Operativos Totales y Ganancia Neta
\[\text{Costos Operativos} = \text{Pago Chofer Final} + \text{Costo Diésel Total}\]

\[\text{Ganancia Neta} = \text{Cobro Total Cliente} - \text{Costos Operativos}\]

---

## 3. JUSTIFICACIÓN DE LOS 10 CRITERIOS DE RÚBRICA

* **Identificación y Bienvenida Dinámica:** Solicita credencial en MAYÚSCULAS con límite de 3 intentos de seguridad, registra el nombre del operador e imprime una bienvenida estilizada.
* **Pantalla de Carga:** Muestra una barra de progreso que incrementa su porcentaje hasta el 100% en un máximo de 5 segundos.
* **Menú como Matriz con `while`:** Estructura las opciones del menú en una matriz de dos dimensiones y las despliega mediante ciclos anidados bajo el control de un ciclo principal.
* **Control de Inactividad (10 min con `for`):** Monitorea la inactividad de la consola. Si transcurren 10 minutos sin pulsar teclas, pausa la pantalla y pregunta mediante "sí"/"no" si se desea continuar en la sesión.
* **Captura de Fecha en Tupla:** Sincroniza el año actual automáticamente, valida el día y mes en el calendario y almacena la información estrictamente en una tupla inmutable `(dia, mes, anio)`.
* **Persistencia en Archivos (4+ .txt):** Trabaja con catálogos en texto plano (`Rutas.txt` y `Camiones.txt`) y genera archivos de reporte individuales por viaje y consolidados al cerrar la sesión.
* **Control de Excepciones:** Previene cierres inesperados del programa ante rutas no encontradas, valores no numéricos o archivos vacíos mediante estructuras de control de errores.
* **Depuración Técnica con PDB:** Incluye un modo de auditoría interna para pausar la ejecución en memoria y verificar el comportamiento de los valores calculados.
* **Comentarios de Calidad:** Cuenta con explicaciones claras e informales en cada sección para entender el funcionamiento del programa.
* **Reporte Académico Final:** Documentación del diseño lógico, ecuaciones y evidencias en el presente documento formal.

---

## 4. ESTRUCTURA Y EVIDENCIA DE ARCHIVOS DE TEXTO DE PRUEBA (4+ .txt)

La persistencia del sistema se demuestra mediante la lectura de los catálogos base y la escritura de los reportes generados en disco:

### Archivo Maestro 1: `Rutas.txt` (Catálogo de Destinos Waldo's)
Contiene las distancias en kilómetros, tarifas base al cliente, días de viaje y sueldos base para el chofer.
* **Ejemplo de registro:** `3 | Toluca-Huatulco ida y regreso | 1500 | 42000 | 3 | 6000`

### Archivo Maestro 2: `Camiones.txt` (Flota de Transportes Peralta)
Almacena la configuración de ejes, capacidad de tanque, factores de costo y la presencia de rampa de descarga.
* **Ejemplo de registro:** `ECO01 | C3S2 | 120 | 1.10 | 1.00 | 1 | 0.25`

### Archivo Generado 3: `Reporte_Toluca_Huatulco_ida_y_regreso_C3S2.txt` (Reporte Individual de Viaje)
Documento en texto plano creado automáticamente en la carpeta de reportes al finalizar la simulación de flete:

```text
================================================================================
REPORTE DE COSTOS Y GANANCIA NETA - TRANSPORTE
================================================================================
FECHA DE OPERACIÓN : 25/09/2026
OPERADOR EN TURNO  : Sorkes_18
================================================================================
DETALLES DE LA RUTA:
 - Ruta               : Toluca-Huatulco ida y regreso
 - Distancia Total    : 1500.0 km
 - Días Estimados     : 3 día(s)

DETALLES DEL VEHÍCULO:
 - Unidad             : C3S2
 - Capacidad Tanque   : 120.0 Galones
 - Rampa de Descarga  : SÍ (+25%)

DESGLOSE FINANCIERO:
 + Tarifa Base Ruta   : $42,000.00 MXN
 + Recargo por Rampa  : $10,500.00 MXN
 -------------------------------------------------------------------------------
 = COBRO TOTAL CLIENTE: $52,500.00 MXN

 - Pago al Chofer     : $6,600.00 MXN
 - Consumo Diésel     : 535.71 L ($14,464.29 MXN)
 -------------------------------------------------------------------------------
 = COSTOS OPERATIVOS  : $21,064.29 MXN

================================================================================
GANANCIA NETA FINAL  : $31,435.71 MXN
================================================================================
```

### Archivo Generado 4: `Reporte_Toluca_Puebla_ida_y_regreso_C3S2.txt` (Reporte Individual sin Rampa)
Reporte individual correspondiente a un viaje donde la unidad no requirió el uso de rampa de descarga:

```text
================================================================================
REPORTE DE COSTOS Y GANANCIA NETA - TRANSPORTE
================================================================================
FECHA DE OPERACIÓN : 25/09/2026
OPERADOR EN TURNO  : Sorkes_18
================================================================================
DETALLES DE LA RUTA:
 - Ruta               : Toluca-Puebla ida y regreso
 - Distancia Total    : 360.0 km
 - Días Estimados     : 1 día(s)

DETALLES DEL VEHÍCULO:
 - Unidad             : C3S2
 - Capacidad Tanque   : 200.0 Galones
 - Rampa de Descarga  : NO

DESGLOSE FINANCIERO:
 + Tarifa Base Ruta   : $12,500.00 MXN
 + Recargo por Rampa  : $0.00 MXN
 -------------------------------------------------------------------------------
 = COBRO TOTAL CLIENTE: $12,500.00 MXN

 - Pago al Chofer     : $1,575.00 MXN
 - Consumo Diésel     : 122.14 L ($3,297.86 MXN)
 -------------------------------------------------------------------------------
 = COSTOS OPERATIVOS  : $4,872.86 MXN

================================================================================
GANANCIA NETA FINAL  : $7,627.14 MXN
================================================================================
```

### Archivo Generado 5: `Reporte_Final_Consolidado_Sesion.txt` (Resumen de Turno)
Documento que resume el total de operaciones simuladas y la ganancia acumulada en el turno de trabajo:

```text
================================================================================
REPORTE CONSOLIDADO FINAL DE LA SESIÓN
================================================================================
FECHA DE EMISIÓN  : 25/09/2026
OPERADOR          : César González Ochoa
TOTAL SIMULACIONES: 2
GANANCIA ACUMULADA: $39,062.85 MXN
================================================================================
DETALLE DE OPERACIONES REALIZADAS EN LA SESIÓN:

 [1] Ruta: Toluca-Huatulco ida y regreso  | Camión: C3S2   | Ganancia Neta: $31,435.71 MXN
 [2] Ruta: Toluca-Puebla ida y regreso    | Camión: C3S2   | Ganancia Neta: $7,627.14 MXN

================================================================================
```

---

## 5. DOCUMENTACIÓN DE DEPURACIÓN TÉCNICA CON PDB

* **Fecha de pruebas:** 25 de septiembre de 2026
* **Auditor:** César González Ochoa
* **Módulo auditado:** Función de cálculo financiero y sub-menú de simulación

### Proceso de Inspección
Durante la revisión técnica con la herramienta de depuración de Python (`PDB`), se colocó una pausa en tiempo de ejecución para auditar la precisión de las operaciones en memoria.

* **Verificación de Carga:** Se confirmó mediante la inspección de variables que los diccionarios de entrada traían los kilómetros, precios y factores de camión correctos desde los archivos de texto.

* **Control de Decimales: Se detectó que las operaciones matemáticas arrojaban valores flotantes periódicos (ejemplo: 14464.285714285714). Como corrección, se implementó el formato de dos decimales :,.2f tanto en las impresiones de consola como en la escritura de reportes .txt, manteniendo la cifra limpia ($31,435.71 MXN) sin sacrificar la exactitud interna en la memoria.

* **Resistencia a Errores: Se forzó la asignación de un valor no numérico en las entradas durante el debugger. La falla fue manejada por las estructuras de control del sub-menú, evitando que el programa se cerrara repentinamente o escribiera un archivo dañado en el disco duro.

## 6. CONCLUSIONES
La realización de este proyecto permitió aplicar de forma práctica los conceptos clave de la programación estructurada (ciclos while y for, tuplas inmutables, manejo de archivos y excepciones), solucionando una tarea repetitiva real en Transportes Peralta.

La automatización de las cotizaciones para las rutas de Waldo's optimiza el tiempo de cálculo, elimina los errores humanos en el desglose de costos operativos y proporciona un registro permanente de cada viaje simulado en el turno de trabajo.