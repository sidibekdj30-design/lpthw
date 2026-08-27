# Imports the argv module from python's sys library
from sys import argv

# Unpack the script name and input file from command line arguments
script, input_file = argv

# Defines a function that reads and prints the whole file
def print_all(f):
    print(f.read())

# Defines a function that moves the file read-head back to byte 0
def rewind(f):
    f.seek(0)

# Defines a function that prints a line number and reads one line from the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# We store open() into current_file
current_file = open(input_file)

# This prints a sentence
print("First let's print the whole file:\n")

# This reads and prints the current_file
print_all(current_file)

# This is a sentence
print("Now let's rewind, kind of like a tape.")

# Calls rewind() to move the read-head back to byte 0 of current_file
rewind(current_file)

# This prints a sentence 
print("Let's print three lines:")

# Sets line tracker to 1 and passes it with current_file to print
current_line = 1
print_a_line(current_line, current_file)

# Increments current_line to 2 and prints line 2 of the file
current_line += 1
print_a_line(current_line, current_file)

# Increments current_line to 3 and prints line 3 of the file
current_line += 1
print_a_line(current_line, current_file)