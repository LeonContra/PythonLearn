from random import choice

capital = "Sacramento"

bird = "California Quail"

flower = "California Poppy"

song = "I Love You California"

def randomfunfact():
    funfacts = [
        "California is the home of wetsuits, barbie dolls, and fortune cookies.",
        "The state has more people than Canada.",
        "The weather is perfect for avocados and wine.",
        "There are over 100,000 earthquakes in California each year."
    ]
    
    index = choice("0123")
    
    print(funfacts[int(index)])
    
if __name__ == "__main__":
    randomfunfact()