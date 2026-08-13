import random


low = 0
high = 100
number = random.randint(low, high)
guesses = 0


while True:
    guess = int(input(f"guess a no. between 0-100:-   "))
    guesses += 1


    if guess > number:
        print(f"{guess} is too high" )
    elif guess < number:
        print(f"{guess} is too low" )

        
    else:
        print(f"you guess the correct number with {guesses} guesses")
        break














                  
