# credenciales correctas
usuario_correcto = "admin"
clave_correcta = "1234"

# número de intentos
intentos = 3

while intentos > 0:

    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    # validar campos vacíos
    if usuario == "" or clave == "":
        print("Error: los campos no pueden estar vacíos")

    # validar credenciales
    elif usuario == usuario_correcto and clave == clave_correcta:
        print("Bienvenido al sistema")
        break

    else:
        intentos -= 1
        print("Datos incorrectos. Intentos restantes:", intentos)

if intentos == 0:
    print("Cuenta bloqueada")