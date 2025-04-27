
def add_three_copies(lst, data):
    # Adds three copies of data to the list
    lst.append(data)
    lst.append(data)
    lst.append(data)

# Now let's test it
messages = []

# Take user input
message = input("Enter a message to copy: ")

print("List before:", messages)

# Call the function
add_three_copies(messages, message)

print("List after:", messages)
