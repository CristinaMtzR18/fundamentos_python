from datetime import datetime

def calculadora_antiguedad():
    print("--- Sistema de Cálculo de Antigüedad para Freelance / Administrativos ---")
    
    # Usamos un ciclo while True para mantener al usuario en un bucle 
    # hasta que ingrese un dato válido, evitando que el programa falle de golpe.
    while True:
        # Se solicita la fecha de ingreso
        fecha_ingreso = input("Ingresa tu fecha de ingreso (DD-MM-AAAA): ")
        
        # Validación 1: Evitar campos vacíos. 
        # El método .strip() elimina espacios en blanco al inicio y al final.
        if not fecha_ingreso.strip():
            print("Error: El campo no puede estar vacío. Intenta de nuevo.\n")
            continue 
            
        # Separamos la cadena de texto usando el guion como referencia
        # Esto nos devuelve una lista: ['DD', 'MM', 'AAAA']
        partes = fecha_ingreso.split('-')
        print(partes)
        # Validación 2: Asegurar que el formato tenga exactamente 3 partes
        if len(partes) != 3:
            print("Error: Formato incorrecto. Asegúrate de usar DD-MM-AAAA.\n")
            continue
            
        # Intentamos convertir los textos a números enteros
        try:
            dia = int(partes[0])
            mes = int(partes[1])
            anio = int(partes[2])
        except ValueError:
            print("Error: La fecha debe contener solo números.\n")
            continue
            
        # Validación 3: Reglas matemáticas para días, meses y años
        # Año actual dinámico para validar que no sea una fecha en el futuro
        anio_actual = 2026 
        
        if dia < 1 or dia > 31:
            print("Error: Día inválido. Debe estar entre 1 y 31.\n")
            continue
        if mes < 1 or mes > 12:
            print("Error: Mes inválido. Debe estar entre 1 y 12.\n")
            continue
        if anio < 2000 or anio > anio_actual:
            print(f"Error: Año inválido. Debe ser entre 2000 y {anio_actual}.\n")
            continue
            
        # --- Lógica de cálculo de antigüedad ---
        hoy = datetime.now()
        
        # Calculamos la diferencia de años inicial
        antiguedad = hoy.year - anio
        
        # El mayor reto: verificar si ya pasó el aniversario este año.
        # Comparamos tuplas (mes, dia). Si la fecha actual es menor a la de ingreso,
        # significa que aún no cumple el año, por lo que restamos 1.
        if (hoy.month, hoy.day) > (mes, dia):
            antiguedad -= 1
            
        # Validación extra: por si el año es el actual pero el mes/día está en el futuro
        if antiguedad < 0:
            print("Error: La fecha de ingreso no puede estar en el futuro.\n")
            continue
            
        # Resultados
        print(f"\nFecha procesada con éxito. Antigüedad calculada: {antiguedad} años.")
        if antiguedad < 1:
            print("Estado: ¡El colaborador es elegible para el bono anual!")
        else:
            print("Estado: Aún no cumple el año mínimo para el bono.")
            
        break

calculadora_antiguedad()