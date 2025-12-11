def insertar_proveedor(tabla, proveedor_validado):

    columnas = ["nombre", "tipo (papa,camote,maiz)", "contacto", "region",
                "precio", "calidad", "tiempo",
                "puntaje_precio", "puntaje_calidad", "puntaje_tiempo",
                "puntaje_total", "estado"]

    fila = {}

    
    for columna in columnas:
        if columna in proveedor_validado:
            fila[columna] = proveedor_validado[columna]
        else:
            fila[columna] = None 

    tabla.append(fila)

    return "Registro insertado correctamente"