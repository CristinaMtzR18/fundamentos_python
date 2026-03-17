"""
LA LEYENDA DEL CHARRO NEGRO

Objetivo: Aplicar conceptos de fundamentos de programación (variables, operadores, 
condicionales, ciclos) y consolidar el aprendizaje de Manejo de Archivos en Python 
(Lectura r, Escritura w y Anexo a).

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

# --- Tu Código Fase 0 ---



# ==============================================================================
# FASE 1: El Encuentro (Variables, Constantes y Operadores)
# ==============================================================================
# El Charro Negro se acerca y te ofrece una pesada bolsa de oro.
#
# INSTRUCCIONES:
# 1. Declara una constante PRECIO_ALMA con el valor de 10000 (entero).
# 2. Declara una variable monedas_ofrecidas con un valor de 6000 (entero).
# 3. Declara una variable nombre_viajero con tu nombre (string).
# 4. Usa un operador matemático para calcular el deficit (cuánto oro falta para 
#    que valga lo mismo que tu alma).
# 5. Usa un operador relacional para crear un booleano oferta_alta que sea True 
#    si las monedas ofrecidas son mayores o iguales a 5000.

# --- Tu Código Fase 1 ---



# ==============================================================================
# FASE 2: El Mensaje del Pasado (Manejo de Archivos - LECTURA)
# ==============================================================================
# Antes de responderle al Charro, notas un papel clavado en un viejo árbol seco 
# con un cuchillo oxidado. Decides leerlo.
#
# INSTRUCCIONES:
# 1. Utiliza open() con el administrador de contexto with para abrir 
#    "nota_arbol.txt" en modo lectura ("r").
# 2. Extrae el contenido usando el método .read() y guárdalo en una variable 
#    llamada advertencia_leida.
# 3. Imprime el contenido en la consola para saber qué hacer.

# --- Tu Código Fase 2 ---


# Lectura del archivo hacia la RAM



# ==============================================================================
# FASE 3: La Decisión (Estructuras de Control - If, Elif, Else)
# ==============================================================================
# El Charro Negro extiende su mano huesuda esperando tu respuesta. Combinarás 
# la advertencia que leíste con operadores lógicos (and, or).
#
# INSTRUCCIONES:
# 1. Declara una variable decision y asígnale el valor "rechazar".
# 2. Crea una estructura condicional múltiple (if-elif-else):
#    - Si la decisión es "aceptar" y oferta_alta es True: Imprime "Ignoraste 
#      la nota. El Charro ríe y tu alma se desvanece."
#    - Si la decisión es "rechazar": Imprime "Le das la espalda al oro y 
#      comienzas a correr."
#    - De lo contrario (else): Imprime "Te quedas paralizado. El caballo 
#      relincha impaciente."

# --- Tu Código Fase 3 ---



# ==============================================================================
# FASE 4: La Huida en la Noche (Ciclos while y for)
# ==============================================================================
# El Charro Negro se enfurece por tu rechazo y comienza a perseguirte. Debes 
# sobrevivir al camino mientras tu energía disminuye.
#
# INSTRUCCIONES:
# 1. Crea un ciclo for que represente 3 horas de carrera (ej. range(1, 4)). 
#    Imprime "Sobreviviendo la hora {hora}...".
# 2. Declara energia = 100.
# 3. Crea un ciclo while que simule tu huida. Mientras tu energia > 0, 
#    disminúyela de 30 en 30 (-=).
# 4. Agrega un if simple dentro del while: si la energía es menor a 30, 
#    imprime "¡Alerta! Casi no puedes respirar...".

# --- Tu Código Fase 4 ---



# ==============================================================================
# FASE 5: El Nuevo Legado (Manejo de Archivos - ESCRITURA Y ANEXO)
# ==============================================================================
# Has sobrevivido. Llegas a la iglesia y decides dejar tu propia advertencia 
# para ayudar a crear una "base de datos" de sobrevivientes usando el modo Anexo ("a").
#
# INSTRUCCIONES:
# 1. Utiliza with open() para abrir un archivo llamado "registro_sobrevivientes.txt".
# 2. ¡OJO! Ábrelo en modo anexo ("a") para que los registros anteriores no se borren.
# 3. Escribe en el archivo usando .write() tu nombre, la cantidad que te ofreció 
#    y que lograste escapar. Agrega \n al final.

# --- Tu Código Fase 5 ---
