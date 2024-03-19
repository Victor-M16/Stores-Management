#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import socket

# Set up the socket for communication (replace 'your_laptop_ip' and 'your_port' with actual values)
#host, port = '192.168.1.188', 8000 #Wongani's laptop
host, port = '192.168.1.152', 8000 #Victor's laptop
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

reader = SimpleMFRC522()

authorised_list = ['Victor','Wongani']

try:
	while True:
		id, tag_owner = reader.read()
		print(f"Scanned ID: {id},")
		

		if any(i == tag_owner for i in authorised_list):
			print(f"{tag_owner} is in the stores")
			
		elif tag_owner == "":
			print(f"A product")
		else:
			print(f"Someone unauthorised is in the stores")

		# Send the scanned data to the laptop
		data = f"{id}"
		s.sendall(data.encode('utf-8'))

finally:
	GPIO.cleanup()
	s.close()

