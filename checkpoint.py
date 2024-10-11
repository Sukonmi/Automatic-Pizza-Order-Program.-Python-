print("Welcome to Ayomide's Python Pizza Deliveries")

# Define pizza prices
print("Pizza sizes: Small, Medium, Large")
pizza_size = input("Enter pizza size: \n")

# Calculate pizza cost
if pizza_size.lower() == "small":
    pizza_cost = 15
elif pizza_size.lower() == "medium":
    pizza_cost = 20
else:
    pizza_cost = 25

# Ask for pepperoni
print("Add pepperoni? (yes/no)")
pepperoni = input().lower()
if pepperoni == 'yes':
    if pizza_size.lower() == "small":
        pepperoni_cost = 2
    elif pizza_size.lower() == "medium":
        pepperoni_cost = 3
    else:
        pepperoni_cost = 5
else:
    pepperoni_cost = 0

# Ask for cheese
cheese_price = 5
print("Add cheese? (yes/no)")
cheese = input().lower()
if cheese == 'yes':
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

print("Thank you for your patronage.")


