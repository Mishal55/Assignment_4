
def count_even(lst):
    # Counting the number of even numbers in the list
    even_count = 0
    
    # Iterate through the list to check each number
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            even_count += 1
    
    # Print the count of even numbers
    print(f"There are {even_count} even numbers in the list.")

def main():
    lst = []
    
    # Populating the list with user input
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop if the user presses enter without typing anything
            break
        else:
            try:
                # Add the integer to the list
                lst.append(int(user_input))
            except ValueError:
                print("Please enter a valid integer.")

    # Call count_even to count the even numbers in the list
    count_even(lst)

# Run the main function
main()
