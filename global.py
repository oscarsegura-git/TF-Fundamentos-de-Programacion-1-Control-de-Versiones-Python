import json
import csv
import sqlite3
from datetime import datetime

# HU1: Validación de datos de proveedores-------------------------------------------------------------------------------------------------------------------
def HU1_G1_validar_proveedor():
    campos_obligatorios = ["nombre", "tipo", "contacto", "region", "precio", "calidad", "tiempo"]
    proveedor = {}
    proveedor_valido = True

    print("\n--- Ingreso de datos del proveedor ---")
    i = 0
    while i < len(campos_obligatorios):
        campo = campos_obligatorios[i]
        valor = input(f"Ingrese {campo}: ")
        if valor.strip() == "":
            proveedor_valido = False
            break
        if campo in ["precio", "calidad", "tiempo"]:
            if not valor.isnumeric():
                proveedor_valido = False
                break
            valor = int(valor)
        proveedor[campo] = valor
        i += 1

    return ("VALIDO", proveedor) if proveedor_valido else ("INVALIDO", None)

def HU1_G2_deteccion_duplicado(proveedor, tabla):
    claves_unicas = ["nombre", "contacto", "region"]
    proveedor_duplicado = False
    i = 0
    while i < len(tabla):
        coincidencias = 0
        j = 0
        while j < len(claves_unicas):
            if proveedor[claves_unicas[j]] == tabla[i][claves_unicas[j]]:
                coincidencias += 1
            j += 1
        if coincidencias == len(claves_unicas):
            proveedor_duplicado = True
            break
        i += 1
    return proveedor_duplicado

def HU1_G3_datos_incompletos(proveedor):
    campos_obligatorios = ["nombre", "tipo", "contacto", "region", "precio", "calidad", "tiempo"]
    campos_faltantes = []
    i = 0
    while i < len(campos_obligatorios):
        campo = campos_obligatorios[i]
        if campo not in proveedor or proveedor[campo] == "" or proveedor[campo] is None:
            campos_faltantes.append(campo)
        i += 1
    return campos_faltantes

def HU1_G4_valores_invalidos(proveedor):
    rangos = {"precio": (1,100000), "calidad": (1,10), "tiempo": (1,365)}
    campos_invalidos = []
    i = 0
    while i < len(rangos):
        clave = list(rangos.keys())[i]
        minimo, maximo = rangos[clave]
        valor = proveedor[clave]
        if valor < minimo or valor > maximo:
            campos_invalidos.append(f"{clave} ({valor} fuera de rango {minimo}-{maximo})")
        i += 1
    return campos_invalidos

# HU2: Organización de datos en tabla------------------------------------------------------------------------------------------------------------------------
tabla_proveedores = []

def HU2_G1_insertar_proveedor(tabla, proveedor):
    columnas = ["nombre","tipo","contacto","region","precio","calidad","tiempo",
                "puntaje_precio","puntaje_calidad","puntaje_tiempo","puntaje_total","estado"]
    fila = {}
    i = 0
    while i < len(columnas):
        col = columnas[i]
        fila[col] = proveedor.get(col, None)
        i += 1
    tabla.append(fila)
    return fila

# HU3: Determinación de valores de referencia----------------------------------------------------------------------------------------------------------------
valores_minimos = {"precio": None, "tiempo": None}

def HU3_G1_determinar_valores(tabla):
    if not tabla:
        return False
    precio_min = tabla[0]['precio']
    tiempo_min = tabla[0]['tiempo']
    for p in tabla:
        if p['precio'] < precio_min:
            precio_min = p['precio']
        if p['tiempo'] < tiempo_min:
            tiempo_min = p['tiempo']
    valores_minimos["precio"] = precio_min
    valores_minimos["tiempo"] = tiempo_min
    return True

def HU3_G2_tabla_vacia(tabla):
    if len(tabla) == 0:
        print("Error: No existen suficientes datos para obtener límites.")
        return True
    return False

def HU3_G3_actualizar_limites(nuevo_proveedor):
    for clave in ["precio", "tiempo"]:
        if valores_minimos[clave] is None or nuevo_proveedor[clave] < valores_minimos[clave]:
            valores_minimos[clave] = nuevo_proveedor[clave]
    return True

# HU4: Cálculo de puntaje------------------------------------------------------------------------------------------------------------------------------------
def HU4_G1_calcular_puntaje(tabla):
    i = 0
    while i < len(tabla):
        p = tabla[i]
        p_precio = (valores_minimos["precio"] / p['precio']) * 35
        p_calidad = (p['calidad']/10) * 45
        p_tiempo = (valores_minimos["tiempo"] / p['tiempo']) * 20
        p['puntaje_precio'] = round(p_precio,2)
        p['puntaje_calidad'] = round(p_calidad,2)
        p['puntaje_tiempo'] = round(p_tiempo,2)
        p['puntaje_total'] = round(p_precio + p_calidad + p_tiempo,2)
        i += 1

def HU4_G2_exportar_resultados(tabla):
    resultados = []
    for p in tabla:
        resultados.append({"nombre":p["nombre"], "puntaje_total":p["puntaje_total"], "estado":p.get("estado","Pendiente")})
    return resultados

def HU4_G3_guardar_metadatos(tabla):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    i = 0
    while i < len(tabla):
        tabla[i]["fecha_evaluacion"] = fecha_hora
        i += 1

# HU5: Ranking-----------------------------------------------------------------------------------------------------------------------------------------------
def HU5_G1_generar_ranking(tabla):
    n = len(tabla)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if tabla[j]["puntaje_total"] > tabla[i]["puntaje_total"]:
                tabla[i], tabla[j] = tabla[j], tabla[i]
            j += 1
        i += 1
    # asignar posiciones
    i = 0
    posicion = 1
    while i < n:
        if i>0 and tabla[i]["puntaje_total"] == tabla[i-1]["puntaje_total"]:
            tabla[i]["posicion"] = tabla[i-1]["posicion"]
        else:
            tabla[i]["posicion"] = posicion
            posicion += 1
        i += 1

def HU5_G2_mostrar_ranking(tabla):
    print("\n--- Ranking de Proveedores ---")
    i = 0
    while i < len(tabla):
        p = tabla[i]
        print(f"{p['posicion']}. {p['nombre']} - Puntaje Total: {p['puntaje_total']} - Estado: {p.get('estado','Pendiente')}")
        i += 1

# HU6: Evaluación por umbrales-------------------------------------------------------------------------------------------------------------------------------
def HU6_G1_evaluar_por_criterios(tabla):
    i = 0
    while i < len(tabla):
        p = tabla[i]
        if p['puntaje_precio'] >= 15 and p['puntaje_calidad'] >= 30 and p['puntaje_tiempo'] >= 10:
            p['estado'] = "ACEPTADO"
        else:
            p['estado'] = "DESCARTADO"
        i += 1

def HU6_G2_evaluar_por_total(tabla):
    i = 0
    while i < len(tabla):
        p = tabla[i]
        if p['puntaje_total'] >= 70:
            p['estado'] = "ACEPTADO"
        else:
            p['estado'] = "DESCARTADO"
        i += 1

# HU7: Fichas------------------------------------------------------------------------------------------------------------------------------------------------
def HU7_G1_generar_fichas(tabla):
    fichas = []
    i = 0
    while i < len(tabla):
        ficha = {}
        for k,v in tabla[i].items():
            if k != "posicion":
                ficha[k] = v
        fichas.append(ficha)
        i += 1
    return fichas

def HU7_G2_exportar_fichas(fichas):
    # JSON
    i = 0
    while i < len(fichas):
        f = fichas[i]
        with open(f"perfil_{f['nombre']}.json", 'w', encoding='utf-8') as file:
            json.dump(f, file, indent=4, ensure_ascii=False)
        i += 1
    # CSV
    with open("resumen_perfiles.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre","Puntaje Total","Estado"])
        i = 0
        while i < len(fichas):
            f = fichas[i]
            writer.writerow([f["nombre"], f["puntaje_total"], f["estado"]])
            i += 1
    # SQLite
    conn = sqlite3.connect("perfiles_finales.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS perfiles(
            nombre TEXT, tipo TEXT, contacto TEXT, region TEXT,
            puntaje_precio REAL, puntaje_calidad REAL, puntaje_tiempo REAL,
            puntaje_total REAL, estado TEXT
        )
    """)
    i = 0
    while i < len(fichas):
        f = fichas[i]
        cursor.execute("INSERT INTO perfiles VALUES(?,?,?,?,?,?,?,?,?)", (
            f["nombre"],f["tipo"],f["contacto"],f["region"],
            f["puntaje_precio"],f["puntaje_calidad"],f["puntaje_tiempo"],
            f["puntaje_total"],f["estado"]
        ))
        i += 1
    conn.commit()
    conn.close()
    print("Exportación JSON, CSV y SQLite completada.")

# MENÚ PRINCIPAL---------------------------------------------------------------------------------------------------------------------------------------------
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar proveedor")
        print("2. Ver tabla de proveedores")
        print("3. Calcular puntajes y ranking")
        print("4. Evaluar proveedores por criterios")
        print("5. Evaluar proveedores por puntaje total")
        print("6. Generar fichas")
        print("7. Exportar fichas y resumen")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion=="1":
            status, proveedor = HU1_G1_validar_proveedor()
            if status=="INVALIDO":
                print("Error: Datos inválidos, verifique campos numéricos y obligatorios.")
                continue

            if HU1_G2_deteccion_duplicado(proveedor, tabla_proveedores):
                print("Error: Proveedor duplicado. Ya existe un proveedor con el mismo nombre, contacto y región.")
                continue

            incompletos = HU1_G3_datos_incompletos(proveedor)
            if incompletos:
                print("Error: Campos incompletos:", ", ".join(incompletos))
                continue

            invalidos = HU1_G4_valores_invalidos(proveedor)
            if invalidos:
                print("Error: Valores inválidos:", ", ".join(invalidos))
                continue

            HU2_G1_insertar_proveedor(tabla_proveedores, proveedor)
            HU3_G3_actualizar_limites(proveedor)
            print(f"Proveedor {proveedor['nombre']} agregado correctamente.")

        elif opcion=="2":
            if not tabla_proveedores:
                print("No hay proveedores registrados.")
            else:
                for p in tabla_proveedores:
                    print(p)

        elif opcion=="3":
            if HU3_G2_tabla_vacia(tabla_proveedores):
                continue
            HU3_G1_determinar_valores(tabla_proveedores)
            HU4_G1_calcular_puntaje(tabla_proveedores)
            HU5_G1_generar_ranking(tabla_proveedores)
            HU5_G2_mostrar_ranking(tabla_proveedores)

        elif opcion=="4":
            HU6_G1_evaluar_por_criterios(tabla_proveedores)
            print("Evaluación por criterios completada.")

        elif opcion=="5":
            HU6_G2_evaluar_por_total(tabla_proveedores)
            print("Evaluación por puntaje total completada.")

        elif opcion=="6":
            fichas = HU7_G1_generar_fichas(tabla_proveedores)
            print("Fichas generadas en memoria.")

        elif opcion=="7":
            fichas = HU7_G1_generar_fichas(tabla_proveedores)
            HU7_G2_exportar_fichas(fichas)

        elif opcion=="8":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__=="__main__":
    menu()
