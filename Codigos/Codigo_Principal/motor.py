import RPi.GPIO as GPIO
from PWM import PWM

class Motor:
    def __init__(self, p1, p2, p_pwm):
        self.pino_1 = p1
        self.pino_2 = p2
        self.pwm = PWM(p_pwm)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pino_1, GPIO.OUT)
        GPIO.setup(self.pino_2, GPIO.OUT)
        
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.LOW)

    def frente(self, velocidade=100):
        self.pwm.alterar_velocidade(velocidade)
        GPIO.output(self.pino_1, GPIO.HIGH)
        GPIO.output(self.pino_2, GPIO.LOW)

    def re(self, velocidade=100):
        self.pwm.alterar_velocidade(velocidade)
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.HIGH)

    def freiar(self):
        self.pwm.alterar_velocidade(0)
        GPIO.output(self.pino_1, GPIO.HIGH)
        GPIO.output(self.pino_2, GPIO.HIGH)

    def parar(self):
        self.pwm.alterar_velocidade(0)
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.LOW)  

