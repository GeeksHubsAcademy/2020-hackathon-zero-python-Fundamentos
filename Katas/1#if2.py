'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de 
forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario 
la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''
edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")