
import os
import sys
import time
import pdb
import threading
from datetime import datetime, date


DIRECTORIO_PROYECTO = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()

RUTA_RUTAS = os.path.join(DIRECTORIO_PROYECTO, "Rutas.txt")
RUTA_CAMIONES = os.path.join(DIRECTORIO_PROYECTO, "Camiones.txt")
REPORTES_DIR = os.path.join(DIRECTORIO_PROYECTO, "reportes_generados")


# A ver, esta función se encarga de leer el archivo de Rutas.txt pero sin que truene.
# Separa las columnas por las barras '|', pasa los datos a números y si hay líneas 
# vacías o textos raros, simplemente los ignora para que no se cierre la app.
def cargar_rutas_blindado():
    rutas = {}
    if not os.path.exists(RUTA_RUTAS) or os.path.getsize(RUTA_RUTAS) == 0:
        return rutas

    try:
        with open(RUTA_RUTAS, 'r', encoding='utf-8') as f:
            for linea in f:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                partes = [p.strip() for p in linea_limpia.split('|')]
                if len(partes) < 6:
                    continue
                
                id_ruta = partes[0]
                rutas[id_ruta] = {
                    "nombre": partes[1],
                    "km": float(partes[2]),
                    "pago_ruta": float(partes[3]),
                    "dias": int(partes[4]),
                    "pago_chofer_base": float(partes[5])
                }
    except Exception as e:
        print(f"[!] Error al procesar Rutas.txt: {e}")
        
    return rutas

# Esta lee el catálogo de Camiones.txt. Checa las banderas de si el camión trae rampa 
# (el '1' o '0') y las vuelve booleanos (True/False) para saber si le cobra el 25% 
# extra al cliente, además de guardar sus factores de costo y diésel.
def cargar_camiones_blindado():
    camiones = {}
    if not os.path.exists(RUTA_CAMIONES) or os.path.getsize(RUTA_CAMIONES) == 0:
        return camiones

    try:
        with open(RUTA_CAMIONES, 'r', encoding='utf-8') as f:
            for linea in f:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                partes = [p.strip() for p in linea_limpia.split('|')]
                if len(partes) < 7:
                    continue
                
                id_camion = partes[0]
                camiones[id_camion] = {
                    "config": partes[1],
                    "tanque_galones": float(partes[2]),
                    "factor_chofer": float(partes[3]),
                    "factor_diesel": float(partes[4]),
                    "tiene_rampa": partes[5] == "1",
                    "recargo_rampa": float(partes[6])
                }
    except Exception as e:
        print(f"[!] Error al procesar Camiones.txt: {e}")
        
    return camiones


CREDENCIALES_AUTORIZADAS = ["ADMINISTRADOR", "GERENTE", "OPERADOR1"]
INTENTOS_MAXIMOS = 3

# Control de acceso anti-pendejos. Checa que la clave esté en MAYÚSCULAS y dentro de
# los roles permitidos. Te da 3 intentos antes de bloquearte y luego te pide tu nombre 
# para saber quién fue el operador que hizo los movimientos en la sesión.
def autenticar_usuario_blindado():
    intentos_restantes = INTENTOS_MAXIMOS
    acceso_concedido = False
    credencial_activa = None
    operador_nombre = None

    print("\n" + "=" * 80)
    print(" SISTEMA DE AUTOMATIZACIÓN DE COSTOS Y GANANCIAS - TRANSPORTE MÉXICO ".center(80, "="))
    print("=" * 80)

    while not acceso_concedido and intentos_restantes > 0:
        print("\nROLES AUTORIZADOS: [ADMINISTRADOR] | [GERENTE] | [OPERADOR1]")
        credencial_input = input("Ingrese Credencial de Acceso (EXACTAMENTE EN MAYÚSCULAS): ").strip().upper()

        if not credencial_input:
            print("[!] Error: No ha ingresado texto. Escriba una credencial válida de la lista.")
            continue

        if credencial_input in CREDENCIALES_AUTORIZADAS:
            acceso_concedido = True
            credencial_activa = credencial_input
            print(f"\n[✓] Credencial [{credencial_activa}] VALIDADA Y ACEPTADA.")
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print(f"[X] Credencial no autorizada. Debe ingresarse en MAYÚSCULAS. Intentos restantes: {intentos_restantes}")
            else:
                print("\n" + "!" * 80)
                print("[!] ACCESO BLOQUEADO POR SEGURIDAD. INTENTOS AGOTADOS.".center(80))
                print("!" * 80 + "\n")
                return None, None

    while True:
        nombre_input = input("\nIngrese el Nombre o Nickname del Operador en turno: ").strip()
        if not nombre_input:
            print("[!] Error: El nombre del operador no puede estar vacío.")
            continue
        if len(nombre_input) < 3:
            print("[!] Error: El nombre debe tener al menos 3 caracteres.")
            continue
        if nombre_input.isdigit():
            print("[!] Error: El nombre del operador no puede ser puramente numérico.")
            continue

        operador_nombre = nombre_input.title()
        print(f"\n[✓] Sesión iniciada correctamente para: {operador_nombre} ({credencial_activa})")
        print("=" * 80)
        break

    return credencial_activa, operador_nombre

# Registra la fecha pero estando bien sincronizado con la laptop. No te deja meter 
# fechas que ya pasaron ni días que no existen (como 31 de febrero) porque usa la 
# librería de datetime. Al final lo empaqueta todo en una tupla inmutable.
def solicitar_fecha_operacion_blindada():
    print("\n" + "-" * 80)
    print(" REGISTRO DE FECHA DE OPERACIÓN PARA REPORTES ".center(80, "-"))
    print("-" * 80)

    fecha_actual_sistema = date.today()
    anio_actual = fecha_actual_sistema.year

    print(f"-> AÑO DE OPERACIÓN SINCRONIZADO EN TIEMPO REAL: {anio_actual}")

    while True:
        try:
            entrada_mes = input("Ingrese el mes de operación (1-12): ").strip()
            if not entrada_mes.isdigit():
                print("[!] Error: El mes debe ser un número entero entre 1 y 12.")
                continue
            mes = int(entrada_mes)
            if not (1 <= mes <= 12):
                print("[!] Error: Mes no válido. Ingrese un valor del 1 al 12.")
                continue

            entrada_dia = input("Ingrese el día de operación (1-31): ").strip()
            if not entrada_dia.isdigit():
                print("[!] Error: El día debe ser un número entero entre 1 y 31.")
                continue
            dia = int(entrada_dia)

            fecha_ingresada = date(anio_actual, mes, dia)

            if fecha_ingresada < fecha_actual_sistema:
                print(f"[!] Error de Negocio: La fecha {dia:02d}/{mes:02d}/{anio_actual} ya ocurrió.")
                print(f"    Solo se permiten registros presentes o futuros (Hoy es: {fecha_actual_sistema.strftime('%d/%m/%Y')}).\n")
                continue

            fecha_tupla = (fecha_ingresada.day, fecha_ingresada.month, fecha_ingresada.year)

            print(f"\n[✓] Fecha de operación validada en calendario real:")
            print(f"    Tupla Guardada: {fecha_tupla} | Formato Estampado: {fecha_tupla[0]:02d}/{fecha_tupla[1]:02d}/{fecha_tupla[2]}")
            print("-" * 80)

            return fecha_tupla

        except ValueError:
            print(f"[!] Error de Calendario: La fecha {dia}/{mes}/{anio_actual} NO EXISTE en el calendario.\n")


def formatear_fecha_tupla(fecha_tupla):
    return f"{fecha_tupla[0]:02d}/{fecha_tupla[1]:02d}/{fecha_tupla[2]}"


# El temporizador de inactividad de 10 minutos. Corre un hilo en segundo plano y usa 
# un ciclo for para contar el tiempo segundo a segundo. Si te vas por un café y dejas
# la pantalla tirada, congela la app y te pregunta si sigues ahí o si ya cierra la sesión.
def solicitar_entrada_con_inactividad(prompt_mensaje, segundos_limite=600):

    respuesta_usuario = [None]

    def capturar_input():
        try:
            respuesta_usuario[0] = input(prompt_mensaje).strip()
        except Exception:
            respuesta_usuario[0] = ""

    hilo_input = threading.Thread(target=capturar_input)
    hilo_input.daemon = True
    hilo_input.start()

    for segundo in range(1, segundos_limite + 1):
        hilo_input.join(timeout=1.0)
        
        if not hilo_input.is_alive():
            return respuesta_usuario[0]

    print("\n\n" + "!" * 80)
    print(" [!] ALERTA DE SEGURIDAD: SESIÓN EN PAUSA POR INACTIVIDAD (10 MINUTOS) ".center(80, "!"))
    print("!" * 80)

    while True:
        try:
            confirmacion = input("\nHa transcurrido tiempo sin actividad. ¿Desea continuar en la sesión? (si/no): ").strip().lower()
            if confirmacion == "si":
                print("\n[✓] Sesión reanudada con éxito.")
                return "REINTENTAR"
            elif confirmacion == "no":
                print("\n[!] Cerrando sesión por inactividad del usuario...")
                return "TIMEOUT_SALIR"
            else:
                print("[!] Respuesta no válida. Ingrese exclusivamente 'si' para reanudar o 'no' para salir.")
        except Exception:
            return "TIMEOUT_SALIR"

# Barra de progreso para darle presencia visual al programa. Usa time.sleep para 
# simular que está procesando los módulos y va pintando los bloquecitos hasta llegar al 100%.
def pantalla_carga(segundos=5, mensaje_proceso="Procesando"):
    print("\n" + "-" * 80)
    print(f"PROCESANDO: {mensaje_proceso}".center(80))
    print("-" * 80)
    for i in range(1, segundos + 1):
        time.sleep(1)
        porcentaje = int((i / segundos) * 100)
        bloques = int((porcentaje / 100) * 30)
        barra = "█" * bloques + "-" * (30 - bloques)
        print(f"[{barra}] {porcentaje}% | Estado: OK ({i}/{segundos}s)")
    print("-" * 80 + "\n")

# Imprime el cartelote de bienvenida con el nombre del operador y su rol. Pura estética 
# multiplicando los caracteres '=' para que quede bien centrado y ordenado.
def mostrar_bienvenida(operador_nombre, credencial_activa):
    marco = "=" * 80
    print(marco)
    print("SUITE INTEGRAL DE AUTOMATIZACIÓN Y LOGÍSTICA DE TRANSPORTE".center(80))
    print(f"BIENVENIDO/A: {operador_nombre.upper()} | CREDENCIAL: [{credencial_activa}]".center(80))
    print(marco)
    pantalla_carga(segundos=5, mensaje_proceso="Inicializando ambiente de trabajo")

# El motor financiero. Aquí se hace toda la matemática: sueldo del chofer según el camión, 
# recargo del 25% si la unidad trae rampa de descarga, el rendimiento del diésel y la 
# ganancia neta final. Si le mandas la bandera de debug, frena el código con PDB.
def calcular_viaje_blindado(ruta, camion, precio_diesel_litro, activar_debug=False):
    if activar_debug:
        print("\n[PDB DEBUGGING] Deteniendo ejecución para inspección de variables...")
        pdb.set_trace()

    pago_chofer_final = ruta["pago_chofer_base"] * camion["factor_chofer"]
    recargo_rampa_monto = ruta["pago_ruta"] * camion["recargo_rampa"] if camion["tiene_rampa"] else 0.0
    cobro_total_cliente = ruta["pago_ruta"] + recargo_rampa_monto

    rendimiento_km_l = 2.8 / camion["factor_diesel"]
    litros_estimados = ruta["km"] / rendimiento_km_l
    costo_diesel_total = litros_estimados * precio_diesel_litro

    costos_totales = pago_chofer_final + costo_diesel_total
    ganancia_neta = cobro_total_cliente - costos_totales

    return {
        "cobro_base": ruta["pago_ruta"],
        "recargo_rampa": recargo_rampa_monto,
        "cobro_total": cobro_total_cliente,
        "pago_chofer": pago_chofer_final,
        "litros_diesel": litros_estimados,
        "costo_diesel": costo_diesel_total,
        "costos_totales": costos_totales,
        "ganancia_neta": ganancia_neta
    }


# Genera el ticket individual en .txt. En cuanto acaba una simulación, crea la carpeta 
# de reportes (si no existe) y escupe un archivo con todo el desglose financiero del viaje.
def guardar_reporte_viaje_automatico(operador, fecha_tupla, ruta_info, camion_info, res):
    if not os.path.exists(REPORTES_DIR):
        os.makedirs(REPORTES_DIR)

    fecha_str = formatear_fecha_tupla(fecha_tupla)
    nombre_clean = ruta_info['nombre'].replace(" ", "_").replace("-", "_")
    filename = os.path.join(REPORTES_DIR, f"Reporte_{nombre_clean}_{camion_info['config']}.txt")

    contenido = f"""================================================================================
REPORTE DE COSTOS Y GANANCIA NETA - TRANSPORTE
================================================================================
FECHA DE OPERACIÓN : {fecha_str}
OPERADOR EN TURNO  : {operador}
================================================================================
DETALLES DE LA RUTA:
 - Ruta               : {ruta_info['nombre']}
 - Distancia Total    : {ruta_info['km']} km
 - Días Estimados     : {ruta_info['dias']} día(s)

DETALLES DEL VEHÍCULO:
 - Unidad             : {camion_info['config']}
 - Capacidad Tanque   : {camion_info['tanque_galones']} Galones
 - Rampa de Descarga  : {'SÍ (+25%)' if camion_info['tiene_rampa'] else 'NO'}

DESGLOSE FINANCIERO:
 + Tarifa Base Ruta   : ${ruta_info['pago_ruta']:,.2f} MXN
 + Recargo por Rampa  : ${res['recargo_rampa']:,.2f} MXN
 -------------------------------------------------------------------------------
 = COBRO TOTAL CLIENTE: ${res['cobro_total']:,.2f} MXN

 - Pago al Chofer     : ${res['pago_chofer']:,.2f} MXN
 - Consumo Diésel     : {res['litros_diesel']:.2f} L (${res['costo_diesel']:,.2f} MXN)
 -------------------------------------------------------------------------------
 = COSTOS OPERATIVOS  : ${res['costos_totales']:,.2f} MXN

================================================================================
GANANCIA NETA FINAL  : ${res['ganancia_neta']:,.2f} MXN
================================================================================
"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"\n[✓] REPORTE INDIVIDUAL GENERADO AUTOMÁTICAMENTE EN:\n    {filename}")
    except Exception as e:
        print(f"[!] Error al escribir el reporte individual: {e}")

# El reporte consolidado de cierre. Se dispara si le das a la opción 4 de salir o si 
# te saca por inactividad. Suma todas las ganancias de los viajes que simulaste en el turno.
def generar_reporte_final_sesion(operador, fecha_tupla, historial_simulaciones):
    if not os.path.exists(REPORTES_DIR):
        os.makedirs(REPORTES_DIR)

    fecha_str = formatear_fecha_tupla(fecha_tupla)
    filename = os.path.join(REPORTES_DIR, "Reporte_Final_Consolidado_Sesion.txt")

    total_viajes = len(historial_simulaciones)
    ganancia_acumulada = sum(item['res']['ganancia_neta'] for item in historial_simulaciones)

    contenido = f"""================================================================================
REPORTE CONSOLIDADO FINAL DE LA SESIÓN
================================================================================
FECHA DE EMISIÓN  : {fecha_str}
OPERADOR          : {operador}
TOTAL SIMULACIONES: {total_viajes}
GANANCIA ACUMULADA: ${ganancia_acumulada:,.2f} MXN
================================================================================
DETALLE DE OPERACIONES REALIZADAS EN LA SESIÓN:
"""
    if total_viajes == 0:
        contenido += "\n [!] No se registraron simulaciones de viaje durante esta sesión."
    else:
        for idx, item in enumerate(historial_simulaciones, start=1):
            r = item['ruta']
            c = item['camion']
            res = item['res']
            contenido += f"\n [{idx}] Ruta: {r['nombre']:<30} | Camión: {c['config']:<6} | Ganancia Neta: ${res['ganancia_neta']:,.2f} MXN"

    contenido += "\n\n================================================================================"

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(contenido)
        pantalla_carga(segundos=5, mensaje_proceso="Emitiendo Reporte Final Consolidado")
        print(f"[✓] REPORTE FINAL CONSOLIDADO EMITIDO CON ÉXITO EN:\n    {filename}\n")
    except Exception as e:
        print(f"[!] Error al emitir el reporte final: {e}")


# Construye y despliega el menú en formato de matriz de 2D. Recorre las filas y columnas 
# con ciclos anidados para que las opciones y descripciones queden alineaditas en pantalla.
def obtener_matriz_menu():
    return [
        ["1", "Simular Viaje y Ganancia", "Calcular costos y rentabilidad"],
        ["2", "Ver Archivos de Texto", "Inspeccionar catálogos o reportes"],
        ["3", "Depuración Técnica (PDB)", "Ejecutar simulación con debugger"],
        ["4", "Salir del Sistema", "Emitir reporte final y cerrar sesión"]
    ]


def mostrar_menu_matriz(matriz):
    print("\n" + "=" * 80)
    print(" MENÚ PRINCIPAL DE OPERACIONES (MATRIZ DE OPCIONES) ".center(80, "="))
    print("=" * 80)
    print(f"{'ID':<5} | {'OPCIÓN':<28} | {'DESCRIPCIÓN':<35}")
    print("-" * 80)
    for fila in matriz:
        linea = f"[{fila[0]}]".ljust(6) + f"| {fila[1]}".ljust(30) + f"| {fila[2]}"
        print(linea)
    print("=" * 80)


def sub_menu_simular(operador, fecha_tupla, historial, activar_debug=False):
    rutas = cargar_rutas_blindado()
    camiones = cargar_camiones_blindado()

    if not rutas or not camiones:
        print("\n[!] ERROR CRÍTICO: No se encontraron los archivos maestros de datos o están vacíos (0 KB).")
        print(f"    Verifique que 'Rutas.txt' y 'Camiones.txt' tengan datos guardados (Ctrl + S).")
        return

    print("\n--- RUTAS DISPONIBLES ---")
    for id_r, r in rutas.items():
        print(f"[{id_r}] {r['nombre']} | {r['km']} km | Tarifa Base: ${r['pago_ruta']:,.2f}")

    while True:
        id_r = input("\nSeleccione el ID de la ruta deseada: ").strip()
        if id_r in rutas:
            break
        print("[!] Error: ID de ruta inexistente. Ingrese un ID válido de la lista.")

    print("\n--- CAMIONES DISPONIBLES ---")
    for id_c, c in camiones.items():
        rampa_txt = "SÍ (+25%)" if c['tiene_rampa'] else "NO"
        print(f"[{id_c}] Configuración: {c['config']} | Tanque: {c['tanque_galones']} Gal | Rampa: {rampa_txt}")

    while True:
        id_c = input("\nSeleccione el ID del camión asignado: ").strip()
        if id_c in camiones:
            break
        print("[!] Error: ID de camión inexistente. Ingrese un ID válido de la lista.")

    while True:
        try:
            precio_input = input("\nIngrese el precio actual por litro de diésel ($ MXN): ").strip()
            precio_diesel = float(precio_input)
            if precio_diesel <= 0:
                print("[!] El precio debe ser un número mayor a cero.")
                continue
            break
        except ValueError:
            print("[!] Entrada inválida. Ingrese un valor decimal válido (ej. 24.50).")

    pantalla_carga(segundos=5, mensaje_proceso="Calculando estructura financiera")
    res = calcular_viaje_blindado(rutas[id_r], camiones[id_c], precio_diesel, activar_debug=activar_debug)

    print("\n" + "=" * 50)
    print(" RESULTADO DE LA SIMULACIÓN ".center(50, "="))
    print("=" * 50)
    print(f" Cobro Total Cliente : ${res['cobro_total']:,.2f} MXN")
    print(f" Costos Operativos   : ${res['costos_totales']:,.2f} MXN")
    print(f" GANANCIA NETA ESTIMADA: ${res['ganancia_neta']:,.2f} MXN")
    print("=" * 50)

    guardar_reporte_viaje_automatico(operador, fecha_tupla, rutas[id_r], camiones[id_c], res)
    historial.append({"ruta": rutas[id_r], "camion": camiones[id_c], "res": res})

# El visor de archivos de texto. Lista los .txt que pesan más de 0 KB y cuando abres uno 
# te imprime un encabezado explicando qué significa cada columna para que el profe no se pierda.
def sub_menu_ver_archivos():
    while True:
        archivos = {}
        
        if os.path.exists(RUTA_RUTAS) and os.path.getsize(RUTA_RUTAS) > 0:
            archivos["1"] = RUTA_RUTAS
        if os.path.exists(RUTA_CAMIONES) and os.path.getsize(RUTA_CAMIONES) > 0:
            archivos["2"] = RUTA_CAMIONES

        idx = 3
        if os.path.exists(REPORTES_DIR):
            for f in sorted(os.listdir(REPORTES_DIR)):
                if f.endswith('.txt'):
                    path_rep = os.path.join(REPORTES_DIR, f)
                    if os.path.getsize(path_rep) > 0:
                        archivos[str(idx)] = path_rep
                        idx += 1

        print("\n--- ARCHIVOS DE TEXTO REGISTRADOS EN DISCO ---")
        if not archivos:
            print("[!] Advertencia: Los archivos maestros están vacíos (0 KB) o no existen.")
            print("    Asegúrese de guardar los datos en 'Rutas.txt' y 'Camiones.txt' con Ctrl + S.")
            input("\nPresione ENTER para regresar al menú principal...")
            break

        for k, v in archivos.items():
            nombre_mostrar = os.path.basename(v)
            print(f"[{k}] {nombre_mostrar} ({v})")

        opcion = input("\nSeleccione el ID del archivo a visualizar (o presione ENTER para volver al menú): ").strip()

        if opcion == "":
            break

        if opcion in archivos:
            archivo_destino = archivos[opcion]
            try:
                pantalla_carga(segundos=5, mensaje_proceso="Cargando contenido del archivo")
                print("\n" + "=" * 80)
                print(f" CONTENIDO DEL ARCHIVO: {os.path.basename(archivo_destino)} ".center(80, "="))
                print("=" * 80)
                
                if archivo_destino == RUTA_RUTAS:
                    print("ESTRUCTURA DE DATOS (RUTAS MAESTRO):")
                    print("[ID] | [Nombre de Ruta] | [Distancia KM] | [Tarifa Cliente $] | [Días] | [Pago Base Chofer $]")
                    print("-" * 80)
                elif archivo_destino == RUTA_CAMIONES:
                    print("ESTRUCTURA DE DATOS (CAMIONES MAESTRO):")
                    print("[ID] | [Config] | [Tanque Gal] | [Factor Chofer] | [Factor Diésel] | [Rampa 1/0] | [Recargo %]")
                    print("-" * 80)

                with open(archivo_destino, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    print(contenido)
                
                print("=" * 80)
                input("\nPresione ENTER para continuar...")
                break
            except Exception as e:
                print(f"[!] Error al leer el archivo: {e}")
                break
        else:
            print(f"\n[!] Error: La opción '[{opcion}]' no es válida. Seleccione una opción de la lista.")

# La función orquestadora principal. Es la que manda a llamar a todas las demás en orden:
# login -> bienvenida -> captura de fecha -> ciclo infinito del menú.
def ejecutar_sistema_completo():
    credencial, operador = autenticar_usuario_blindado()
    if not operador:
        return

    mostrar_bienvenida(operador, credencial)
    fecha_operacion = solicitar_fecha_operacion_blindada()

    matriz_menu = obtener_matriz_menu()
    historial_sesion = []

    while True:
        mostrar_menu_matriz(matriz_menu)
        
        opcion = solicitar_entrada_con_inactividad("\nSeleccione una opción de la matriz [1-4]: ", segundos_limite=600)

        if opcion == "REINTENTAR":
            continue
        elif opcion == "TIMEOUT_SALIR":
            generar_reporte_final_sesion(operador, fecha_operacion, historial_sesion)
            print(f"Cierre automático por inactividad ejecutado para el operador: {operador}.")
            break

        if opcion == "1":
            sub_menu_simular(operador, fecha_operacion, historial_sesion, activar_debug=False)
        elif opcion == "2":
            sub_menu_ver_archivos()
        elif opcion == "3":
            print("\n[!] MODO DEBUGGING ACTIVADO (PDB)")
            sub_menu_simular(operador, fecha_operacion, historial_sesion, activar_debug=True)
        elif opcion == "4":
            generar_reporte_final_sesion(operador, fecha_operacion, historial_sesion)
            print(f"Cierre de sesión finalizado. Operador: {operador}. ¡Hasta pronto!")
            break
        else:
            print("\n[!] Opción no válida. Ingrese un ID numérico de la matriz (1, 2, 3 o 4).")


if __name__ == "__main__":
    ejecutar_sistema_completo()