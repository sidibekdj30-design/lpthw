# Here is the number of types of people.
types_of_people = 10 
# The variable x is giving the number of types of people in an affirmative sentence.
x = f"There are {types_of_people} types of people."
# This stores the word "binary" as text
binary = "binary"
# This stores the contraction "don't" as text 
do_not = "don't"
# The variable y is making an affirmation.
y = f"Those who know {binary} and those who {do_not}."
# This shows what's inside  the variable x
print(x)
# This shows what's inside the variable y
print(y) 
# This print stores an "f-string"
print(f"I said: {x}")
# This print stores also another "f-string"
print(f"I also said: '{y}'")
# The variable hilarious stores the boolean value False 
hilarious = False 
# The variable joke evaluation stores a question 
joke_evaluation = "Isn't that joke so funny?! {}"
# The print use another kind of formatting
print(joke_evaluation.format(hilarious))
# This stores an affirmative sentence not finished yet
w = "This is the left side of... "
# This stores a complete affirmative sentence
e = "a string with a right side."
# This links both variables together to make a complete sentence
print(w + e)