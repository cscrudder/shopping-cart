# Shopping Cart Project for Python Class

## Setup

Create a virtual environment:

```sh
conda create -n shopping-env python=3.8
```

Activate the virtual environment:

```sh
conda activate shopping-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Setting up Tax Rate

Create a .env file. It will stay on your laptop, so your information is safe. Open the project file in VS Code. Click the "Explorer" tab in the upper left. Then, in the shopping-cart file, click the "New File" icon. Type ".env" in the box. Open the ".env" file. Type:

```sh
TAX_RATE = 
```
Then, type your jurisdiction's tax rate to the right of the equal sign. For example, a 10% tax rate would be:

```sh
TAX_RATE = .10
```
If you do not select a tax rate, the program will default to 8.725%

## Setting up Email Recipts

In the .env file, type:

```sh
SENDGRID_API_KEY = 
```

Then, go to https://sendgrid.com/

Create an account using the information for your grocery.  On the left column, select the "Settings" tab. Click "API Keys" Copy the key and paste it to the right of the equal sign. For example, an API Key of 123ABC would look like:

```sh
SENDGRID_API_KEY = 123ABC
```

Once you have set up the API key, type:

```sh
SENDER_ADDRESS = 
```

Put the email address associated with your SendGrid account to the right of the equal sign:

```sh
SENDER_ADDRESS = your@email
```

## Usage
This program allow you to enter the 'id' numbers of a the products a customer is purchasing. It then aggregates the purchases, prints a receipt in the terminal and gives the user an option to send an emailed receipt.

To run the program, type:

```sh
python shopping_cart.py
```

