# Variables from line 2 to line to line 4 store strings .
name = "Kadidjatou"
study = "Bioinformatics"
university = "Université Péléforo Gon Coulibaly"

# Print from line 6 to line 17 stores a combines escape sequences and format strings to create a more complex format .
print(f"\tMy name is Sidibé {name} Nanan.")
print(f"\tI am studying {study} now with python on visual code studio.")
print(f"\tI study at the {university} an excellent university.")
print(f"\nMy goals:")
print(f"\t* Become a bioinformatician")
print(f"\t* Work internationally")
print(f"\t* Master python and English")
print("\nKadidjatou, goes at the :\t \"{}\".".format(university))

mum = "\nMy Mum loves {}." 
book = "learnig new things everydays"
print(mum.format(book))