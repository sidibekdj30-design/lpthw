# we defined the variables "formatter" with four {}
formatter = "{} {} {} {}"

# we call the function .format() and we give it four arguments
print(formatter.format(1, 2, 3, 4))
# we  can put anything inside even words
print(formatter.format("one", "two", "three", "four"))
# we also put boolean inside
print(formatter.format(True, False, False, True))
# we put words inside
print(formatter.format(formatter, formatter, formatter, formatter))
# we can even put many words
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))