import threading
import time


def sensor(numero, temperatura):

    for i in range(5):
        print("Sensor", numero, "-> Temperatura:", temperatura, "°C")
        time.sleep(1)


hilo1 = threading.Thread(target=sensor, args=(1, 30))
hilo2 = threading.Thread(target=sensor, args=(2, 40))
hilo3 = threading.Thread(target=sensor, args=(3, 50))
hilo4 = threading.Thread(target=sensor, args=(4, 60))
hilo5 = threading.Thread(target=sensor, args=(5, 70))


hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()


hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()
hilo5.join()


print("Todos los sensores terminaron")