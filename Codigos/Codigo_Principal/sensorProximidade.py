from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=25, trigger=8)

try:
    while True:
        distance = sensor.distance * 100  
        print(f"Distancia: {distance:.2f} cm")
        sleep(1) 

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuario.")