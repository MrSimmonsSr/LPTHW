# Simply prints the text
print("I will now count my chickens:")

# Divides 30 by 6 then adds it to 25. Result is a number instead of integrer?
print("Hens:", 25 + 30 / 6)

# First, this line multiplies 25 by 3, giving 75. 
# The 75 is then modulor with 4, which leaves 3.
# The 3 is then subtracted from 100, leaving 97. That is a lot of roosters!
print("Roosters:", 100 - 25 * 3 % 4)

# Just prints text
print("Now I will count the eggs:")
# The first step is the 4 % 2m which results in 0, 
# leaving (3 + 2 + 1 - 5 + 0 - 1 / 4 + 6)
# Then 1 / 4 if evaluated, leaving .25 in that spot:
# (3 + 2 + 1 - 5 + 0 - .25 + 6)
# And the rest of the arithmetic results in: 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# This line just prints
print("Is it true that 3 + 2 < 5 - 7?")

# This should result in False, since 5 is greater than -2
print(3 + 2 < 5 - 7)

# Addition = 5
print("What is 3 + 2?", 3 + 2)

# Subtraction = -2
print("What is 5 - 7?", 5 - 7)

# Prints text
print("Oh, that's why it's False.")

#Prints text
print("How about some more.")

# Should be True
print("Is it greater?", 5 > -2)

# Should also be True
print("Is it greater or equal?", 5 >= -2)

# Should be False
print("Is it less or equal?", 5 <= -2)