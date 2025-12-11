lista_proveedores = obtener_lista_con_puntajes_finales()

i = 0
while i < len(lista_proveedores):
    j = i + 1
    while j < len(lista_proveedores):
        if lista_proveedores[j]["puntaje"] > lista_proveedores[i]["puntaje"]:
            temporal = lista_proveedores[i]
            lista_proveedores[i] = lista_proveedores[j]
            lista_proveedores[j] = temporal
        j = j + 1
    i = i + 1

posicion = 1
i = 0

while i < len(lista_proveedores):
    if i == 0:
        lista_proveedores[i]["posicion"] = posicion
    else:
        if lista_proveedores[i]["puntaje"] == lista_proveedores[i - 1]["puntaje"]:
            lista_proveedores[i]["posicion"] = lista_proveedores[i - 1]["posicion"]
        else:
            posicion = posicion + 1
            lista_proveedores[i]["posicion"] = posicion
    i = i + 1

ranking_valido = True