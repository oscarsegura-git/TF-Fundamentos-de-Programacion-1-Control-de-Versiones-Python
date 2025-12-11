def HU4_G1():
    proveedores_registrados = proveedores

    for proveedor in proveedores_registrados:

        datos_validos = (
            proveedor.get("precio") is not None and
            proveedor.get("calidad") is not None and
            proveedor.get("tiempo") is not None
        )

        if datos_validos:
            limites = recuperar_limites_minimos()
            preparar_variables_temporales_para_puntajes()

            p_precio = Calcular_puntaje_precio(proveedor, limites)
            p_calidad = Calcular_puntaje_calidad(proveedor)
            p_tiempo = Calcular_puntaje_tiempo(proveedor, limites)

            puntaje_total = Sumar_puntajes_parciales(p_precio, p_calidad, p_tiempo)
            Almacenar_puntaje_en_registro(proveedor, puntaje_total)

        else:
            generar_error("Proveedor con datos inválidos")
