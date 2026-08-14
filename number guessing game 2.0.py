import random


low = 0
high = 100
number = random.randint(low, high)
guesses = 0



while True:
    

    guesst = input(f"guess a no. between {low} - {high}:-   ")
    
   
    if not guesst.isdigit() :
        print(f"enter a valid number between {low} - {high}")
        continue
    guess = int(guesst)
    guesses += 1
   

    
        
    if guess > number:
            
        print(f"{guess} is too high" )
    elif guess < number:
         print(f"{guess} is too low" )

        
    else:
        
        print()    
        print(f"you guess the correct number with {guesses} guesses")
        break














                  
