lista_proveedores = obtener_lista_con_puntajes_finales()

preparar_lista_ordenada = lista_proveedores
i = 0
while i < len(preparar_lista_ordenada):
    j = i + 1
    while j < len(preparar_lista_ordenada):
        if preparar_lista_ordenada[j]["puntaje"] > preparar_lista_ordenada[i]["puntaje"]:
            temporal = preparar_lista_ordenada[i]
            preparar_lista_ordenada[i] = preparar_lista_ordenada[j]
            preparar_lista_ordenada[j] = temporal
        j = j + 1
    i = i + 1

lista_proveedores = preparar_lista_ordenada
ranking_confirmado = True

