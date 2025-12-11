from datetime import datetime

def guardar_metadatos(tabla):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    i = 0
    while i < len(tabla):
        tabla[i]["fecha_evaluacion"] = fecha_hora
        i += 1
    return tabla


tabla_actualizada = guardar_metadatos(tabla_proveedores)
print(tabla_actualizada)

