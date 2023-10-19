from classes import *

b = Bola('azul', 10, "plastico")

print(b.cor)
print(b.circunferencia)
print(b.mostrarMaterial())

b.cor = 'amarela'
b.circunferencia = 20
b.__material = 'madeira'

print(b.mostrarMaterial())

