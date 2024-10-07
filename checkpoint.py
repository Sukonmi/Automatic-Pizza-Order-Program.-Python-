'Welcome to Python Pizza Deliveries'

# Define pizza, pepperoni, and cheese prices
pizza_prices = {'Small': 15, 'Medium': 20, 'Large': 25}
pepperoni_prices = {'Small': 2, 'Medium': 3, 'Large': 5}
cheese_price = 5

# Prompt user for pizza size
print("Pizza Sizes: Small, Medium, Large")
pizza_size = input("Enter pizza size: \n")

# Calculate pizza cost
pizza_cost = pizza_prices[pizza_size]

# Ask for pepperoni
print("Add pepperoni? (yes/no)")
pepperoni = input()
if pepperoni == 'yes':
    pepperoni_cost = pepperoni_prices[pizza_size]
else:
    pepperoni_cost = 0

# Ask for cheese
print("Add cheese? (yes/no)")
cheese = input()
if cheese == 'yes':
    cheese_cost = cheese_price
else:
    cheese_cost = 0

# Calculate total cost
total_cost = pizza_cost + pepperoni_cost + cheese_cost

# Display order summary
print("\nOrder Summary:")
print("Pizza (" + pizza_size + "): $" + str(pizza_cost))
if pepperoni_cost > 0:
    print("Pepperoni (" + pizza_size + "): $" + str(pepperoni_cost))
if cheese_cost > 0:
    print("Cheese: $" + str(cheese_cost))
print("Total: $" + str(total_cost))


