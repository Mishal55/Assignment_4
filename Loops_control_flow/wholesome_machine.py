
# The affirmation we want the user to type
affirmation = "I am capable of doing anything I put my mind to."

# Loop until the user types the affirmation correctly
while True:
    user_input = input("Please type the following affirmation: ")
    
    # Check if the user's input matches the affirmation
    if user_input == affirmation:
        print("That's right! :)")
        break
    else:
        print("Hmmm That was not the affirmation.")
