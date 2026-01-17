def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

# Sample number
number = 5

# Function call
result = factorial(number)

# Output
print("Factorial of", number, "is:", result)


Factorial of 5 is: 120
