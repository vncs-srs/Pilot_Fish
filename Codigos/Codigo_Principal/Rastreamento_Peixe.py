import cv2
from Controle_Rodas import ControleRodas
from sensorProximidade import SensorProximidade

COR_VERMELHO = (0, 0, 255)
COR_VERDE = (0, 255, 0)
COR_AZUL = (255, 0, 0)


class Rastreamento_Peixe:

    def __init__(self):
        self.kernel_size = (5, 5)
        self.epsilon_multiplicador = 0.001
        self.LIMITE_INFERIOR = (90, 50, 50)
        self.LIMITE_SUPERIOR = (130, 255, 255)

    def definir_limites_cor(self, limite_inferior, limite_superior):
        self.LIMITE_INFERIOR = limite_inferior
        self.LIMITE_SUPERIOR = limite_superior

    def linearizar_frame(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        black_mask = cv2.inRange(hsv, self.LIMITE_INFERIOR, self.LIMITE_SUPERIOR)
        black_result = cv2.bitwise_and(frame, frame, mask=black_mask)
        gray_frame = cv2.cvtColor(black_result, cv2.COLOR_BGR2GRAY)
        gaus_frame = cv2.GaussianBlur(gray_frame, self.kernel_size, 0)
        _, frame_binario = cv2.threshold(gaus_frame, 0, 255, cv2.THRESH_BINARY)
        pixel_preenchimento = cv2.getStructuringElement(cv2.MORPH_CROSS, self.kernel_size)
        frame = cv2.morphologyEx(frame_binario, cv2.MORPH_CLOSE, pixel_preenchimento)
        return frame

    def calcular_area_contorno(self, contorno):
        return cv2.contourArea(contorno)

    def tracking_peixe(self, frame, frame_binario):
        contornos, _ = cv2.findContours(frame_binario, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if contornos:
            maior_contorno = max(contornos, key=self.calcular_area_contorno)
            self.desenha_grade(frame)
            self.desenha_tracking(frame, maior_contorno)

    def desenha_tracking(self, frame, contorno):
        hull = cv2.convexHull(contorno)
        cv2.drawContours(frame, [hull], -1, COR_AZUL, 1)
        M = cv2.moments(hull)
        if M["m00"] != 0:
            x_central = int(M["m10"] / M["m00"])
            y_central = int(M["m01"] / M["m00"])
            cv2.circle(frame, (x_central, y_central), 5, COR_VERMELHO, -1)
            cv2.drawContours(frame, [contorno], -1, (0, 255, 255), 1)
            texto = f"X: {x_central}, Y: {y_central}"
            cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

#    def rastreia_ponto(self, frame, contorno):
#        hull = cv2.convexHull(contorno)
#        cv2.drawContours(frame, [hull], -1, COR_AZUL, 1)
#        M = cv2.moments(hull)
#        x_Central = int(M["m10"] / M["m00"])
#        y_Central = int(M["m01"] / M["m00"])
#        return x_Central, y_Central
#
#    def desenha_tracking(self, frame, contorno):
#        x_Central, y_Central = self.rastreia_ponto(frame, contorno)
#        cv2.circle(frame, (x_Central, y_Central), 5, COR_VERMELHO, -1)
#        cv2.drawContours(frame, [contorno], -1, (0, 255, 255), 1)
#        texto = f"X: {x_Central}, Y: {y_Central}"
#        cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        
    def desenha_grade(self, frame):
        h_Frame, w_Frame, _ = frame.shape
        divisoes = 3
        for i in range(1, divisoes):
            y = int(i * h_Frame / divisoes)
            cv2.line(frame, (0, y), (w_Frame, y), COR_VERDE, 2)
        for i in range(1, divisoes):
            x = int(i * w_Frame / divisoes)
            cv2.line(frame, (x, 0), (x, h_Frame), COR_VERDE, 2)
            
    def mover_carro(self, frame, contorno):
        h_frame, w_frame, _ = frame.shape
        if contorno is not None:
            x_central, y_central = self.calcular_centro_contorno(contorno)
            # Defina as coordenadas dos limites para cada direção
            x1, x2 = w_frame // 3, 2 * w_frame // 3
            y1, y2 = h_frame // 3, 2 * h_frame // 3
            SensorProximidade(25, 8)
            # Verifique a distância do sensor de proximidade
            distancia = SensorProximidade.medir_distancia()
            print(f"Distância medida: {distancia:.2f} cm")

            # Limite de proximidade em centímetros
            limite_proximidade = 30

            if distancia < limite_proximidade:
                print("Muito próximo de um obstáculo, parando.")
                ControleRodas.Parar()
            else:
                # Lógica para movimentar o carro com base na posição do peixe
                if y1 < y_central < y2:
                    if x1 < x_central < x2:
                        #print("Fique parado")
                        ControleRodas.Parar()
                    elif x_central >= x2:
                        #print("Ande para baixo")
                        ControleRodas.Re()
                    else:  # x_central <= x1
                        #print("Ande para cima")
                        ControleRodas.Frente()
                elif y_central >= y2:
                    if x1 < x_central < x2:
                        #print("Ande para a direita")
                        ControleRodas.Direita()
                    elif x_central >= x2:
                        #print("Ande para baixo e para a direita")
                        ControleRodas.DI_Direita()
                    else:  # x_central <= x1
                        #print("Ande para cima e para a direita")
                        ControleRodas.DS_Direita
                else:  # y_central <= y1
                    if x1 < x_central < x2:
                        #print("Ande para a esquerda")
                        ControleRodas.Esquerda()
                    elif x_central >= x2:
                        #print("Ande para baixo e para a esquerda")
                        ControleRodas.DI_Esquerda()    
                    else:  # x_central <= x1
                        #print("Ande para cima e para a esquerda")
                        ControleRodas.DS_Esquerda()

    def calcular_centro_contorno(self, contorno):
        M = cv2.moments(contorno)
        if M["m00"] != 0:
            x_central = int(M["m10"] / M["m00"])
            y_central = int(M["m01"] / M["m00"])
            return x_central, y_central
        else:
            return None

    def loop(self):
        webcam = cv2.VideoCapture(0)
        webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        webcam.set(cv2.CAP_PROP_FPS, 30)

        while True:
            valido, frame = webcam.read()
            if valido:
                frame_binario = self.linearizar_frame(frame)
                contornos, _ = cv2.findContours(frame_binario, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                contorno_principal = max(contornos, key=self.calcular_area_contorno) if contornos else None
                self.mover_carro(frame, contorno_principal)
                self.tracking_peixe(frame, frame_binario)
                cv2.imshow('BINARIO', frame_binario)
                cv2.imshow('PRINCIPAL', frame)
                if cv2.waitKey(1) != -1:
                    break
            else:
                break
        webcam.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    tracker = Rastreamento_Peixe()
    tracker.loop()