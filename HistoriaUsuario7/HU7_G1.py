def HU7_G1():
    # Obtener lista de proveedores evaluados (con puntajes y estado final)
    lista_proveedores = obtener_lista_final()

    fichas_generadas = []

    i = 0
    while i < len(lista_proveedores):
        datos = lista_proveedores[i]

        plantilla = {
            "nombre": datos["nombre"],
            "tipo": datos["tipo"],
            "contacto": datos["contacto"],
            "region": datos["region"],

            "puntaje_precio": datos["puntaje_precio"],
            "puntaje_calidad": datos["puntaje_calidad"],
            "puntaje_tiempo": datos["puntaje_tiempo"],
            "puntaje_total": datos["puntaje_total"],

            "estado": datos["estado"]
        }

        fichas_generadas.append(plantilla)

        i += 1

    return fichas_generadas

