#!/user/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
try:
	tag_owner = input('Input who the tag should be assigned to: ')
	print("Place your tag on the scanner to assign owner")
	reader.write(tag_owner)
	print(f"Tag has been assigned to {tag_owner}")
finally:
	GPIO.cleanup()

