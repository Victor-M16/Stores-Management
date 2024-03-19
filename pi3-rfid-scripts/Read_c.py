#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import socket

# Set up the socket for communication (replace 'your_laptop_ip' and 'your_port' with actual values)
host, port = '192.168.1.188', 8000 #Wongani
#host, port = '192.168.1.152', 8000 #Victor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

reader = SimpleMFRC522()

try:
    while True:
        id, text = reader.read()
        print(f"Scanned ID: {id},")

        # Send the scanned data to the laptop
        data = f"{id}"
        s.sendall(data.encode('utf-8'))

finally:
    GPIO.cleanup()
    s.close()
