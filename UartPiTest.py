import serial
import time

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

time.sleep(2)

while True:
    ser.write(b'Hello From Raspberry Pi \n')
    print("sent")
    time.sleep(1)
    if ser.in_waiting>0:
        data = ser.readline().decode('utf-8', errors='ignore').strip()
        print('Received:', data)
        
    time.sleep(1)