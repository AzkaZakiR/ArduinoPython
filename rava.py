import pyfirmata
from pyfirmata import Arduino
import time

board = pyfirmata.Arduino('COM4')

led = board.digital[13]

while True:
    led.write(1)
    time.sleep(1)
    led.write(0)
    time.sleep(1)