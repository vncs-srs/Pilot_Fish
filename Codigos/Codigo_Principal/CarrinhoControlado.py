import cv2
from Rastreamento_Peixe import Rastreamento_Peixe
from Controle_Rodas import ControleRodas  # Importando ControleRodas para controlar os motores

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
                ControleRodas.Parar()  # Fique parado
                print("Fique parado")
            elif x_central >= x2:
                ControleRodas.DI_Esquerda()  # Mover diagonal esquerda para frente
                print("Andando na diagonal esquerda")
            else:  # x_central <= x1
                ControleRodas.DS_Direita()  # Mover diagonal direita para frente
                print("Andando na diagonal direita")
        elif y_central >= y2:
            if x1 < x_central < x2:
                ControleRodas.Frente()  # Ande para frente
                print("Andando para frente")
            elif x_central >= x2:
                ControleRodas.DI_Direita()  # Mover diagonal direita para trás
                print("Andando na diagonal direita")
            else:  # x_central <= x1
                ControleRodas.DI_Esquerda()  # Mover diagonal esquerda para trás
                print("Andando na diagonal esquerda")
        else:  # y_central <= y1
            if x1 < x_central < x2:
                ControleRodas.Re()  # Ande para trás
                print("Andando para trás")
            elif x_central >= x2:
                ControleRodas.DS_Direita()  # Mover diagonal direita para trás
                print("Andando na diagonal direita")
            else:  # x_central <= x1
                ControleRodas.DS_Esquerda()  # Mover diagonal esquerda para trás
                print("Andando na diagonal esquerda")

    def loop(self):
        self.rastreador.loop()  # Chamando o loop do rastreador

if __name__ == '__main__':
    carrinho = CarrinhoControlado()
    carrinho.loop()

