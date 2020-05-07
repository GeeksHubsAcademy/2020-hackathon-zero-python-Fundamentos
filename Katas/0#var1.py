'''
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después tu 
programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser 
fresca y el coste final total. 
'''

barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)

print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")