import RPi.GPIO as GPIO
import cv2
from Controle_Rodas import ControleRodas
from sensorProximidade import SensorProximidade 
from picamera2 import Picamera2
import time

COR_VERMELHO = (0, 0, 255)
COR_VERDE = (0, 255, 0)
COR_AZUL = (255, 0, 0)

class Rastreamento_Peixe:

    def __init__(self):
        self.kernel_size = (5, 5)
        self.epsilon_multiplicador = 0.001
        self.LIMITE_INFERIOR = (90, 50, 50)
        self.LIMITE_SUPERIOR = (130, 255, 255)
        
        # Criando os sensores de proximidade
        self.SensorProximidade1 = SensorProximidade(trig=6, echo=5)  # Sensor 1
        self.SensorProximidade2 = SensorProximidade(trig=20, echo=21)  # Sensor 2 (Novo)

        self.ControleRodas = ControleRodas()

    def definir_limites_cor(self, limite_inferior, limite_superior):
        self.LIMITE_INFERIOR = limite_inferior
        self.LIMITE_SUPERIOR = limite_superior

    def linearizar_frame(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.LIMITE_INFERIOR, self.LIMITE_SUPERIOR)
        black_result = cv2.bitwise_and(frame, frame, mask=mask)
        gray_frame = cv2.cvtColor(black_result, cv2.COLOR_BGR2GRAY)
        gaus_frame = cv2.GaussianBlur(gray_frame, self.kernel_size, 0)
        _, frame_binario = cv2.threshold(gaus_frame, 0, 255, cv2.THRESH_BINARY)
        pixel_preenchimento = cv2.getStructuringElement(cv2.MORPH_CROSS, self.kernel_size)
        return cv2.morphologyEx(frame_binario, cv2.MORPH_CLOSE, pixel_preenchimento)

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

    def desenha_grade(self, frame):
        h, w, _ = frame.shape
        for i in range(1, 3):
            cv2.line(frame, (0, h * i // 3), (w, h * i // 3), COR_VERDE, 2)
            cv2.line(frame, (w * i // 3, 0), (w * i // 3, h), COR_VERDE, 2)

    def mover_carro(self, frame, contorno):
        h, w, _ = frame.shape
        if contorno is not None:
            x_central, y_central = self.calcular_centro_contorno(contorno)
            x1, x2 = w // 3, 2 * w // 3
            y1, y2 = h // 3, 2 * h // 3

            # Verificando a distância dos dois sensores
            distancia1 = self.SensorProximidade1.medir_distancia()
            distancia2 = self.SensorProximidade2.medir_distancia()
            print(f"Distância Sensor 1: {distancia1:.2f} cm | Distância Sensor 2: {distancia2:.2f} cm")

            if distancia1 < 30 or distancia2 < 30:
                print("Obstáculo detectado! Parando.")
                self.ControleRodas.Parar()
            else:
                if y1 < y_central < y2:
                    if x1 < x_central < x2:
                        self.ControleRodas.Parar()
                    elif x_central >= x2:
                        self.ControleRodas.Re()
                    else:
                        self.ControleRodas.Frente()
                elif y_central >= y2:
                    if x1 < x_central < x2:
                        self.ControleRodas.Direita()
                    elif x_central >= x2:
                        self.ControleRodas.DI_Direita()
                    else:
                        self.ControleRodas.DS_Direita()
                else:
                    if x1 < x_central < x2:
                        self.ControleRodas.Esquerda()
                    elif x_central >= x2:
                        self.ControleRodas.DI_Esquerda()    
                    else:
                        self.ControleRodas.DS_Esquerda()

    def calcular_centro_contorno(self, contorno):
        M = cv2.moments(contorno)
        if M["m00"] != 0:
            return int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
        return None

    def loop(self):
        picam2 = Picamera2()
        picam2.configure(picam2.create_preview_configuration(main={"format":'XRGB8888', "size":(640,480)}))
        picam2.start()

        try:
            while True:
                frame = picam2.capture_array()
                frame_binario = self.linearizar_frame(frame)
                contornos, _ = cv2.findContours(frame_binario, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                contorno_principal = max(contornos, key=self.calcular_area_contorno) if contornos else None
                self.mover_carro(frame, contorno_principal)
                self.tracking_peixe(frame, frame_binario)
                cv2.imshow('BINARIO', frame_binario)
                cv2.imshow('PRINCIPAL', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário. Encerrando...")
        finally:
            picam2.stop()
            cv2.destroyAllWindows()
            GPIO.cleanup()

if __name__ == '__main__':
    tracker = Rastreamento_Peixe()
    tracker.loop()