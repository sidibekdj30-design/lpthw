# This stores the file name
filename = "test.txt"


print(f"We're to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# This opens the file in write mode because of the 'w'
target = open(filename,'w')

print("Truncating the file. Goodbye!")
# This empties the target 
target.truncate()

print("Now I'm going to ask you for three lines.") 

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# This allows to write lines into your target
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
# This closes your target
target.close()