#hardware platform: FireBeetle-ESP8266

from machine import Pin
button=Pin(15,Pin.IN)           #create Button object from pin15,Set Pin15 to input (D4)
while True: