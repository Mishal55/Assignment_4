
def make_sentence(word, part_of_speech):
    # Check the part_of_speech value and create the corresponding sentence
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech value!")

def main():
    # Ask the user for a word
    word = input("Please type a noun, verb, or adjective: ")
    
    # Ask the user for the part of speech
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the make_sentence function
    make_sentence(word, part_of_speech)

# Run the main function
main()
