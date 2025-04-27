
import random

# DONE_LIKELIHOOD represents the likelihood of done() returning True
DONE_LIKELIHOOD = 0.3  # 30% chance of stopping the count early

# done() function that has a chance of returning True based on DONE_LIKELIHOOD
def done():
    return random.random() < DONE_LIKELIHOOD

# chaotic_counting function
def chaotic_counting():
    for i in range(1, 11):  # Count from 1 to 10
        if done():  # Check if done() returns True
            return  # Stop the counting and exit the function
        print(i, end=" ")  # Print the current number

# main function
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Call the chaotic counting function
    print("I'm done.")  # Print when done

# Call main
main()
