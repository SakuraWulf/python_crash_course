# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, sich as I really love pizza!

pizzas = ['ny_style', 'margerita', 'chicago_style']

for pizza in pizzas:
  print(f"One of my favorite kinds of pizzas is: {pizza.title()}.")

print("I grew up in NYC so naturally, I love NY style pizza.")
print("I haven't had an authentic margerita from Italy but from what i've seen they look amazing and the good ones i've had in the states have been pretty good.")
print("When I was working near Chicago, I had a chance to visit one of their popular joints, \"Giordano\'s.\"")
print("I'm love food so while these styles of pizza came to mind first, I wouldn't mind any kind.")

# I wrote my first for loop today without having to look anything up. Fuck yes! Iteration!
