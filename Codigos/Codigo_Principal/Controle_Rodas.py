import RPi.GPIO as GPIO
from motor import Motor
import time
from pwm import PWMControl

pino_motor_1_E = 17
pino_motor_2_E = 27
pino_motor_1_D = 23
pino_motor_2_D = 24

pino_pwm_E = 18
pino_pwm_D = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motor_direito = Motor(pino_motor_1_D, pino_motor_2_D)
motor_esquerdo = Motor(pino_motor_1_E, pino_motor_2_E)

pwm_direito = PWMControl(pino_pwm_D)
pwm_esquerdo = PWMControl(pino_pwm_E)

class ControleRodas:
        
    def Direita(velocidade=100):
        print("Virando para direita")
        motor_direito.re()
        motor_esquerdo.frente()
        
        pwm_direito.ajustar_velocidade(velocidade)
        pwm_esquerdo.ajustar_velocidade(velocidade)

    def Esquerda(velocidade=100):
        print("Virando para esquerda")
        motor_direito.frente()
        motor_esquerdo.re()
        
        pwm_direito.ajustar_velocidade(velocidade)
        pwm_esquerdo.ajustar_velocidade(velocidade)

    def Frente(velocidade=100):
        print("Andando para frente")
        motor_direito.frente()
        motor_esquerdo.frente()
        
        pwm_direito.ajustar_velocidade(velocidade)
        pwm_esquerdo.ajustar_velocidade(velocidade)

    def Re(velocidade=100):
        print("Dando re")
        motor_direito.re()
        motor_esquerdo.re()
        
        pwm_direito.ajustar_velocidade(velocidade)
        pwm_esquerdo.ajustar_velocidade(velocidade)

    def Parar():
        print("Parando")
        motor_direito.parar()
        motor_esquerdo.parar()
        
        pwm_direito.parar()
        pwm_esquerdo.parar()

    def Freiar():
        print("Freiando")
        motor_direito.freiar()
        motor_esquerdo.freiar()
        
        pwm_direito.finalizar()
        pwm_esquerdo.finalizar()
    
    def DS_Direita(velocidade=100):
        print("Andando na diagonal superior direita")
        motor_direito.frente()
        motor_esquerdo.frente()
        
        pwm_direito.ajustar_velocidade(velocidade/2)
        pwm_esquerdo.ajustar_velocidade(velocidade)

    def DS_Esquerda(velocidade=100):
        print("Andando na diagonal superior esquerda")
        motor_direito.frente()
        motor_esquerdo.frente()
        
        pwm_direito.ajustar_velocidade(velocidade)
        pwm_esquerdo.ajustar_velocidade(velocidade/2)

    def DI_Direita(velocidade=100):
        print("Andando na diagonal inferior direita")
        motor_direito.re()
        motor_esquerdo.re()
        
        pwm_direito.ajustar_velocidade(velocidade/2)
        pwm_esquerdo.ajustar_velocidade(velocidade)

    def DI_Esquerda(velocidade=100):
        print("Andando na diagonal inferior esquerda")
        motor_direito.re()
        motor_esquerdo.re()
        
        pwm_direito.ajustar_velocidade(velocidade)
        pwm_esquerdo.ajustar_velocidade(velocidade/2)

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
