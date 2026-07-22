from sys import argv

script, name = argv
# This uses input() to ask for the age while the program is running.
# It combines argv (name from command line ) and input()(age while running)
age = input(f"Hi {name} ! How old are you?")
# This prints a sentence combining both the name from argv and age from input.
print(f"So {name} is {age} years old!")