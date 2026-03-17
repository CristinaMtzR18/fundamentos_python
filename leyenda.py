# =================================================================
# LA LEYENDA DEL CHARRO NEGRO: EL MENSAJE DEL PASADO
# =================================================================

import time # Opcional: para darle pausas dramáticas a la historia

# --- FASE 0: PREPARACIÓN ---
print("--- FASE 0: Preparando el entorno ---")
# Creamos la nota del viajero anterior en el disco duro
with open("nota_arbol.txt", "w", encoding="utf-8") as archivo:
    archivo.write("ADVERTENCIA PARA EL PRÓXIMO VIAJERO:\n")
    archivo.write("Si el Charro te ofrece 5000 monedas o más, es una trampa mortal.\n")
    archivo.write("Ignóralo y corre, no aceptes tratos.\n")
print("El archivo 'nota_arbol.txt' ha sido creado en la oscuridad del bosque...\n")


# --- FASE 1: El Encuentro ---
print("--- FASE 1: El Encuentro ---")
PRECIO_ALMA = 10000
monedas_ofrecidas = 6000
nombre_viajero = "TuNombre" # ¡Pon tu nombre aquí!

deficit = PRECIO_ALMA - monedas_ofrecidas
oferta_alta = monedas_ofrecidas >= 5000

print(f"De las sombras, el Charro Negro le ofrece a {nombre_viajero} {monedas_ofrecidas} monedas de oro.")


# --- FASE 2: El Mensaje del Pasado ---
print("\n--- FASE 2: El Mensaje del Pasado ---")
print("Encuentras una nota clavada en un árbol. La abres temblando...")
print("-" * 40)

# Lectura del archivo hacia la RAM
with open("nota_arbol.txt", "r", encoding="utf-8") as archivo:
    advertencia_leida = archivo.read()
    print(advertencia_leida, end="") # end="" evita saltos de línea extra

print("-" * 40)


# --- FASE 3: La Decisión ---
print("\n--- FASE 3: La Decisión ---")
decision = "rechazar" # Cambia esto a "aceptar" bajo tu propio riesgo

print(f"Tu decisión es: {decision.upper()}")

if decision == "aceptar" and oferta_alta:
    print("Ignoraste la nota. El Charro ríe siniestramente y tu alma se desvanece.")
elif decision == "rechazar":
    print("Le das la espalda al oro maldito y comienzas a correr hacia el pueblo.")
else:
    print("Te quedas paralizado. El caballo relincha impaciente.")


# --- FASE 4: La Huida en la Noche ---
# Solo huimos si la decisión fue rechazar o ignorar
if decision != "aceptar":
    print("\n--- FASE 4: La Huida en la Noche ---")
    print("¡Comienza la persecución!")

    # Ciclo For (Tiempo)
    for hora in range(1, 4):
        print(f"Corriendo en la hora {hora} de la madrugada...")

    energia = 100
    # Ciclo While (Resistencia física)
    while energia > 0:
        print(f"  -> Energía restante: {energia}")
        energia -= 30 
        
        # If simple anidado
        if energia > 0 and energia < 30:
            print("  -> ¡Alerta! Casi no puedes respirar, el galope suena muy cerca...")

    print("\n¡Ves a lo lejos las luces de la iglesia del pueblo! Estás a salvo.")


# --- FASE 5: El Nuevo Legado ---
# Solo dejamos registro si sobrevivimos
if decision != "aceptar":
    print("\n--- FASE 5: El Nuevo Legado ---")
    print("Entras a la iglesia y buscas el libro de registros de viajeros...")

    # Modo "a" (append) añade texto al final sin destruir lo anterior
    with open("registro_sobrevivientes.txt", "a", encoding="utf-8") as archivo_registro:
        archivo_registro.write(f"SOBREVIVIENTE: {nombre_viajero}\n")
        archivo_registro.write(f"Me ofreció {monedas_ofrecidas} monedas. Rechacé y corrí con todas mis fuerzas.\n")
        archivo_registro.write("-" * 30 + "\n")

    print("Has dejado tu registro para las futuras generaciones.")
    print("Verifica el explorador de archivos para ver el 'registro_sobrevivientes.txt'.")