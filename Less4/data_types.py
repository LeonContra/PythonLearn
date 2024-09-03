import math

# String Data Type

# Literal Assignment
first = "John"
last = "Doe"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatination
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a String
decade = str(1990)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple Lines
multiline =  '''
Hey, how are you?   

I was just checking in.   

                            All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                              "
multiline = "                           " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a Menu
title = 'menu'.upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$20".rjust(4))

# String Index Values
print(first[1])
print(first[-1]) #This gets last character in a string
print(first[1:-1]) #Gets all characters between the given values. Last value give is Exclusive
print(first[1:]) #Gets all after the given value. Inclusive

# Some Methods Return Boolean Data
print(first.startswith("J"))
print(first.endswith("Z"))

# Boolean Data Type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

#Numeric Data Types

# Integer Type
price = 100
best_Price = int(80)
print(type(print))
print(isinstance(best_Price, int))

# Float Type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# Complex Type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in Functions for Numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa)) # Round to integer
print(round(gpa, 1)) #Round to decimal

print(math.pi)
print(math.sqrt(4))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a String to a Number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
print(zip_value)

# Error if you Attempt to Cast Incorrect Data
#zip_value = int("New York")
