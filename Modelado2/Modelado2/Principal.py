from MiModelo.Mi_archivo import *
from MiModelo.Mi_modelo import *

m = MiArchivo()
lista_jugador = m.obtener_informacion()
lista_jugador = [l.split("|") for l in lista_jugador]

lista = []

for d in lista_jugador:
    p = Jugador(d[0],d[1],d[2],d[3])
    lista.append(p)



print(lista_jugador)

operacion = Operaciones(lista)
print("Por Nombre")
print(operacion.ordenar())
operacion2 = Operaciones(lista)
print("Por Campeonato")
print(operacion2.ordenar2())

