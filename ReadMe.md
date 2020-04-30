#Module scrapping price by sku - cdiscount

the module take a sku and return the price from the associated product from cdiscount
you can install it with the commande pip
then import the module in youre script with the commande :

import scrapper as scrapper

and finally launche the function with:

scrapper.parse_price(<your sku>)


The module take the price with tax in the htlm page from the cdiscount page
