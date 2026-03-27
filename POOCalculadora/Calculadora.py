#Practica de calculadora basica con POO. INFOTEC. Curso FDP
#operaciones: sumar, restar, multiplicar, division
class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: no se puede dividir entre cero"
        return a / b


# Crear objeto
calc = Calculadora()

# Menú principal
while True:
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion in ['1', '2', '3', '4']:

        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            resultado = calc.sumar(a, b)

        elif opcion == '2':
            resultado = calc.restar(a, b)

        elif opcion == '3':
            resultado = calc.multiplicar(a, b)

        elif opcion == '4':
            resultado = calc.dividir(a, b)

        print("Resultado:", resultado)

    elif opcion == '5':
        print("Saliendo...")
        break

    else:
        print("Opción no válida")