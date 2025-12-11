def HU4_G2():
    estructura = Acceder_a_estructura_puntajes_finales()

    if evaluacion_generada:
        preparar_estructura_de_salida()
        convertir_estructura_interna_a_formato_adecuado_para_exportacion()
        crear_procedimiento_para_guardar_en_archivo()
        Escribir_contenido_en_archivo()
        Confirmar_generacion_archivo_correcta()
        dejar_archivo_disponible_para_analista()
    else:
        generar_error("Evaluación no completada. No se puede exportar.")
