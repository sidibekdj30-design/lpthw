# This imports the argv tool from the sys module.
from sys import argv

# This unpacks argv into 4 variables: the script name and 3 arguments.
# read the WYSS section for how to run this 
script, first, second, third = argv

# This prints the name of the script that is running.
print("The script is called:", script)
# This prints the first argument the user gave.
print("Your first variable is:", first)
# This prints the second argument the user gave.
print("Your second variable is:", second)
# This prints the third argument the user gave.
print("Your third variable is:", third)