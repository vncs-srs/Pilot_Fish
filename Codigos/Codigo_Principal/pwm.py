import RPi.GPIO as GPIO

class PWMControl:
	def __init__(self, pino_pwm):
		self.pino_pwm = pino_pwm
		GPIO.setup(self.pino_pwm,GPIO.OUT)
		self.pwm = GPIO.PWM(self.pino_pwm, 100)
		self.pwm.start(0)
		
	def ajustar_velocidade(self, velocidade):
		self.pwm.ChangeDutyCycle(velocidade)
		
	def parar(self):
		self.pwm.ChangeDutyCycle(0)
		
	def finalizar(self):
		self.pwm.stop()
		
	
