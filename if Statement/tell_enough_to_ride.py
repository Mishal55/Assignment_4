
# Minimum height requirement
MIN_HEIGHT = 50

while True:
    height_input = input("How tall are you? ")
    
    if height_input == "":
        # If the user presses Enter without typing anything, stop the loop
        break

    height = int(height_input)

    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
