# Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination \t and \n at least once and print the name 4 times to show the changes when using .strip.

name = "  danny  "

print(name)
print(f"\n{name.rstrip()}")
print(name.lstrip())
print(f"\t {name.strip()}")