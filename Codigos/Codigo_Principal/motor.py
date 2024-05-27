import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Motor:
    def __init__(self, p1, p2, p3):
        self.pino_1 = p1
        self.pino_2 = p2
        self.pwm = p3
        
        GPIO.setup(self.pino_1, GPIO.OUT)
        GPIO.setup(self.pino_2, GPIO.OUT)
        GPIO.setup(self.pwm, GPIO.OUT)
        
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.LOW)

    def frente(self):
        GPIO.output(self.pino_1, GPIO.HIGH)
        GPIO.output(self.pino_2, GPIO.LOW)

    def re(self):
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.HIGH)

    def freiar(self):
        GPIO.output(self.pino_1, GPIO.HIGH)
        GPIO.output(self.pino_2, GPIO.HIGH)

    def parar(self):
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.LOW)

    def frente_reduzido(self):
        pwm = GPIO.PWM(self.pino_1, 1000)
        pwm.start(0)
        pwm.ChangeDutyCycle(50)
        GPIO.output(self.pino_2, GPIO.LOW)

    def re_reduzido(self):
        pwm = GPIO.PWM(self.pino_2, 1000)
        pwm.start(0)
        pwm.ChangeDutyCycle(50)
        GPIO.output(self.pino_1, GPIO.LOW)