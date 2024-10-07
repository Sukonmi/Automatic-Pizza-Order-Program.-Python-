'Welcome to Python Pizza Deliveries'

# Define pizza, pepperoni, and cheese prices
pizza_prices = {
    'Small': 15,
    'Medium': 20,
    'Large': 25
}
pepperoni_prices = {
    'Small': 2,
    'Medium': 3,
    'Large': 5
}
cheese_price = 5

# Prompt user for pizza size
print("Pizza Sizes: Small, Medium, Large")
pizza_size = input("Enter pizza size: ")

# Calculate pizza cost
pizza_cost = pizza_prices[pizza_size]

# Ask for pepperoni
pepperoni = input("Add pepperoni? (yes/no): ")
if pepperoni.lower() == 'yes':
    pepperoni_cost = pepperoni_prices[pizza_size]
else:
    pepperoni_cost = 0

# Ask for cheese
cheese = input("Add cheese? (yes/no): ")
if cheese.lower() == 'yes':
    cheese_cost = cheese_price
else:
    cheese_cost = 0

# Calculate total cost
total_cost = pizza_cost + pepperoni_cost + cheese_cost

# Display order summary
print("\nOrder Summary:")
print(f"Pizza ({pizza_size}): ${pizza_cost}")
if pepperoni_cost > 0:
    print(f"Pepperoni ({pizza_size}): ${pepperoni_cost}")
if cheese_cost > 0:
    print(f"Cheese: ${cheese_cost}")
print(f"Total: ${total_cost}")

