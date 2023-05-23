from pyfirmata import Arduino, util
import pyfirmata
import time

#ser = Arduino('/dev/tty.usbserial-A6008rIF')
#ser = serial.Serial('COM4',9600)
ser = pyfirmata.Arduino("COM4")  #ganti dengan COM yang sesuai di Arduino

while True:
    ser.digital[13].write(1)
    time.sleep(3)
    ser.digital[13].write(0)
    time.sleep(3)
