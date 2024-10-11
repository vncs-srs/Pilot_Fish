import cv2
from Rastreamento_Peixe import Rastreamento_Peixe
from Controle_Rodas import ControleRodas

class Deteccao_Preto:
    def __init__(self):
        # Inicializa o rastreador de peixe
        self.rastreador = Rastreamento_Peixe()

    def loop(self):
        # Captura de vídeo da webcam
        webcam = cv2.VideoCapture(0)
        webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Define a largura do frame
        webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Define a altura do frame
        webcam.set(cv2.CAP_PROP_FPS, 30)             # Define a taxa de quadros por segundo

        while True:
            valido, frame = webcam.read()  # Lê o frame da webcam
            if valido:
                # Processa o frame para detectar o peixe
                frame_binario = self.rastreador.linearizar_frame(frame)
                
                # Chama o método para rastrear o peixe e desenhar no frame
                self.rastreador.tracking_peixe(frame, frame_binario)

                # Exibe os frames processados
                cv2.imshow('BINARIO', frame_binario)  # Mostra o frame binário
                cv2.imshow('PRINCIPAL', frame)        # Mostra o frame original

                # Encerra o loop se uma tecla for pressionada
                if cv2.waitKey(1) != -1:
                    break
            else:
                break  # Se não há frame válido, sai do loop

        # Libera a webcam e fecha todas as janelas ao final
        webcam.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    # Inicia o processo de detecção de peixe
    detecao = Deteccao_Preto()
    detecao.loop()  # Chama o loop principal

