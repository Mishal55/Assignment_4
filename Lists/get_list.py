
# Create an empty list
values = []

while True:
    value = input("Enter a value: ")
    if value == "":
        break  # Stop if the user presses enter without typing
    values.append(value)

# Print the final list
print("Here's the list:", values)
