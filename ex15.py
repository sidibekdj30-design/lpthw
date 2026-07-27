# This imports the argv tool from the sys module
from sys import argv

# This unpacks argv into 2 variables: script name and filename
script,filename = argv

# This opens the file and stores it in the variable txt
txt = open(filename)

# This prints the name of the file
print(f"Here's your file {filename} :")

# This reads and prints the contents of the file
print(txt.read())

# This tells the user to type the filename again
print("Type the file name again :")

# This shows a prompt and waits for the user to type the filename
file_again = input(">")

# This opens the file again using the name the user typed
txt_again = open(file_again)

# Tis reads and prints the contents of the file a second time
print(txt_again.read())

# This closes the txt
txt.close()

# This closes the txt_again 
txt_again.close()
