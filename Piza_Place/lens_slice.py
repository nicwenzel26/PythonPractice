
toppings  = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizzas = zip(prices, toppings)

pizzas = list(pizzas)

print(pizzas)

pizzas.sort()

cheapest_pizza= pizzas[0]
pricest_pizza = pizzas[-1]

cheapest_three = pizzas[0:3]
print(cheapest_three)
