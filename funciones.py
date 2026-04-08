class mangos:
    def __init__(self, vidas, puntos):
        self.vidas = vidas
        self.puntos = puntos
mangus7 = mangos(7, 0)
gameover = False
if mangus7.vidas <= 0:
    gameover = True
if gameover == True:
    print("Game Over")
else:    
    print("Sigue jugando")

class movimiento:
    def __init__(self, direccion):
        self.direccion = direccion
movimiento1 = movimiento("derecha")
movimiento2 = movimiento("izquierda")
movimiento3 = movimiento("arriba")
movimiento4 = movimiento("abajo")
movimiento1.usekey = "a"
movimiento2.usekey = "d"
movimiento3.usekey = "w"
movimiento4.usekey = "s"
print("Movimiento 1: ", movimiento1.direccion, "tecla: ", movimiento1.usekey)
print("Movimiento 2: ", movimiento2.direccion, "tecla: ", movimiento2.usekey)
print("Movimiento 3: ", movimiento3.direccion, "tecla: ", movimiento3.usekey)
print("Movimiento 4: ", movimiento4.direccion, "tecla: ", movimiento4.usekey)
move = input("a donde quieres moverte? ")
if move == movimiento1.usekey:
    print("Te has movido a la ", movimiento1.direccion)
elif move == movimiento2.usekey:
    print("Te has movido a la ", movimiento2.direccion)
elif move == movimiento3.usekey:
    print("Te has movido a la ", movimiento3.direccion)
elif move == movimiento4.usekey:
    print("Te has movido a la ", movimiento4.direccion)
else:
    print("Tecla no valida")