from time import sleep

# In een echte situatie zouden we hier GPIO pins gebruiken
LED_PIN = 13
TEMP_PIN = 0

def read_temperature():
    # Dit is een simulatie van de sensor
    sensor_value = 512  # Dit zou in het echt van de ADC komen
    return sensor_value * (5.0 / 1024.0) * 100

while True:
    temperature = read_temperature()

    if temperature > 25:
        led_status = "ON"
        print("Te warm - LED aan")
    else:
        led_status = "OFF"
        print("Temperatuur OK - LED uit")

    sleep(1)