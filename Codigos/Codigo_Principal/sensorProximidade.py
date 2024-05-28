from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=25, trigger=8)

try:
    while True:
        distance = sensor.distance * 100  # Convertendo para centímetros
        print(f"Distância: {distance:.2f} cm")
        sleep(1)  # Aguarda 1 segundo

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")