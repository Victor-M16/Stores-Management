

inventory_metrics = {
'P1': {
    'Product': 'Maize',
    'Optimal Order Quantity': 190,
    'Reorder Point': 189.2,
    'Safety Stock': 91.2,
    'Total Cost': 201900.0,
    'Remaining Inventory Stock': 9510
},
'P2': {
    'Product': 'Sugar',
    'Optimal Order Quantity': 186,
    'Reorder Point': 185.8,
    'Safety Stock': 86.0,
    'Total Cost': 81860.0,
    'Remaining Inventory Stock': 3501
},
'P3': {
    'Product': 'Medicine',
    'Optimal Order Quantity': 137,
    'Reorder Point': 136.2,
    'Safety Stock': 66.4,
    'Total Cost': 141370.0,
    'Remaining Inventory Stock': 6651
}
}

# Example queries
product_p2_optimal_order_quantity = inventory_metrics['P2']['Optimal Order Quantity']
product_p3_total_cost = inventory_metrics['P3']['Total Cost']

print(f"Optimal Order Quantity for Product P2: {product_p2_optimal_order_quantity}")
print(f"Total Cost for Product P3: {product_p3_total_cost}")

