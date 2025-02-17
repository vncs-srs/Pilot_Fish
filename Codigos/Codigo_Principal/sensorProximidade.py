import RPi.GPIO as GPIO
import time

class SensorProximidade:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        
        # Configuração dos pinos
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, False)
        time.sleep(0.1)  # Pequena pausa para estabilizar

    def medir_distancia(self):
        # Enviar um pulso de 10µs para ativar o sensor
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        inicio_tempo = time.time()
        fim_tempo = time.time()

        # Espera o ECHO ficar alto
        while GPIO.input(self.echo) == 0:
            inicio_tempo = time.time()

        # Espera o ECHO ficar baixo
        while GPIO.input(self.echo) == 1:
            fim_tempo = time.time()

        # Calcula a diferença de tempo
        duracao = fim_tempo - inicio_tempo

        # Converte para distância em cm (velocidade do som = 34300 cm/s)
        distancia = (duracao * 34300) / 2

        return distancia
