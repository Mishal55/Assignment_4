
def double(num):
    # Return the result of multiplying num by 2
    return num * 2

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the double function and store the result
    result = double(num)
    
    # Print the result
    print(f"Double that is {result}")

# Call the main function to run the program
main()
