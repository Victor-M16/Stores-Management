import os
import random
import sys
import pytz
import django
import requests

from django.conf import settings
from django.utils import timezone


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

django.setup()


from stock.models import ProductInventory
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for oneport in ports:
    portList.append(str(oneport))
    print(str(oneport))


val = input('Select port COM:')

for x in range(0, len(portList)):
    if portList[x].startswith('COM'+str(val)):
        portVar = "COM"+str(val)
        print(portList[x])


serialInst.baudrate = 115200 #rate at which board will be transmitting the data

serialInst.port = portVar

serialInst.open() #listen for incoming data

while True:

    if serialInst.in_waiting:
        packet = serialInst.readline()
        packet = packet.decode('utf-8').strip()
        print(packet)
        req = requests.get('http://127.0.0.1:8000/stock/product-inventory/')
        print(req)
        try:
            product = ProductInventory.objects.get(sku=packet)
            print(product)
        except:
            pass
