
MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item
        print(removed_item)

# Here's the main function already provided (or similar to what you described):
def main():
    n = int(input("How many elements in your list? "))
    user_list = []
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
    
    shorten(user_list)
    print("Final list:", user_list)

# Run the main function
main()
