# 📚 Guía Completa de Fundamentos de Python

---

## 🔤 1. Entrada, Salida y Caracteres Especiales

| Elemento | Sintaxis Exacta | Regla de Formato / Sangría | Ejemplo Práctico |
| :--- | :--- | :--- | :--- |
| **Imprimir** | `print("texto")` | Va al borde izquierdo. | `print("Hola Mundo")` |
| **Leer teclado** | `variable = input("Texto: ")` | Guarda la respuesta como texto (`string`). | `nombre = input("Tu nombre: ")` |
| **Convertir a entero** | `variable = int(input("Texto: "))` | Convierte la entrada a número sin decimales. | `edad = int(input("Tu edad: "))` |
| **Convertir a decimal**| `variable = float(input("Texto: "))` | Convierte la entrada a número con decimales. | `precio = float(input("Costo: "))` |
| **Salto de línea** | `\n` | Va **dentro** de las comillas del texto. | `print("Línea 1\nLínea 2")` |
| **Tabulación (Sangría)**| `\t` | Agrega un espacio grande dentro del texto. | `print("Producto:\t$100")` |

---

## ⚖️ 2. Tomas de Decisión y Operadores Lógicos

> ⚠️ **Regla de Sangría (Indentación):** Todo lo que dependa del `if`, `elif` o `else` debe llevar **4 espacios** a la izquierda.

| Elemento | Sintaxis Exacta | ¿Cuándo se usa? | Ejemplo Práctico |
| :--- | :--- | :--- | :--- |
| **Estructura IF / ELSE** | `if condicion:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`codigo`<br>`else:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`codigo` | Evalúa si una condición es verdadera; si no, ejecuta el `else`. Obligatorio los dos puntos (`:`). | `if edad >= 18:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Adulto")`<br>`else:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Menor")` |
| **Múltiples opciones (ELIF)**| `if ...:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`...`<br>`elif otra_condicion:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`...` | Para evaluar más de dos caminos posibles. | `if edad < 12:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`precio = 50`<br>`elif edad < 60:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`precio = 100` |
| **Operador AND** | `condicion1 and condicion2` | Exige que **ambas** condiciones se cumplan obligatoriamente. | `if edad >= 18 and credencial == "si":` |
| **Operador OR** | `condicion1 or condicion2` | Se cumple si al menos **una** de las condiciones es verdadera. | `if dia == "Sábado" or dia == "Domingo":` |
| **Operador NOT** | `not condicion` | Invierte el valor: convierte algo verdadero en falso o viceversa. | `if not registrado:` |

---

## 🔄 3. Ciclos y Bucles

> ⚠️ **Regla de Sangría (Indentación):** Todo el código que se repita dentro del bucle debe llevar **4 espacios** a la izquierda.

| Elemento | Sintaxis Exacta | ¿Cuándo se usa? | Ejemplo Práctico |
| :--- | :--- | :--- | :--- |
| **Ciclo Indefinido** | `while condicion:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`codigo` | Se ejecuta **mientras** la condición sea verdadera. Se usa en menús. | `while activo == True:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`opcion = input("1.Salir")` |
| **Ciclo Finito** | `for i in range(limite):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`codigo` | Se repite una cantidad **exacta** y conocida de veces. | `for i in range(5):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Turno", i)` |
| **Romper Ciclo** | `break` | Detiene y **sale inmediatamente** del ciclo actual. | `if opcion == "salir":`<br>&nbsp;&nbsp;&nbsp;&nbsp;`break` |
| **Saltar Turno** | `continue` | Salta el resto del código actual y **pasa al siguiente turno**. | `if edad < 3:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`continue` |

---

## 🔢 4. Conversiones de Base Numérica

| Elemento | Sintaxis Exacta | Resultado / Formato | Ejemplo en Python |
| :--- | :--- | :--- | :--- |
| **A Binario** | `bin(numero)` | Devuelve texto con prefijo `0b`. | `bin(10)` $\rightarrow$ `'0b1010'` |
| **A Octal** | `oct(numero)` | Devuelve texto con prefijo `0o`. | `oct(10)` $\rightarrow$ `'0o12'` |
| **A Hexadecimal** | `hex(numero)` | Devuelve texto con prefijo `0x`. | `hex(255)` $\rightarrow$ `'0xff'` |
