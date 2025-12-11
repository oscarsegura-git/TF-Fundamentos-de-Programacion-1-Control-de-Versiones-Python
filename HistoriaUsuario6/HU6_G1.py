lista_proveedores = obtener_lista_con_puntajes()

minimo_precio = 15
minimo_calidad = 30
minimo_tiempo = 10

i = 0
while i < len(lista_proveedores):

    puntaje_precio = lista_proveedores[i]["puntaje_precio"]
    puntaje_calidad = lista_proveedores[i]["puntaje_calidad"]
    puntaje_tiempo = lista_proveedores[i]["puntaje_tiempo"]

    cumple_precio = False
    cumple_calidad = False
    cumple_tiempo = False

    if puntaje_precio >= minimo_precio:
        cumple_precio = True

    if puntaje_calidad >= minimo_calidad:
        cumple_calidad = True

    if puntaje_tiempo >= minimo_tiempo:
        cumple_tiempo = True

    if cumple_precio and cumple_calidad and cumple_tiempo:
        lista_proveedores[i]["estado"] = "ACEPTADO"
    else:
        lista_proveedores[i]["estado"] = "DESCARTADO"

    i = i + 1
