# Here is another way to use input() - asking quations and storing answers .
age = input("How old are you? ")
manga = input("What is your favorite manga ? ")
print("I am ", age," my favorite manga is " ,manga )

# Here is another "form" like the one on ex11.py to ask some other questions.
print("Welcom to the Biology Student Form!")
print("Please answer the following questions.\n")

name = input("What is your name?")
university = input("What university do you attend?")
year = input("What year are you in?")
favorite_subject = input("What is your favorite biology subject? ")
goal = input("What is your career goal?")

print(f"\n--- Student Profile---")
print(f"Name:{name}")
print(f"University:{university}")
print(f"Year: {year}")
print(f"Favorite subject: {favorite_subject}")
print(f"Career goal = {goal}")
print(f"\nThank you {name}! good luck with your studies!")