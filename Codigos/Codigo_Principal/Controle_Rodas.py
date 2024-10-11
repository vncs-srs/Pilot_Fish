import RPi.GPIO as GPIO
from motor import Motor

# Definição dos pinos
pino_motor_1_E = 17
pino_motor_2_E = 27
pino_pwm_E = 18  # Pino PWM para o motor esquerdo
pino_motor_1_D = 23
pino_motor_2_D = 24
pino_pwm_D = 25  # Pino PWM para o motor direito

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motor_direito = Motor(pino_motor_1_D, pino_motor_2_D, pino_pwm_D)
motor_esquerdo = Motor(pino_motor_1_E, pino_motor_2_E, pino_pwm_E)

class ControleRodas:
    @staticmethod
    def Direita():
        print("Virando para direita")
        motor_direito.frente()
        motor_esquerdo.re()

    @staticmethod
    def Esquerda():
        print("Virando para esquerda")
        motor_direito.re()
        motor_esquerdo.frente()

    @staticmethod
    def Frente():
        print("Andando para frente")
        motor_direito.frente()
        motor_esquerdo.frente()

    @staticmethod
    def Re():
        print("Dando ré")
        motor_direito.re()
        motor_esquerdo.re()

    @staticmethod
    def Parar():
        print("Parando")
        motor_direito.parar()
        motor_esquerdo.parar()

    @staticmethod
    def Freiar():
        print("Freiando")
        motor_direito.freiar()
        motor_esquerdo.freiar()

    @staticmethod
    def DS_Direita():
        print("Andando na diagonal superior direita")
        motor_direito.frente()
        motor_esquerdo.re()

    @staticmethod
    def DS_Esquerda():
        print("Andando na diagonal superior esquerda")
        motor_direito.re()
        motor_esquerdo.frente()

    @staticmethod
    def DI_Direita():
        print("Andando na diagonal inferior direita")
        motor_direito.re()
        motor_esquerdo.frente()

    @staticmethod
    def DI_Esquerda():
        print("Andando na diagonal inferior esquerda")
        motor_direito.frente()
        motor_esquerdo.re()

