
def print_even_odd():
    for i in range(10, 20):
        if i % 2 == 0:
            print(f"{i} even", end=" ")
        else:
            print(f"{i} odd", end=" ")

# Call the function to print the result
print_even_odd()
