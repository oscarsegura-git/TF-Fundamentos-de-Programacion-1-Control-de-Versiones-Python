def guardar_metadatos_evaluacion():
    global calculo_de_puntajes_termino
    global resultados_finales
    global informe_final
    global metadatos_disponibles

    if calculo_de_puntajes_termino == True:
        fecha_hora_actual = obtener_fecha_y_hora_actual()
        metadatos = {}
        metadatos["fecha_hora_evaluacion"] = fecha_hora_actual
        resultados_finales["metadatos"] = metadatos
        informe_final["metadatos"] = metadatos
        metadatos_disponibles = True
