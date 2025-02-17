import RPi.GPIO as GPIO
import time

class SensorProximidade:
    def __init__(self):
        #self.trig = 6
        #self.echo = 5
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def medir_distancia(self):
        # Enviar um pulso de 10us
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        inicio_tempo = time.time()
        fim_tempo = time.time()

        # Salva o tempo de envio do pulso
        while GPIO.input(self.echo) == 0:
            inicio_tempo = time.time()

        # Salva o tempo de recepção do pulso
        while GPIO.input(self.echo) == 1:
            fim_tempo = time.time()

        # Calcular a diferença de tempo
        duracao = fim_tempo - inicio_tempo

        # Multiplica pela velocidade do som (34300 cm/s) e divide por 2
        distancia = (duracao * 34300) / 2

        return distancia