print("Adivina donde esta la reina de corazones")
cartas = [" ___   ___   ___", "|J  | |Q  | |8  |", "| ♦ | | ♥ | | ♣ |", "|__J| |__Q| |__8|"]


def funcion_jugar():
    nombre = input("> Por favor indique su nombre:")
    print(f"!{nombre} mantén tus ojos abiertos mientras las cartas se mueven¡")
    for i in cartas:
        print(i)
    print(f"Lo siento {nombre}, esta seccion aun esta en desarrollo")


def funcion_salir():
    print("Hasta luego")
    exit()


def funcion_tabla():
    print("Top 5 de lo(a)s mejores:\n\n")
    with open('Tabla.txt', 'r', encoding='utf-8') as tabla:
        for linea in tabla:
            print(linea)


def funcion_verificar_marcador(x):
    with open('Tabla.txt', 'r', encoding='utf-8') as tabla:
        for linea in tabla:
            print(linea)


while True:
    opcion = input("> Seleccione jugar [J], tabla de posiciones [T], salir [S]:")
    if opcion == "J" or opcion == "j":
        funcion_jugar()
    elif opcion == "S" or opcion == "s":
        funcion_salir()
    elif opcion == "T" or opcion == "t":
        funcion_tabla()
    else:
        print("Por favor ingrese un valor valido")
