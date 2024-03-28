# Working with one of the programs from 3.4 through 3.7, use len() to print a message indicating the number of people you're inviting to dinner.

guest_list = ['snoop dogg', 'matt garstka', 'lex fridman']

print(f"{guest_list[0].title()}, I am writing to invite you to dinner along with two other distinguished guests i'm sure you'd enjoy spending the evening with.")
print(f"{guest_list[1].title()}, I am writing to invite you to dinner along with two other distinguished guests i'm sure you'd enjoy spending the evening with.")
print(f"{guest_list[2].title()}, I am writing to invite you to dinner along with two other distinguished guests i'm sure you'd enjoy spending the evening with.")

print(f"{len(guest_list)} people will be invited to this dinner." )