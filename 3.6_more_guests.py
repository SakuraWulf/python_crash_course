# You just found a bigger dinner table, so more space is available. Think of three more guests to invite to dinner.
# Start with your program from 3.4 or 3.5. Add a print call to the end of your program, informing people that you found a bigger table. 
# Use insert() to add one new guest to the beginning of your list. 
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitations, one for each guest in your list. 

guest_list = ['snoop dogg', 'matt garstka', 'lex fridman']

print("Good news! There is a larger table that has become available at The Best Restaurant Ever. More guests will be invited!")

guest_list.insert(0, "claudio sanchez",)
guest_list.insert(2, "andrew huberman")
guest_list.append("randall kennedy")

print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[0].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[1].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[2].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[3].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[4].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[5].title()}! It will be an evening to remember!")