def datos_incompletos(proveedor):

    campos_obligatorios = ["nombre", "tipo (papa,camote,maiz)", "contacto", "region",
                           "precio", "calidad", "tiempo"]

    campos_faltantes = []

    i = 0
    
    while i < len(campos_obligatorios):

        campo = campos_obligatorios[i]

        if campo not in proveedor or proveedor[campo] == "" or proveedor[campo] is None:
            campos_faltantes.append(campo)

        i = i + 1

    if len(campos_faltantes) > 0:

        mensaje = "Faltan completar los siguientes campos: "

        k = 0
        while k < len(campos_faltantes):
            mensaje = mensaje + campos_faltantes[k]
            if k < len(campos_faltantes) - 1:
                mensaje = mensaje + ", "
            k = k + 1

        return "DATOS INCOMPLETOS – REGISTRO BLOQUEADO", mensaje

    return "DATOS COMPLETOS – CONTINUAR REGISTRO", ""
    