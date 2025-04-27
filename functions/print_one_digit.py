
def print_ones_digit(num):
    # Get the ones digit by taking num modulo 10
    ones_digit = num % 10
    # Print the ones digit
    print(f"The ones digit is {ones_digit}")

def main():
    # Ask the user for an integer input
    num = int(input("Enter a number: "))
    # Call the function to print the ones digit
    print_ones_digit(num)

# Run the main function
main()
