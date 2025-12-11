def detectar_duplicado(proveedor_ingresado, lista_proveedores):

    claves_unicas = ["nombre", "contacto", "region"]
    proveedor_duplicado = False
    i = 0  

    while i < len(lista_proveedores):

        proveedor_actual = lista_proveedores[i]
        coincidencias = 0  # Contador de coincidencias

        j = 0  
        while j < len(claves_unicas):

            clave = claves_unicas[j]

            if proveedor_ingresado[clave] == proveedor_actual[clave]:
                coincidencias = coincidencias + 1
            j = j + 1

        if coincidencias == len(claves_unicas):
            proveedor_duplicado = True
            break
        i = i + 1

    if proveedor_duplicado:
        return "PROVEEDOR DUPLICADO – REGISTRO BLOQUEADO"
    else:
        return "NO DUPLICADO – CONTINUAR REGISTRO"
        