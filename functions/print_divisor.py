
def print_divisors(num):
    # Print all divisors of the number from 1 to num
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:  # If i is a divisor of num
            divisors.append(i)
    
    # Print the divisors
    print(f"Here are the divisors of {num}")
    for divisor in divisors:
        print(divisor, end=" ")
    print()  # To ensure the output ends with a new line

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the print_divisors function
    print_divisors(num)

# Run the main function
main()
