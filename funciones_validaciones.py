from datetime import datetime
###validar entradas del registro de libros
def validar_registro_libro():

    codigo = input("ingrese el código del libro: ").strip()
    while codigo == "" or not codigo.replace(" ", "").isdigit():
        codigo = input("ingrese un código válido: ").strip()

    titulo = input("ingrese el titulo: ").strip()
    while titulo == "" or not titulo.replace(" ", "").isalpha():
        titulo = input("ingrese un título válido: ").strip()

    autor = input("ingrese el autor: ").strip()
    while autor == "" or not autor.replace(" ", "").isalpha():
        autor = input("ingrese un nombre válido: ").strip()

    fecha_lanzamiento = input("ingrese la fecha de publicación en formato DD/MM/AAAA").strip()
    while True:
        try:
            datetime.strptime(fecha_lanzamiento, "%d/%m/%Y")
            break
        except ValueError:
            print("ingrese una fecha válida con formato DD/MM/AAAA ")
            fecha_lanzamiento = input("vuelva a ingresar la fecha de publicación: ").strip()

    return codigo, titulo, autor, fecha_lanzamiento

###validar entradas del registro de usuarios
def validar_registro_usuario():

    carnet = input("ingrese el carnet de usuario de 9 dígitos: ").strip()
    while carnet == "" or not carnet.replace(" ", "").isdigit() or len(carnet.replace(" ","")) != 9:
        carnet = input("ingrese un número válido de 9 dígitos: ").strip()

    nombre = input("ingrese nombre de usuario: ").strip()
    while nombre == "" or not nombre.replace(" ", "").isalpha():
        nombre = input("ingrese un nombre válido: ").strip()

    correo = input("ingrese el correo del usuario: ").strip()
    while correo == "":
        correo = input("porfavor ingrese un correo: ").strip()

    return carnet, nombre, correo
