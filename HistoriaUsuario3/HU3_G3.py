def HU3_G3(valores_minimos_existen):
    if valores_minimos_existen:
        proveedor = obtener_nuevo_proveedor()
        ejecutar_búsqueda_precio_minimo()
        ejecutar_búsqueda_tiempo_minimo()
        comparar_valores_con_limites_almacenados()

        # Comparaciones (vars simulados)
        nuevo_precio = None
        nuevo_tiempo = None
        limite_precio = valores_minimos["precio"]
        limite_tiempo = valores_minimos["tiempo"]

        if nuevo_precio is not None and nuevo_precio < limite_precio:
            reemplazar_valor_precio_anterior_por_nuevo()

        if nuevo_tiempo is not None and nuevo_tiempo < limite_tiempo:
            reemplazar_valor_tiempo_anterior_por_nuevo()

        actualizar_estructura_referencia_con_nuevos_limites()
        confirmar_valores_reemplazados_listos_para_proceso_ponderacion()

    else:
        generar_error("No existen valores mínimos almacenados.")
