# =====================================================================
# 1. CLASES, CONSTRUCTORES, ATRIBUTOS Y MÉTODOS
# =====================================================================
# Una clase es una plantilla o molde... El constructor inicializa los atributos

class MoldePastel:
    # CONSTRUCTOR: El método __init__ que se ejecuta al crear el objeto
    def __init__(self, sabor, forma):
        # ATRIBUTOS: Las características del pastel (Ingredientes/Datos)
        self.sabor = sabor
        self.forma = forma
        self.ingredientes = ["harina", "huevo", "leche"] # Lista por defecto

    # MÉTODO: Las acciones que el pastel puede hacer
    def hornear(self):
        print(f"Horneando un rico pastel de {self.sabor} en forma de {self.forma}.")

# --- EJERCICIO 1 ---
print("--- EJERCICIO 1: Clases y Objetos ---")
# Crea un OBJETO (instancia) llamado 'pastel_chocolate' usando el molde anterior.
# Ponle sabor "Chocolate" y forma "Estrella".
pastel_chocolate = MoldePastel("Chocolate", "Estrella")

# Llama al método hornear() de tu nuevo pastel.
pastel_chocolate.hornear()

# Agrega dos ingredientes más a la lista de atributos de tu pastel (como pediste antes):
pastel_chocolate.ingredientes.append("cacao en polvo")
pastel_chocolate.ingredientes.append("chispas")
print(f"Los ingredientes ahora son: {pastel_chocolate.ingredientes}\n")


# =====================================================================
# 2. ENCAPSULAMIENTO (GETTERS Y SETTERS CON DECORADORES)
# =====================================================================
# Proteger los datos internos... Python ofrece decoradores @property

class PastelSecreto:
    def __init__(self, sabor):
        self.sabor = sabor
        # Atributo PRIVADO (doble guion bajo). No se debe tocar desde afuera.
        self.__receta_secreta = "Vainilla con toque de canela"
    
    # GETTER: Permite LEER el valor privado de forma segura
    @property
    def receta(self):
        return f"La receta es: {self.__receta_secreta}"
    
    # SETTER: Permite MODIFICAR el valor privado validando que sea correcto
    @receta.setter
    def receta(self, nueva_receta):
        if len(nueva_receta) > 5: # Validación: que no esté vacía o sea muy corta
            self.__receta_secreta = nueva_receta
            print("¡Receta actualizada con éxito!")
        else:
            print("Error: La receta debe ser más larga y descriptiva.")

# --- EJERCICIO 2 ---
print("--- EJERCICIO 2: Encapsulamiento ---")
mi_pastel_secreto = PastelSecreto("Fresa")

# 1. Lee la receta usando el getter (nota que no usa paréntesis)
print(mi_pastel_secreto.receta)

# 2. Intenta poner una receta muy corta (fallará por la validación del setter)
mi_pastel_secreto.receta = "Sal" 

# 3. Pon una receta válida
mi_pastel_secreto.receta = "Fresa natural con crema batida especial"
print(mi_pastel_secreto.receta, "\n")


# =====================================================================
# 3. ABSTRACCIÓN
# =====================================================================
# Mostrar solo lo esencial y ocultar los detalles internos.

class MaquinaPasteles:
    def __init__(self):
        self.temperatura = 0
    
    # MÉTODOS INTERNOS (Ocultos al cliente, empiezan con un guion bajo)
    def _mezclar_masa(self):
        print("- Mezclando ingredientes a velocidad media...")
    
    def _precalentar_horno(self):
        self.temperatura = 180
        print(f"- Horno precalentado a {self.temperatura} grados.")
        
    # MÉTODO PÚBLICO (La abstracción: El cliente solo ve esto)
    def preparar_pedido(self, tipo_pastel):
        print(f"Iniciando preparación automática de: {tipo_pastel}")
        self._mezclar_masa()
        self._precalentar_horno()
        print("¡Pastel listo para entregar!")

# --- EJERCICIO 3 ---
print("--- EJERCICIO 3: Abstracción ---")
maquina = MaquinaPasteles()
# Como cliente, solo pides el pastel. 
# No necesitas llamar a _mezclar_masa() tú mismo, la máquina lo abstrae por ti.
maquina.preparar_pedido("Pastel de Zanahoria")
print("")


# =====================================================================
# 4. HERENCIA (SUPERCLASES Y SUBCLASES)
# =====================================================================
# Crear una nueva clase a partir de una existente... reutilizar código

# SUPERCLASE (Clase Padre)
class PastelBase:
    def __init__(self, sabor):
        self.sabor = sabor
        self.tamaño = "Mediano" # Por defecto
        
    def empaquetar(self):
        print(f"Empaquetando pastel de {self.sabor} en caja estándar.")

# SUBCLASE (Clase Hija) - Hereda de PastelBase
class Cupcake(PastelBase):
    def __init__(self, sabor, decoracion):
        # super() llama al constructor de la clase Padre
        super().__init__(sabor)
        self.tamaño = "Chico (Individual)"
        self.decoracion = decoracion # Atributo exclusivo de la subclase

# --- EJERCICIO 4 ---
print("--- EJERCICIO 4: Herencia ---")
# Crea un objeto de la subclase Cupcake
mi_cupcake = Cupcake("Vainilla", "Chispas de colores")

# Imprime el tamaño (heredado y modificado) y llama al método heredado
print(f"Mi postre es tamaño: {mi_cupcake.tamaño}")
print(f"Tiene decoración de: {mi_cupcake.decoracion}")
mi_cupcake.empaquetar() # Este método viene de la clase Padre
print("")


# =====================================================================
# 5. POLIMORFISMO (SOBRESCRITURA DE MÉTODOS)
# =====================================================================
# Diferentes objetos responden de manera distinta a un mismo método.

class PastelCircular(PastelBase):
    # Sobrescribimos un método (que imaginamos estaba en la base)
    def cortar(self):
        return "Cortando en rebanadas triangulares desde el centro. 🍕"

class PastelCuadrado(PastelBase):
    # Sobrescribimos el mismo método, pero hace algo distinto
    def cortar(self):
        return "Cortando en cuadrícula de 4x4 cuadritos perfectos. 🔲"

# --- EJERCICIO 5 ---
print("--- EJERCICIO 5: Polimorfismo ---")
pastel_redondo = PastelCircular("Limón")
pastel_cuadro = PastelCuadrado("Tres Leches")

# Tenemos una lista con diferentes objetos (formas)
vitrina_pasteles = [pastel_redondo, pastel_cuadro]

# Al recorrer la lista, llamamos al MISMO método (.cortar()), 
# pero cada objeto responde de forma diferente.
for pastel in vitrina_pasteles:
    print(f"El pastel de {pastel.sabor} se corta así: {pastel.cortar()}")