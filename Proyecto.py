print("Adivina donde esta la reina de corazones")

def funcion_jugar():
    nombre = input("Por favor indique su nombre:")
    print(f"hola {nombre}, esta seccion aun esta en desarrollo")
  
def funcion_salir():
    print("Hasta luego")
    exit()

def funcion_tabla():
    print("Top 5 de lo(a)s mejores:", end = "\n\n")
    with open('Tabla.txt', 'r', encoding='utf-8') as tabla:
        for linea in tabla:
            print(linea)
def funcion_verificar_marcador(x):
    with open('Tabla.txt', 'r', encoding='utf-8') as tabla:
          for linea in tabla:
              print(linea)

while True: 
  opcion  = input("Seleccione jugar [J], tabla de posiciones [T], salir [S]:")
  if opcion == "J":
    funcion_jugar()
  elif opcion == "S":
    funcion_salir()
  elif opcion == "T":
    funcion_tabla()
  