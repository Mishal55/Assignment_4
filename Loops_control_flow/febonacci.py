
# Constant for the maximum value
MAX_VALUE = 10000

# Initialize the first two terms of the Fibonacci sequence
fib_0 = 0
fib_1 = 1

# Print the first two terms (Fib(0) and Fib(1))
print(fib_0, fib_1, end=" ")

# Generate the next terms in the Fibonacci sequence until the value exceeds MAX_VALUE
while True:
    # Calculate the next Fibonacci number
    fib_next = fib_0 + fib_1
    
    # If the next Fibonacci number exceeds MAX_VALUE, break the loop
    if fib_next >= MAX_VALUE:
        break
    
    # Print the current Fibonacci number
    print(fib_next, end=" ")
    
    # Update fib_0 and fib_1 for the next iteration
    fib_0 = fib_1
    fib_1 = fib_next
