
def get_first_element(lst):
    # Print the first element of the list
    print(lst[0])

# Now let's collect the list from the user
n = int(input("How many elements in your list? "))

user_list = []
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Call the function
get_first_element(user_list)
