"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al 
usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide 
con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")