# TO DO:
## Integrating with a CSV File Datastore
## Integrating with a google sheets datastore

# Import datetime for receipt time.
from datetime import datetime
# date and time syntax came from Programiz: https://www.programiz.com/python-programming/datetime/current-datetime

# Imports os and dotenv to get global variables
import os
from dotenv import load_dotenv

# Import sengrid modules for emailing
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# email syntax came from Prof Rossetti's hints

# Loads global variables
load_dotenv()

import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
SHEET_NAME = os.getenv("SHEET_NAME", default="Products-2021")

#
# AUTHORIZATION
#
# see: https://gspread.readthedocs.io/en/latest/api.html#gspread.authorize
# ... and FYI there is also a newer, more high level way to do this (see the docs)

# an OS-agnostic (Windows-safe) way to reference the "auth/google-credentials.json" filepath:
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google-credentials.json")
print("1")
AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

client = gspread.authorize(credentials)
print("CLIENT:", type(client)) #> <class 'gspread.client.Client'>

#
# READ SHEET VALUES
#
# see: https://gspread.readthedocs.io/en/latest/api.html#client
# ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Spreadsheet
# ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet

print("-----------------")
print("READING DOCUMENT...")

doc = client.open_by_key(DOCUMENT_ID)
print("DOC:", type(doc), doc.title) #> <class 'gspread.models.Spreadsheet'>

sheet = doc.worksheet(SHEET_NAME)
print("SHEET:", type(sheet), sheet.title)#> <class 'gspread.models.Worksheet'>

rows = sheet.get_all_records()
print("ROWS:", type(rows)) #> <class 'list'>

for row in rows:
    print(row) #> <class 'dict'>

#
# WRITE VALUES TO SHEET
#
# see: https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet.insert_row

print("-----------------")
print("NEW ROW...")

auto_incremented_id = len(rows) + 1 # TODO: should change this to be one greater than the current maximum id value
new_row = {
    "id": auto_incremented_id,
    "name": f"Product {auto_incremented_id} (created from my python app)",
    "department": "snacks",
    "price": 4.99,
    "availability_date": "2021-02-17"
}
print(new_row)

print("-----------------")
print("WRITING VALUES TO DOCUMENT...")

# the sheet's insert_row() method wants our data to be in this format (see docs):
new_values = list(new_row.values()) #> [13, 'Product 13', 'snacks', 4.99, '2019-01-01']

# the sheet's insert_row() method wants us to pass the row number where this will be inserted (see docs):
next_row_number = len(rows) + 2 # number of records, plus a header row, plus one

response = sheet.insert_row(new_values, next_row_number)

print("RESPONSE:", type(response)) #> dict
print(response) #> {'spreadsheetId': '____', 'updatedRange': "'Products-2021'!A9:E9", 'updatedRows': 1, 'updatedColumns': 5, 'updatedCells': 5}




# Products given by Prof. Rossetti
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

# Function to format as USD
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

# Creates list of ids of in stock products to use for validation
product_ids = [str(product['id']) for product in products]

# ALLOWS USER TO ENTER IN ANY INPUTS AND THEN ADDS THE PRODUCT INFO TO LIST
while True:
    product_input = input('Please input a product identifier: ')
    # allows user to end input process by typing 'done'
    if product_input.lower() == 'done':
        break
    # validates inputted id based on what's in stock
    elif product_input not in product_ids:
        print('Hey, are you sure that product identifier is correct? Please try again!')
    # appends the item details based on 'id'
    else: 
        for product in products:
            if str(product['id']) == str(product_input):
                matching_products.append(product)


# PRINTS RECEIPT IN TERMINAL
print('\n------------------------------')
print('        Whole Foods')
print('     www.WholeFoods.com')
print('------------------------------')

#Sets and formats time
now = datetime.now()
d1 = now.strftime("%B %d, %Y %H:%M:%S")
print(f'  {d1}  ')
print('------------------------------')
print('Selected Products:')
print('------------------------------')

# Loops through matching_products and prints what the customer bought
for match in matching_products:
    print(" ... "+ match['name'] + " (" + str(to_usd(match['price'])) + ")")
print('------------------------------')

# Creates list of prices. Clears it first.
prices = []
for match in matching_products:
    prices.append(float(match['price']))

# sums the prices
subtotal = sum(prices)

# prints subtotal
print(f'SUBTOTAL: {to_usd(subtotal)}')

# gets tax rate from .env file
tax_rate = float(os.getenv("TAX_RATE", default = "0.0875"))

# calculates and prints tax
tax = subtotal * tax_rate
print(f'TAX: {to_usd(tax)}')

# calculates and prints total
total = tax + subtotal
print(f'TOTAL: {to_usd(total)}')

# prints footer
print('------------------------------')
print('Thank you for shopping at WF.')
print('------------------------------\n')

# requires the user to input 'y' or 'n'
while True:
    # takes user input
    email_yn = input('Would you like your receipt emailed? y/n ')
    # if the user wants an email....
    if email_yn.lower() == 'y':
        # gets the user's email
        email_input = input('What email would you like the receipt to be sent to? ')
        
        # creates formatted list to email out
        html_items_list = ""
        for match in matching_products:
            html_items_list += "<li>" + match['name'] + " (" + str(to_usd(match['price'])) + ") " + "</li>"

        # gets SENGRID info from .env
        SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
        SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

        client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
        print("CLIENT:", type(client))

        # subject of email
        subject = "Your Receipt from Whole Foods"
        
        # content of email
        html_content = html_content = f"""
        <h2>Hello, this is your receipt from Whole Foods.</h2>
        <h3>Date: {now.strftime("%B %d, %Y %H:%M:%S")}</h3>
        <p>Subtotal: {to_usd(subtotal)}</p>
        <p>Tax: {to_usd(tax)}</p>
        <p><h3>Total: {to_usd(total)}</h3></p>
        <p>You ordered:</p>
        <ul>
            {html_items_list}
        </ul>
        """
        print("HTML:", html_content)

        # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
        # ... but we can customize the `to_emails` param to send to other addresses
        message = Mail(from_email=SENDER_ADDRESS, to_emails=email_input, subject=subject, html_content=html_content)

        try:
            response = client.send(message)

            print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
            print(response.status_code) #> 202 indicates SUCCESS
            print(response.body)
            print(response.headers)

        except Exception as err:
            print(type(err))
            print(err)
        break
    elif email_yn.lower()=='n':
        print('Thank you for shopping! Your receipt is printed above and will not be emailed.')
        break
    else: 
        print("Try again, that was not a vaild input.")