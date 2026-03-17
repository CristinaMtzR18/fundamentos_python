"""
LA LEYENDA DEL CHARRO NEGRO

Objetivo: Encontrar y reparar 5 errores sintácticos y 5 errores semánticos 
basándote en las instrucciones de cada fase.

Contexto:
Eres un viajero caminando solo por un camino de terracería en la noche. De pronto, 
escuchas el galope de un caballo. De las sombras emerge el Charro Negro, un ente 
que ofrece riquezas a cambio de un precio muy alto. Tus decisiones y tu lógica de 
programación decidirán tu destino.
"""

# ==============================================================================
# FASE 0: La Preparación del Entorno (Solo ejecuta esto una vez)
# ==============================================================================
# Para que nuestra historia funcione, simularemos que un viajero del pasado 
# dejó un mensaje en el bosque. Ejecuta este código primero para "crear" el 
# archivo en tu disco duro.

print("--- FASE 0: Preparando el entorno ---")

with open("nota_arbol.txt", "w" encoding="utf-8") as archivo:
    archivo.write("ADVERTENCIA PARA EL PRÓXIMO VIAJERO:\n")
    archivo.write("Si el Charro te ofrece 5000 monedas o más, es una trampa mortal.\n")
    archivo.write("Ignóralo y corre, no aceptes tratos.\n")
print("El archivo 'nota_arbol.txt' ha sido creado en la oscuridad del bosque...\n")


# ==============================================================================
# FASE 1: El Encuentro (Variables, Constantes y Operadores)
# ==============================================================================
# INSTRUCCIONES:
# 1. Declara una constante PRECIO_ALMA con el valor de 10000 (entero).
# 2. Declara una variable monedas_ofrecidas con un valor de 6000 (entero).
# 3. Declara una variable nombre_viajero con tu nombre (string).
# 4. Usa un operador matemático para calcular el deficit (cuánto oro falta para 
#    que valga lo mismo que tu alma).
# 5. Usa un operador relacional para crear un booleano oferta_alta que sea True 
#    si las monedas ofrecidas son mayores o iguales a 5000.

print("--- FASE 1: El Encuentro ---")
PRECIO_ALMA = 10000
monedas_ofrecidas = 6000
nombre_viajero = "TuNombre" 

# Calculando la diferencia
deficit = monedas_ofrecidas - PRECIO_ALMA 
oferta_alta = monedas_ofrecidas >= 5000

print(f"De las sombras, el Charro Negro le ofrece a {nombre_viajero} {monedas_ofrecidas} monedas de oro.")


# ==============================================================================
# FASE 2: El Mensaje del Pasado (Manejo de Archivos - LECTURA)
# ==============================================================================
# INSTRUCCIONES:
# 1. Utiliza open() con el administrador de contexto with para abrir 
#    "nota_arbol.txt" en modo lectura ("r").
# 2. Extrae el contenido usando el método .read() y guárdalo en una variable 
#    llamada advertencia_leida.
# 3. Imprime el contenido en la consola para saber qué hacer.

print("\n--- FASE 2: El Mensaje del Pasado ---")
print("Encuentras una nota clavada en un árbol. La abres temblando...")
print("-" * 40)

with open("nota_arbol.txt", "r", encoding="utf-8" as archivo:
    advertencia_leida = archivo.read()
    print(advertencia_leida, end="") 

print("-" * 40)


# ==============================================================================
# FASE 3: La Decisión (Estructuras de Control - If, Elif, Else)
# ==============================================================================
# INSTRUCCIONES:
# 1. Declara una variable decision y asígnale el valor "rechazar".
# 2. Crea una estructura condicional múltiple (if-elif-else):
#    - Si la decisión es "aceptar" y oferta_alta es True: Imprime "Ignoraste 
#      la nota. El Charro ríe y tu alma se desvanece."
#    - Si la decisión es "rechazar": Imprime "Le das la espalda al oro y 
#      comienzas a correr."
#    - De lo contrario (else): Imprime "Te quedas paralizado. El caballo 
#      relincha impaciente."

print("\n--- FASE 3: La Decisión ---")
decision = "rechazar" 

print(f'Tu decisión es: {decision.upper()}")

if decision = "aceptar" or oferta_alta:
    print("Ignoraste la nota. El Charro ríe siniestramente y tu alma se desvanece.")
elif decision == "rechazar":
    print("Le das la espalda al oro maldito y comienzas a correr hacia el pueblo.")
else
    print("Te quedas paralizado. El caballo relincha impaciente.")


# ==============================================================================
# FASE 4: La Huida en la Noche (Ciclos while y for)
# ==============================================================================
# INSTRUCCIONES:
# 1. Crea un ciclo for que represente 3 horas de carrera (ej. range(1, 4)). 
#    Imprime "Sobreviviendo la hora {hora}...".
# 2. Declara energia = 100.
# 3. Crea un ciclo while que simule tu huida. Mientras tu energia > 0, 
#    disminúyela de 30 en 30 (-=).
# 4. Agrega un if simple dentro del while: si la energía es menor a 30, 
#    imprime "¡Alerta! Casi no puedes respirar...".

if decision != "aceptar":
    print("\n--- FASE 4: La Huida en la Noche ---")
    print("¡Comienza la persecución!")

    for hora in range(1, 4):
        print(f"Corriendo en la hora {hora} de la madrugada...")

    energia = 100
    
    while energia < 0:
        print(f"  -> Energía restante: {energia}")
        energia += 30 
        
        if energia > 100:
            print("  -> ¡Alerta! Casi no puedes respirar, el galope suena muy cerca...")

    print("\n¡Ves a lo lejos las luces de la iglesia del pueblo! Estás a salvo.")


# ==============================================================================
# FASE 5: El Nuevo Legado (Manejo de Archivos - ESCRITURA Y ANEXO)
# ==============================================================================
# INSTRUCCIONES:
# 1. Utiliza with open() para abrir un archivo llamado "registro_sobrevivientes.txt".
# 2. ¡OJO! Ábrelo en modo anexo ("a") para que los registros anteriores no se borren.
# 3. Escribe en el archivo usando .write() tu nombre, la cantidad que te ofreció 
#    y que lograste escapar. Agrega \n al final.

if decision != "aceptar":
    print("\n--- FASE 5: El Nuevo Legado ---")
    print("Entras a la iglesia y buscas el libro de registros de viajeros...")

    with open("registro_sobrevivientes.txt", "a", encoding="utf-8") as archivo_registro:
        archivo_registro.write(f"SOBREVIVIENTE: {nombre_viajero}\n")
        archivo_registro.write(f"Me ofreció {monedas_ofrecidas} monedas. Rechacé y corrí con todas mis fuerzas.\n")
        archivo_registro.write("-" * 30 + "\n")

    print("Has dejado tu registro para las futuras generaciones.")