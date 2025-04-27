
def print_multiple(message, repeats):
    # Print the message repeats number of times
    for _ in range(repeats):
        print(message)

def main():
    # Ask the user for a message and the number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the print_multiple function
    print_multiple(message, repeats)

# Run the main function
main()
