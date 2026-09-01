#This function adds two numbers and returns the result
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# This function subtracts two numbers and returns the result
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# This function multiplies two numbers and returns the result
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

# This function divides two numbers and returns the result
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b 


# This prints a sentence
print("Let's do some math with just functions!")

# This calls add and stores the result in age
age = add(30, 5)
# This calls subtract and stores the result in height
height = subtract(78, 4)
# This calls multiply and stores the result in weight
weight = multiply(90, 2)
# This calls divide and stores the result in iq
iq = divide(100, 2)

# This prints all the results
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# This combines all four fonctions together using return values
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# This prints the final result of the puzzle
print("That becomes: ",what, "Can you do it by hand?")

# This is a study drill that combines all three functions together using return values
result =subtract(add(24, divide(100,34)), 1023)

# This prints the final result of the study drill
print(f"My {result}")