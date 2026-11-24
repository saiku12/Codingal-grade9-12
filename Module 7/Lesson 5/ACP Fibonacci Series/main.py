
# Fibonacci Series using Recursion

# Function to calculate Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Take input from the user
terms = int(input("Enter the number of terms: "))

# Print Fibonacci series
print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")
