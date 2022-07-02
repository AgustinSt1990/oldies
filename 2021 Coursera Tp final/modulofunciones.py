import os

def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    return 2021-agno-1

def obtener_estatura():
    estatura = float(input("Cuanto mides? Damelo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    sexo = sexo.upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo

def obtener_pais():
    pais = input("Indica tu pais de nacimiento: ")
    return pais

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))
    return amigos

def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_num_amigos()
    return (n,e,em,ec,na)

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos):
    print ("--------------------------------------------------")
    print ("Nombre:   ", nombre)
    print ("Edad:     ", edad, "años")
    print ("Estatura: ", estatura_m, "m y ", estatura_cm, "centimetros")
    print ("Sexo:     ", sexo)
    print ("Pais:     ", pais)
    print ("Amigos:   ", num_amigos)
    print ("--------------------------------------------------")

def opcion_menu():
    print ("Acciones disponibles:")
    print ("  1. Escribir un mensaje publico")
    print ("  2. Escribir un mensaje solo a algunos amigos")
    print ("  3. Mostrar los datos de perfil")
    print ("  4. Actualizar el perfil de usuario")
    print ("  0. Salir")
    opcion = int(input("Ingresa una opcion: "))
    while opcion < 0 or opcion > 4:
        print ("No conozco la opcion que has ingresado. Intentalo otra vez.")
        opcion = int(input("Ingresa una opcion: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. Que piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print ("--------------------------------------------------")
    if destinatario == None:
        print (origen, "dice:", mensaje)
    else:
        print (origen, "dice:", "@"+destinatario, mensaje)
    print ("--------------------------------------------------")

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    sexo = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    num_amigos = int(archivo_usuario.readline())
    estado = archivo_usuario.readline().rstrip()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)

def escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(str(num_amigos)+"\n")
    archivo_usuario.write(estado+"\n")
    #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()