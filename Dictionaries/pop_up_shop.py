
# Dictionary of fruits and their costs
fruit_prices = {
    "apple": 2.5,
    "durian": 10.0,
    "jackfruit": 5.0,
    "kiwi": 3.0,
    "rambutan": 4.0,
    "mango": 4.5
}

# Initialize total cost
total_cost = 0

# Loop through the fruit prices dictionary and ask the user for each fruit's quantity
for fruit, price in fruit_prices.items():
    quantity = int(input(f"How many ({fruit}) do you want?: "))
    total_cost += quantity * price

# Print the total cost
print(f"Your total is ${total_cost}")
