# You just found out that your new dinner table won't arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from exercise 3.6. Add a new line that prints a message saying that you can only invite two people to dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person, letting them know you're sorry you can't invite them to dinner.
# Print a message to each of the two people stil on your list, letting them know they're still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ['snoop dogg', 'matt garstka', 'lex fridman']

print("Good news! There is a larger table that has become available at The Best Restaurant Ever. More guests will be invited!")

guest_list.insert(0, "claudio sanchez",)
guest_list.insert(2, "andrew huberman")
guest_list.append("randall kennedy")

print(f"\nA select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[0].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[1].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[2].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[3].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[4].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[5].title()}! It will be an evening to remember!")

print(f"\nDue to unforseen circumstances regarding availability, I am forced to rescind the invitation. Please look forward to the next invitation {guest_list[5].title()}!")
guest_list.pop(5)
print(f"Due to unforseen circumstances regarding availability, I am forced to rescind the invitation. Please look forward to the next invitation {guest_list[4].title()}!")
guest_list.pop(4)
print(f"Due to unforseen circumstances regarding availability, I am forced to rescind the invitation. Please look forward to the next invitation {guest_list[3].title()}!")
guest_list.pop(3)
print(f"Due to unforseen circumstances regarding availability, I am forced to rescind the invitation. Please look forward to the next invitation {guest_list[2].title()}!")
guest_list.pop(2)

print(f"\nThis will hopefully be the last update to the invitations being sent out for this evening's event. Rest assured, you are still invited {guest_list[0]}!")
print(f"This will hopefully be the last update to the invitations being sent out for this evening's event. Rest assured, you are still invited {guest_list[1]}!")

del guest_list[0]
del guest_list[0]

print(guest_list)