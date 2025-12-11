def valores_invalidos(proveedor):

    rangos_permitidos = {
        "precio": (1, 100000),
        "calidad": (1, 10),
        "tiempo": (1, 365)
    }

    campos_invalidos = []

    for campo in rangos_permitidos:

        minimo, maximo = rangos_permitidos[campo]
        valor = proveedor[campo]
        if valor < minimo or valor > maximo:
            campos_invalidos.append(campo)

    if len(campos_invalidos) > 0:

        mensaje = "Se encontraron valores inválidos en: "
        i = 0
        while i < len(campos_invalidos):
            mensaje = mensaje + campos_invalidos[i]
            if i < len(campos_invalidos) - 1:
                mensaje = mensaje + ", "
            i = i + 1

        return "VALORES INVÁLIDOS – REGISTRO BLOQUEADO", mensaje

    return "VALORES VÁLIDOS – CONTINUAR", ""