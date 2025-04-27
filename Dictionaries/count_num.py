
# Create an empty dictionary to store the count of each number
num_count = {}

# Keep asking the user for numbers until they press enter without typing anything
while True:
    num_input = input("Enter a number: ")
    
    if num_input == "":  # If the user presses Enter without typing anything, stop the loop
        break
    
    # Convert the input to an integer
    num = int(num_input)
    
    # If the number is already in the dictionary, increment its count
    if num in num_count:
        num_count[num] += 1
    else:
        # Otherwise, add it to the dictionary with a count of 1
        num_count[num] = 1

# Print the count of each number
for num, count in num_count.items():
    print(f"{num} appears {count} times.")
