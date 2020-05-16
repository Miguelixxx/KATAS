"""
Escribir un programa que almacene la cadena
"""


password = "contraseña"
password_del_usuario = input("Introduzca la contraseña: ")

if password == password_del_usuario:
        print("El password es correcto")
else:
    print("El password no coincide")