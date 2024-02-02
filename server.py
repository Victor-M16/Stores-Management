import os
import random
import sys
import pytz
import django
import requests

from django.conf import settings
from django.utils import timezone
import socket

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

django.setup()



from stock.models import *
from procurement.models import *


#add your django server's port here.
host, port = '192.168.1.152', 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

def auto_rfq(rfid,product_to_rfq):
    inventory_metrics = {
    'P1': {
        'Product': 'Maize',
        'sku': '566540807600',
        'Optimal Order Quantity': 190,
        'Reorder Point': 189.2,
        'Safety Stock': 91.2,
        'Total Cost': 201900.0,
        'Remaining Inventory Stock': 9510
    },
    'P2': {
        'Product': 'Sugar',
        'sku': '357685595552',
        'Optimal Order Quantity': 186,
        'Reorder Point': 185.8,
        'Safety Stock': 86.0,
        'Total Cost': 81860.0,
        'Remaining Inventory Stock': 3501
    },
    'P3': {
        'Product': 'Vaccine',
        'sku': '772559868266',
        'Optimal Order Quantity': 137,
        'Reorder Point': 136.2,
        'Safety Stock': 66.4,
        'Total Cost': 141370.0,
        'Remaining Inventory Stock': 6651
    }
    
    }

    rfq_metrics = {
    '566540807600': {
        'Product': 'Maize',
        'sku': '566540807600',
        'Optimal Order Quantity': 190,
        'Reorder Point': 189.2,
        'Safety Stock': 91.2,
        'Total Cost': 201900.0,
        'Remaining Inventory Stock': 9510
    },
    '357685595552': {
        'Product': 'Sugar',
        'sku': '357685595552',
        'Optimal Order Quantity': 186,
        'Reorder Point': 185.8,
        'Safety Stock': 86.0,
        'Total Cost': 81860.0,
        'Remaining Inventory Stock': 3501
    },
    '772559868266': {
        'Product': 'Vaccine',
        'sku': '772559868266',
        'Optimal Order Quantity': 137,
        'Reorder Point': 136.2,
        'Safety Stock': 66.4,
        'Total Cost': 141370.0,
        'Remaining Inventory Stock': 6651
    }
    
    }

    rfq_optimum_order_quantity = rfq_metrics[rfid]['Optimal Order Quantity']

    try:
        product_to_rfq = ProductInventory.objects.get(sku=rfid)
        stock_to_rfq = Stock.objects.get(product_inventory = product_to_rfq)

        yrfq = {
            'Product': product_to_rfq.product.name,
            'sku': rfid,
            'Optimal Order Quantity': rfq_optimum_order_quantity,
            'Description': '[RFQ Description]',
            
        }

        

        rfq_set = RFQ.objects.all()

        # Assuming 'rfid', 'product_to_rfq', 'stock_to_rfq', and 'rfq_metrics' are defined elsewhere
        if rfid == product_to_rfq.sku and stock_to_rfq.total_stock <= rfq_metrics[rfid]['Reorder Point']:
            # Check if an RFQ for the same product doesn't already exist
            if not any(i.product == product_to_rfq.product for i in rfq_set):
                # Create an RFQ
                rfq = RFQ.objects.create(
                    product=product_to_rfq.product,
                    description='[RFQ Description]',
                    quantity=rfq_metrics[rfid]['Optimal Order Quantity']
                )


    except:
        print("Error")
        pass

    

    # Example queries
    product_p2_optimal_order_quantity = inventory_metrics['P2']['Optimal Order Quantity']
    product_p3_total_cost = inventory_metrics['P3']['Total Cost']

    #print(f"Optimal Order Quantity for Product P2: {product_p2_optimal_order_quantity}")
    #print(f"Total Cost for Product P3: {product_p3_total_cost}")

print(f"Listening on {host}:{port}")

all_product = ProductInventory.objects.all()
print(all_product)

conn, addr = s.accept()
print(f"Connection established with {addr}")

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")

        # Perform querying logic using the received data and existing queryset
        # For example, if the received data is an ID, filter the queryset
        # with that ID and do something with the result.
        # Replace this logic with your specific requirements.
        # For demonstration purposes, let's assume the data is an ID:
        received_id = data.decode('utf-8')



        filtered_product = ProductInventory.objects.get(sku=received_id)
        print("Filtered Product:", filtered_product)


        try:
            # Retrieve or create the associated Stock object
            filtered_stock, created = Stock.objects.get_or_create(product_inventory=filtered_product)
            print(filtered_stock.total_stock)

            # Adjust total_stock based on the condition
            if filtered_stock.total_stock > 10:
                filtered_stock.total_stock -= 10
                filtered_stock.save()
            else:
                print(f"You are out of stock for {filtered_product}.")

            # Save the changes to the Stock object
                filtered_stock.save()


        except ProductInventory.DoesNotExist:
            print(f" {filtered_product} not found.")
        except Stock.DoesNotExist:
            print(f"Stock not found for {filtered_product}.")



        #auto_rfq
        auto_rfq(received_id,filtered_product)




finally:
    conn.close()