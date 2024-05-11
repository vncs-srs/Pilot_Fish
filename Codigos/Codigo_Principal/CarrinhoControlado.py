import cv2
from Rastreamento_Peixe import Rastreamento_Peixe
from motor import Motor
from Controle_Rodas import pino_motor_1_D 
from Controle_Rodas import pino_motor_2_D 
from Controle_Rodas import pino_motor_1_E
from Controle_Rodas import pino_motor_2_E  

class CarrinhoControlado:
    def __init__(self):
        self.rastreador = Rastreamento_Peixe()
        self.motor_direito = Motor(pino_motor_1_D, pino_motor_2_D)
        self.motor_esquerdo = Motor(pino_motor_1_E, pino_motor_2_E)

    def controlar_carrinho(self, x_Central, y_Central, w_Frame, h_Frame):
        # Definir a lógica para controlar o carrinho com base na posição do objeto rastreado
        if x_Central < w_Frame / 3:
            self.Esquerda_vira()
        elif x_Central > 2 * w_Frame / 3:
            self.Direita_vira()
        else:
            self.Frente()

    def loop(self):
        webcam = cv2.VideoCapture(0)
        webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        webcam.set(cv2.CAP_PROP_FPS, 30)

        while True:
            valido, frame = webcam.read()
            if valido:
                frame_binario = self.rastreador.linearizar_frame(frame)
                x_Central, y_Central, w_Frame, h_Frame = self.rastreador.trancking_peixe(frame, frame_binario)
                self.controlar_carrinho(x_Central, y_Central, w_Frame, h_Frame)
                cv2.imshow('BINARIO', frame_binario)
                cv2.imshow('PRINCIPAL', frame)
                if cv2.waitKey(1) != -1:
                    break
            else:
                break
        webcam.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    carrinho = CarrinhoControlado()
    carrinho.loop()