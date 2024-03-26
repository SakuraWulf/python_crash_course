# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the change.
# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

buffet_foods = ('fried rice', 'chicken teriyaki', 'eggrolls', 'wonton soup', 'mongolian beef')
print("\nOriginal buffet foods: ")
for food in buffet_foods:
  print(food.title())

# Type error, since tuples don't support reassignment: buffet_foods[0] = 'white_rice'

buffet_foods = ('white rice', 'chicken teriyaki', 'eggrolls', 'eggdrop soup', 'mongolian beef')
print("\nModified buffet foods: ")
for food in buffet_foods:
  print(food.title())

