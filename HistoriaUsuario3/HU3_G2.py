def HU3_G2(tabla_vacia):
    if tabla_vacia:
        activar_indicador_sin_datos = True
        generar_error("No existen suficientes datos para obtener límites.")
        proceso_detenido = True

        return {
            "sin_datos": activar_indicador_sin_datos,
            "proceso_detenido": proceso_detenido,
            "estado": "ERROR"
        }

    return {"estado": "OK"}
