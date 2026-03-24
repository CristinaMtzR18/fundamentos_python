import pandas as pd

def cargar_datos(ruta_aspirantes, ruta_secreto):
    """
    Paso 1: Abre la Mente.
    Carga los archivos CSV y los convierte en DataFrames.
    """
    print("Cargando los registros del Valle de la Paz...")
    df_guerreros = pd.read_csv(ruta_aspirantes)
    df_rollo = pd.read_csv(ruta_secreto)
    return df_guerreros, df_rollo

def evaluar_sincronia(df_guerreros, df_rollo):
    """
    Paso 2 y 3: El Combate y El Veredicto.
    Compara las técnicas usadas contra el secreto del Rollo del Dragón.
    """
    print("Evaluando sincronía con el universo...")
    
    # Creamos una lista vacía para ir guardando los puntos de cada guerrero
    puntuaciones_totales = []
    
    # Iteramos fila por fila a través del DataFrame de los guerreros
    for index, fila_guerrero in df_guerreros.iterrows():
        puntos = 0
        
        # Iteramos a través de las 5 pruebas (Prueba1 a Prueba5)
        for prueba_num in range(1, 6):
            nombre_prueba = f'Prueba{prueba_num}'
            
            # Obtenemos la técnica que usó este guerrero en esta prueba
            tecnica_usada = fila_guerrero[nombre_prueba]
            
            # Buscamos en el df_rollo cuál era la técnica perfecta para esa prueba
            # .loc filtra la fila donde la columna 'Prueba' coincida, y extraemos el valor de 'Tecnica_Perfecta'
            tecnica_perfecta = df_rollo.loc[df_rollo['Prueba'] == nombre_prueba, 'Tecnica_Perfecta'].values[0]
            
            # Comparamos. Si son iguales, gana 1 punto de Paz Interior
            if tecnica_usada == tecnica_perfecta:
                puntos += 1
                
        # Guardamos el total de puntos de este guerrero en la lista
        puntuaciones_totales.append(puntos)
    
    # Asignamos la lista completa como una nueva columna en nuestro DataFrame
    df_guerreros['Puntos_Paz_Interior'] = puntuaciones_totales
    
    return df_guerreros

def generar_reporte(df_resultados, ruta_salida):
    """
    Paso 4: El Legado.
    Guarda los resultados finales en un nuevo archivo CSV.
    """
    # Guardamos en CSV sin incluir el índice numérico
    df_resultados.to_csv(ruta_salida, index=False)
    print(f"\n¡El veredicto ha sido sellado! Archivo guardado en: '{ruta_salida}'")
    
    # Mostramos un resumen rápido en consola ordenado por los mejores
    print("\n--- RESUMEN DEL TORNEO ---")
    resumen = df_resultados[['Guerrero', 'Puntos_Paz_Interior']].sort_values(by='Puntos_Paz_Interior', ascending=False)
    print(resumen.to_string(index=False))
    
    # Anunciamos al ganador
    ganador = resumen.iloc[0]['Guerrero']
    print(f"\n¡El Maestro Oogway ha hablado! El Guerrero Dragón es: {ganador}")

# --- FLUJO PRINCIPAL DE EJECUCIÓN ---
if __name__ == "__main__":
    # Definimos los nombres de nuestros archivos
    archivo_aspirantes = "movimientos_aspirantes.csv"
    archivo_secreto = "secreto_rollo.csv"
    archivo_salida = "eleccion_guerrero_dragon.csv"
    
    try:
        # Ejecutamos las funciones en orden
        df_aspirantes, df_clave = cargar_datos(archivo_aspirantes, archivo_secreto)
        df_evaluado = evaluar_sincronia(df_aspirantes, df_clave)
        generar_reporte(df_evaluado, archivo_salida)
        
    except FileNotFoundError:
        print("\n[Error] ¡Alguien robó los pergaminos! Asegúrate de que los archivos CSV existan en la misma carpeta.")