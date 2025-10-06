#Planteamiento: 
#1. El programa permite registrar votos a diferentes candidatos.
#2. Se podrá votar varias veces (simulación de varios votantes).
#3. El usuario podrá cerrar la votación.
#4. Se mostrarán los votos de cada candidato.
#5. Se determinará el ganador (o si hay empate).

#Lógica del Algoritmo:
#1. Se inicializa un diccionario vacío para almacenar los votos.
#2. Se muestra un menú para votar o cerrar la votación.
#3. Al votar, se pide el nombre del candidato. Si ya existe, se suma 1 a sus votos; si no, se agrega con 1 voto.
#4. Cuando finaliza la votación, se imprime el total de votos por candidato.
#5. Se determina quién tiene más votos y se declara ganador o se informa de un empate.

# Definimos una función llamada sistema_votacion que contendrá todo el algoritmo.
def sistema_votacion():
    # Creamos un diccionario vacío para guardar los votos por candidato.
    votos = {}
    
    # Mostramos un mensaje de bienvenida
    print("=== Sistema Simple de Votación ===")
    
    # Bucle infinito que se repetirá hasta que el usuario decida finalizar
    while True:
        # Mostramos las opciones disponibles al usuario
        print("\nOpciones:")
        print("1. Votar")
        print("2. Finalizar votación")
        
        # Solicitamos al usuario que elija una opción
        opcion = input("Elige una opción (1 o 2): ")

        # Si elige "1", se procede a registrar un voto
        if opcion == "1":
            # Pedimos el nombre del candidato al que quiere votar
            candidato = input("Escribe el nombre del candidato: ").strip().title()
            # Verificamos que el nombre no esté vacío
            if candidato:
                # Si el candidato ya tiene votos, sumamos 1; si no, se crea con 1 voto
                votos[candidato] = votos.get(candidato, 0) + 1
                print(f"Voto registrado para {candidato}.")
            else:
                # Si el nombre está vacío, mostramos un error
                print("Nombre de candidato inválido.")
        
        # Si elige "2", se finaliza el proceso de votación
        elif opcion == "2":
            break  # Rompe el bucle y pasa a mostrar resultados
        
        # Si elige cualquier otra cosa, se muestra un mensaje de error
        else:
            print("Opción no válida. Intenta de nuevo.")
    
    # Verificamos si no se registraron votos
    if not votos:
        print("\nNo se registraron votos.")
        return  # Termina la función aquí
    
    # Mostramos los resultados de la votación
    print("\n Resultados de la votación ")
    # Recorremos el diccionario para mostrar cuántos votos tiene cada candidato
    for candidato, cantidad in votos.items():
        print(f"{candidato}: {cantidad} votos")
    
    # Calculamos el número máximo de votos obtenidos
    max_votos = max(votos.values())
    
    # Creamos una lista de ganadores (por si hay empate)
    ganadores = [c for c, v in votos.items() if v == max_votos]

    # Si hay solo un ganador
    if len(ganadores) == 1:
        print(f"\n El ganador es: {ganadores[0]} con {max_votos} votos.")
    else:
        # Si hay más de uno, es un empate
        print(f"\n Empate entre: {', '.join(ganadores)} con {max_votos} votos cada uno.")

# Llamamos a la función para ejecutar el programa
sistema_votacion()
