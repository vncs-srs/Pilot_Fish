import cv2
from Rastreamento_Peixe import Rastreamento_Peixe
#from Controle_Rodas import ControleRodas

class CarrinhoControlado:
    def __init__(self):
        self.rastreador = Rastreamento_Peixe()

    def mover_carro(self, x_central, y_central, largura_frame, altura_frame):
        # Defina as coordenadas dos limites para cada direção
        x1, x2 = largura_frame // 3, 2 * largura_frame // 3
        y1, y2 = altura_frame // 3, 2 * altura_frame // 3

        # Lógica para movimentar o carro com base na posição do peixe
        if y1 < y_central < y2:
            if x1 < x_central < x2:
               # ControleRodas.Parar()
                print("Fique parado")
            elif x_central >= x2:
               # ControleRodas.Esquerda()
                print("Ande para a esquerda")
            else:  # x_central <= x1
               # ControleRodas.Direita()
                print("Ande para a direita")
        elif y_central >= y2:
            if x1 < x_central < x2:
                print("Ande para cima")
            elif x_central >= x2:
                print("Ande para cima e para a esquerda")
            else:  # x_central <= x1
                print("Ande para cima e para a direita")
        else:  # y_central <= y1
            if x1 < x_central < x2:
                print("Ande para baixo")
            elif x_central >= x2:
                print("Ande para baixo e para a esquerda")
            else:  # x_central <= x1
                print("Ande para baixo e para a direita")
        Rastreamento_Peixe.loop(self)
    #def controlar_carrinho(self, x_Central, y_Central, w_Frame, h_Frame):
        # Definir a lógica para controlar o carrinho com base na posição do objeto rastreado
    #    if x_Central < w_Frame / 3:
    #        self.Esquerda()
    #    elif x_Central > 2 * w_Frame / 3:
    #        self.Direita()
    #    else:
    #        self.Frente()



if __name__ == '__main__':
    carrinho = CarrinhoControlado()