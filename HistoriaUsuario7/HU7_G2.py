def HU7_G2(fichas_generadas):
    import json
    import csv
    import sqlite3

    # Guardar cada ficha en JSON
    for ficha in fichas_generadas:
        archivo = f"perfil_{ficha['nombre']}.json"
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(ficha, f, indent=4, ensure_ascii=False)

    # Guardar resumen en CSV
    with open("resumen_perfiles.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Puntaje Total", "Estado"])
        for ficha in fichas_generadas:
            writer.writerow([ficha["nombre"], ficha["puntaje_total"], ficha["estado"]])

    # Guardar en SQLite
    conn = sqlite3.connect("perfiles_finales.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS perfiles (
            nombre TEXT,
            tipo TEXT,
            contacto TEXT,
            region TEXT,
            puntaje_precio REAL,
            puntaje_calidad REAL,
            puntaje_tiempo REAL,
            puntaje_total REAL,
            estado TEXT
        )
    """)

    for ficha in fichas_generadas:
        cursor.execute("""
            INSERT INTO perfiles VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            ficha["nombre"], ficha["tipo"], ficha["contacto"], ficha["region"],
            ficha["puntaje_precio"], ficha["puntaje_calidad"], ficha["puntaje_tiempo"],
            ficha["puntaje_total"], ficha["estado"]
        ))

    conn.commit()
    conn.close()
