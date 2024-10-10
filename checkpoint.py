print("Welcome to Python Pizza Deliveries")

# Define pizza prices
print("pizza_size: Small, Medium, Large")
pizza_size = input("Enter pizza size: \n")

# Calculate pizza cost
if pizza_size == "Small":
    pizza_cost = 15
elif pizza_size == "Medium":
    pizza_cost = 20
else:
    pizza_cost = 25

# Ask for pepperoni
print("Add pepperoni? (yes/no)")
pepperoni = input()
if pepperoni == 'yes':
    if pizza_size == "Small":
        pepperoni_cost = 2
    elif pizza_size == "Medium":
        pepperoni_cost = 3
    else:
        pepperoni_cost = 5
else:
    pepperoni_cost = 0

# Ask for cheese
cheese_price = 5
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



