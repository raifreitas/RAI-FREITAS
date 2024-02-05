import random

def juego_adivinanza():
    print("¡Bienvenido al Juego de Adivinanzas!")
    
    # Genera un número aleatorio entre 1 y 100
    numero_a_adivinar = random.randint(1, 100)
    
    intentos_maximos = 7
    intentos_realizados = 0

    while intentos_realizados < intentos_maximos:
        intento = int(input("\nIntenta adivinar el número (entre 1 y 100): "))

        if intento == numero_a_adivinar:
            print(f"Felicidades, ¡has adivinado el número {numero_a_adivinar}!")
            break
        elif intento < numero_a_adivinar:
            print("El número es mayor. ¡Sigue intentando!")
        else:
            print("El número es menor. ¡Sigue intentando!")

        intentos_realizados += 1

    if intentos_realizados == intentos_maximos:
        print(f"\nLo siento, has agotado tus {intentos_maximos} intentos. El número a adivinar era {numero_a_adivinar}.")

# Iniciar el juego
juego_adivinanza()
