users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptyList = []

print("Dave" in emptyList)

print(users[0])
print(users[-2])

print(users.index('Sara'))
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie' , 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

#del data
data.clear()
print(data)


users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True) #Does modify the list
# print(nums)

print(sorted(nums, reverse=True)) #Does not modify the list
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

numscopy.sort(reverse=True)
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, 'Neil', True])
print(mylist)

# Tuples YOU CANOT MODIFY A TUPLE

mytuple = tuple(('Dave', 42, True))

anothertuple = (1,4,2,8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple #Asterist(*) gets all values in between
print(one)
print(two)
print(hey)

print(anothertuple.count(2))