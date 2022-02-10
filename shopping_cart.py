# shopping_cart.py

## Sales tax rate
## Sending receipts via email
## Integrating with a CSV File Datastore
## Integrating with a google sheets datastore

from datetime import datetime
now = datetime.now()
#date and time syntax came from Programiz: https://www.programiz.com/python-programming/datetime/current-datetime

import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("TAX_RATE"))

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# CLEARS OUT ANY PAST TRANSACTION
matching_products = []

# ALLOWS USER TO ENTER IN ANY INPUTS AND THEN ADDS THE PRODUCT INFO TO LIST

product_ids = [str(product['id']) for product in products]

while True:
    product_input = input('Please input a product identifier: ')
    if product_input.lower() == 'done':
        break
    elif product_input not in product_ids:
        print('Hey, are you sure that product identifier is correct? Please try again!')
    else: 
        for product in products:
            if str(product['id']) == str(product_input):
                matching_products.append(product)



print('\n------------------------------')
print('        Whole Foods')
print('     www.WholeFoods.com')
print('------------------------------')
d1 = now.strftime("%B %d, %Y %H:%M:%S")
print(f'  {d1}  ')
print('------------------------------')
print('Selected Products:')
print('------------------------------')
for match in matching_products:
    print(" ... "+ match['name'] + " (" + str(to_usd(match['price'])) + ")")
print('------------------------------')
prices = []
for match in matching_products:
    prices.append(float(match['price']))
subtotal = sum(prices)
print(f'SUBTOTAL: {to_usd(subtotal)}')
tax_rate = float(os.getenv("TAX_RATE", default = "0.1"))
print("TAX RATE:", tax_rate)
tax = subtotal * tax_rate
print(f'TAX: {to_usd(tax)}')
total = tax + subtotal
print(f'TOTAL: {to_usd(total)}')
print('------------------------------')
print('Thank you for shopping at WF.')
print('------------------------------\n')