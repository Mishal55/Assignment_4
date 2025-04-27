
# Prompt the user to enter a number
curr_value = int(input("Enter a number: "))

# While loop to double the number until it reaches or exceeds 100
while curr_value < 100:
    # Double the current value
    curr_value = curr_value * 2
    
    # Print the current value
    print(curr_value, end=" ")
