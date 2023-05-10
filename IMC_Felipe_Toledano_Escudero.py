
# @GitHub F3LIP3X
# @author Felipe Toledano Escudero

usuarios = []

def agregar_usuario():
    nombre = input("Introduce tu nombre: ")
    while nombre == "":
        nombre = str(input("El nombre está vacío. Introduzca de nuevo el nombre del Usuario: "))

    altura = float(input("Introduce tu altura (en metros | 1.00): "))
    while altura == "":
        altura = float(input("La altura está vacía. Introduzca de nuevo la altura del Usuario: "))

    peso = float(input("Introduce tu peso (en kilogramos | 80.0): "))
    while peso == "":
        peso = float(input("El peso está vacío. Introduzca de nuevo el peso del Usuario: "))

    edad = int(input("Introduce tu edad: "))
    while edad == "":
        edad = int(input("La edad está vacía. Introduzca de nuevo la edad del Usuario: "))

    contraseña = input("Introduce tu contraseña: ")
    while contraseña == "":
        contraseña = 1234

    usuarios.append({"nombre": nombre, "altura": altura, "peso": peso, "edad": edad, "contraseña": contraseña, "permisos": False})

    print(f"El usuario {nombre} ha sido añadido correctamente.")

def print_name():
    print(f"Hola, {usuarios[indice]['nombre']}.")

def imc_Calcular():
    usuario_actual = usuarios[indice]
    imc = usuario_actual["peso"] / usuario_actual["altura"] ** 2
    print(f"Tu IMC es {imc:.2f}.")

    if imc >= 16 and imc < 18.5:
        print("Tu estado es de: Bajo Peso")
    elif imc > 18.5 and imc <= 25.0:
        print("Tu estado es: Normal") 
    elif imc > 25.0 and imc <= 40.0:
        print("Tu estado es de: Sobrepeso")
    else:
        print("SantaMariaMadreDeMiMadre")

def mayor_edad():
    if usuarios[indice]["edad"] >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

def consultar_usuarios():
    nombres_usuarios = [usuario["nombre"] for usuario in usuarios]
    print("Los usuarios del sistema son:")
    print("\n".join(nombres_usuarios))

def print_user():
    nombre = input("Introduce el nombre del usuario: ")
    user_find = None
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            user_find = usuario
            break

    if user_find is not None: 
        print(f"Nombre: {user_find['nombre']}")
        print(f"Altura: {user_find['altura']:.2f} m")
        print(f"Peso: {user_find['peso']} kg")
        print(f"Edad: {user_find['edad']}")
    else:
        print(f"No se ha encontrado ningún usuario con el nombre {nombre}.")

def exit():
    global ejecutarse
    ejecutarse = False

nombre = input("Introduce tu nombre: ")
while nombre == "":
    nombre = str(input("El nombre está vacío. Introduzca de nuevo el nombre del Usuario: "))

altura = float(input("Introduce tu altura (en metros | 1.00): "))
while altura == "":
    altura = float(input("La altura está vacía. Introduzca de nuevo la altura del Usuario: "))

peso = float(input("Introduce tu peso (en kilogramos | 80.0): "))
while peso == "":
    peso = float(input("El peso está vacío. Introduzca de nuevo el peso del Usuario: "))

edad = int(input("Introduce tu edad: "))
while edad == "":
    edad = int(input("La edad está vacía. Introduzca de nuevo la edad del Usuario: "))

contraseña = input("Introduce tu contraseña: ")
while contraseña == "":
    contraseña = 1234

usuarios.append({"nombre": nombre, "altura": altura, "peso": peso, "edad": edad, "contraseña": contraseña, "permisos": True})
indice = 0 
ejecutarse = True

def cambiar_usuario():
    global indice
    nombre_usuario = input("Introduce el nombre del usuario al que quieres cambiar: ")
    indice_user = -1
    for i, usuario in enumerate(usuarios):
        if usuario["nombre"] == nombre_usuario:
            indice_user = i
            break
    if indice_user != -1:
        indice = indice_user
        print(f"Has cambiado al usuario {nombre_usuario}.")
    else:
        print(f"No se encontró el usuario {nombre_usuario}.")

# Menú principal
while ejecutarse:
    print("\n***************************** Menú de Opciones *****************************")
    print("1. Nombre de usuario")
    print("2. Calcular IMC")
    print("3. Comprobar la mayoría de edad")
    print("4. Consultar los usuarios del sistema")
    print("5. Añadir nuevo usuario")
    print("6. Imprimir datos de un usuario concreto")
    print("7. Cambiar de usuario")
    print("8. Salir del programa")

    opcion = input("Introduce el número de opción que deseas ejecutar: ")

    if opcion == "1":
        print_name()
    elif opcion == "2":
        imc_Calcular()
    elif opcion == "3":
        mayor_edad()
    elif opcion == "4":
        consultar_usuarios()
    elif opcion == "5":
        agregar_usuario()
    elif opcion == "6":
        print_user()
    elif opcion == "7":
        cambiar_usuario()
    elif opcion == "8":
        exit()
    else:
        print("Opción inválida. Por favor, introduce un número del 1 al 7.")