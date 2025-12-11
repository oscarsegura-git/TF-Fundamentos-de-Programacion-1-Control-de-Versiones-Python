def validar_proveedor():
    
    campos_obligatorios = ["nombre", "tipo (papa,camote,maiz)", "contacto", "region",
                           "precio", "calidad", "tiempo"]

    proveedor = {}
    proveedor_valido = True
    i = 0

    print("\n--- Ingreso de datos del proveedor ---")

    while i < len(campos_obligatorios):

        campo = campos_obligatorios[i]
        valor = input("Ingrese " + campo + ": ")

        
        if valor.strip() == "":
            proveedor_valido = False
            break
        if campo == "precio" or campo == "calidad" or campo == "tiempo":
          
            if not valor.isnumeric():
                proveedor_valido = False
                break
            else:
                
                 valor = int(valor)
                
        proveedor[campo] = valor
      
        i = i + 1
    
    if proveedor_valido:
        return "VALIDO", proveedor
    else:
        return "INVALIDO", None
        
validar_proveedor()       