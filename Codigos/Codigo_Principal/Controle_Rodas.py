import RPi.GPIO as GPIO
from motor import Motor
import time

pino_motor_1_E = 17
pino_motor_2_E = 27
pino_motor_1_D = 23
pino_motor_2_D = 24
pino_ENA = 4
pino_ENB = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motor_direito = Motor(pino_motor_1_D, pino_motor_2_D, pino_ENB)
motor_esquerdo = Motor(pino_motor_1_E, pino_motor_2_E, pino_ENA, pino_ENA)

class ControleRodas:
    def Direita():
        print("Virando para direita")
        motor_direito.frente()
        motor_esquerdo.re()

    def Esquerda():
        print("Virando para esquerda")
        motor_direito.re()
        motor_esquerdo.frente()

    def Frente():
        print("Andando para frente")
        motor_direito.frente()
        motor_esquerdo.frente()

    def Re():
        print("Dando re")
        motor_direito.re()
        motor_esquerdo.re()

    def Parar():
        print("Parando")
        motor_direito.parar()
        motor_esquerdo.parar()

    def Freiar():
        print("Freiando")
        motor_direito.freiar()
        motor_esquerdo.freiar()
    
    def DS_Direita():
        print("Andando na diagonal superior direita")
        motor_direito.frente()
        motor_esquerdo.frente_reduzido()

    def DS_Esquerda():
        print("Andando na diagonal superior esquerda")
        motor_direito.frente_reduzido()
        motor_esquerdo.frente()

    def DI_Direita():
        print("Andando na diagonal inferior direita")
        motor_direito.re_reduzido()
        motor_esquerdo.re()

    def DI_Esquerda():
        print("Andando na diagonal inferior esquerda")
        motor_direito.re()
        motor_esquerdo.re_reduzido

#try:
#    while True:
#         Frente()
#         time.sleep(5)
#        
#         Direita()
#         time.sleep(5)
#        
#         Esquerda()
#         time.sleep(5)
#        
#         Re()
#         time.sleep(5)
#        
#         Parar()
#         time.sleep(5)
#except KeyboardInterrupt:
#    Parar()
#    GPIO.cleanup()
