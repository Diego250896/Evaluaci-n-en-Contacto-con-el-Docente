#  1. Configuración inicial de jugadores
jugadores = []  # Lista que guardará las tuplas (numero, nombre)
contador_jugadores = 0

print("=== CONFIGURACIÓN DE JUGADORES ===")

while True:
    print(f"\nJugadores actuales en la lista: {jugadores}")
    print(f"Total de jugadores registrados: {contador_jugadores}")
    
    opcion = input("\n¿Qué deseas hacer? (1: Agregar / 2: Quitar / 3: Iniciar Juego): ")
    
    if opcion == "1":
        nombre = input("Ingresa el nombre del jugador: ").capitalize()
        contador_jugadores += 1
        # Creamos una tupla con el número y el nombre
        nuevo_jugador = (contador_jugadores, nombre)
        jugadores.append(nuevo_jugador)
        print(f"¡Jugador {nombre} agregado con el ID {contador_jugadores}!")
        
    elif opcion == "2":
        if len(jugadores) == 0:
            print("No hay jugadores para quitar.")
        else:
            nombre_quitar = input("Ingresa el nombre del jugador a quitar: ").capitalize()
            # Buscamos al jugador en la lista de tuplas
            encontrado = False
            for jugador in jugadores:
                if jugador[1] == nombre_quitar:
                    jugadores.remove(jugador)
                    print(f"Jugador {nombre_quitar} eliminado.")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró ningún jugador con ese nombre.")
                
    elif opcion == "3":
        if len(jugadores) == 0:
            print("¡Debes agregar al menos un jugador para comenzar!")
        else:
            print("\n¡Lista de juego cerrada!")
            break
    else:
        print("Opción no válida. Intenta de nuevo.")

# 2. Configuración del juego de palabras
print("\n" + "="*30)
palabra_secreta = input("Ingrese la palabra secreta para el juego: ").lower()
intentos_maximos = 5
contador_errores = 0
letras_adivinadas = []

print(f"\n¡El juego comienza! Participantes: {[j[1] for j in jugadores]}")
print(f"Tienes {intentos_maximos} oportunidades para fallar.")

# 3. Bucle principal
while contador_errores < intentos_maximos:
    print("\n" + "="*30)
    
    # Mostrar el progreso de la palabra
    palabra_completa = True
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            palabra_completa = False
            
    print("\n") 

    if palabra_completa:
        print("¡GANADORES! Han adivinado la palabra secreta.")
        break

    # Solicitar una letra al jugador
    letra_ingresada = input("Adivine una letra: ").lower()

    if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue

    if letra_ingresada in letras_adivinadas:
        print("Ya habías ingresado esa letra, intenta con otra.")
        
    elif letra_ingresada in palabra_secreta:
        print(f"¡Bien hecho! La letra '{letra_ingresada}' es correcta.")
        letras_adivinadas.append(letra_ingresada)
        
    else:
        contador_errores += 1
        print(f"Error número: {contador_errores}")
        print(f"Te quedan {intentos_maximos - contador_errores} oportunidades.")
        letras_adivinadas.append(letra_ingresada)

# 4. Fin del juego
if contador_errores == intentos_maximos:
    print("\nFin del juego. ¡Se han quedado sin oportunidades!")
    print(f"La palabra secreta era: {palabra_secreta}") 