name = "Dave"

count = 1

print(name)

def another():
    color = "blue"
    global count 
    count += 1
    print(count)
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("Dave")
    
another()
print(count)