value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         print("am stopping at 5") 
#         break Stops iterating through the rest of the loop and does not trigger the else statement
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5: 
#         print("I love mangos")
#         continue # Only does what is before this continue block then continues iterating
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)
    
# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(4): Starts at 0, stops before 4
#     print(x)
    
# for x in range(2, 4): (Start at 2, stop before 4)
#     print(x)

for x in range(0, 101, 5): # (start at 0, stop before 101, increment by 5)
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")