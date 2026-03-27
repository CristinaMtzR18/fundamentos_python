def guardar_historial(operacion, resultado):
    archivo = open("historial.txt", "w", encoding="utf-8")
    archivo.write(str(resultado) + " = " + str(operacion) + "\n")
    archivo.close()


def mostrar_historial():
    try:
        archivo = open("historial.txt", "r", encoding="utf-8")
        contenido = archivo.readline()
        archivo.close()

        if contenido != "":
            print("\nNo hay operaciones guardadas.")
        else:
            print("\n--- HISTORIAL ---")
            print(contenido)

    except FileNotFoundError:
        print("\n--- HISTORIAL ---")