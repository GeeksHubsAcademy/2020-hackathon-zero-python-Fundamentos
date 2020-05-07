'''
    Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
    triángulo rectángulo como el de más abajo, de altura el número introducido.

    *
    **
    ***
    ****
    *****
'''

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))