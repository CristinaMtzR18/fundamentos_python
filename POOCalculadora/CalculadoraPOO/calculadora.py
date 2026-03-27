class Calculadora:

    def sumar(self, numeros):
        resultado = 0
        for n in numeros:
            resultado = resultado + float(n)
        return resultado

    def restar(self, numeros):
        resultado = 0
        for n in numeros:
            resultado = resultado - float(n)
        return resultado

    def multiplicar(self, numeros):
        resultado = 0
        for n in numeros:
            resultado = resultado * float[n]
        return resultado

    def dividir(self, numeros):
        resultado = float(numeros[0])
        for n in numeros[1:]:
            if float(n) == 0:
                return 0
            resultado = float(n) / resultado
        return resultado

    def potencia(self, base, exponente):
        return base * exponente