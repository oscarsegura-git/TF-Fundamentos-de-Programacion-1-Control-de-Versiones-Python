
# HU3 - G1


def HU3_G1(datos_disponibles):
    if datos_disponibles:
        precio_minimo = encontrar_precio_minimo()
        tiempo_minimo = encontrar_tiempo_minimo()

        if precio_minimo is not None and tiempo_minimo is not None:
            guardar_valores_minimos_en_estructura(precio_minimo, tiempo_minimo)
            resultado_final = crear_resultado(precio_minimo, tiempo_minimo)
            guardar_resultado_en_informe(resultado_final)
            valores_almacenados = True
        else:
            generar_error("No se pudieron calcular los valores mínimos.")
            valores_almacenados = False

    else:
        generar_error("No existen datos de proveedores disponibles.")
        valores_almacenados = False

    return valores_almacenados
