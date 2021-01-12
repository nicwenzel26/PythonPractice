# Program for practicing strings and prices in Python

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# Price of loveseat
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# Price for settee
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Price for lamp
luxurious_lamp_price = 52.15


# Value for the rate of sales tax
sales_tax = .088


# Customer Interactions

customer_one_total = 0
# Variable to keep track of the items purchased by customer one
customer_one_itemization = ""

# Customer One purchases loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Customer one buys a Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += " " + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:" )
print(customer_one_total)
