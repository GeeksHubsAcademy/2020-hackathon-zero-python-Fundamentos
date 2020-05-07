'''
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
'''

def circle_area(radius):
    """Función que calcula el area de un círculo.
    Parámetros
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius. 
    """
    pi = 3.1415
    return 2*pi*radius**2

def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return circle_area(radius)*high

print(cilinder_volume(3,5))