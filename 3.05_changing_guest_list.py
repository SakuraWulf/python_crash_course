# You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
# Start with your program from 3.4. Add a print call at the end of your program, stating the name of the guest who can't make it.
# Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

guest_list = ['snoop dogg', 'matt garstka', 'lex fridman']

print(f"{guest_list[0].title()} cannot make it to this evening's event.")
del guest_list[0]
guest_list.append('barack obama')

print(f"{guest_list[0].title()}, I am writing to invite you to dinner.")
print(f"{guest_list[1].title()}, I am writing to invite you to dinner.")
print(f"{guest_list[2].title()}, I am writing to invite you to dinner.")