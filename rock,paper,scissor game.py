import random

options = ("rock", "paper", "scissor")

running = True



while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("enter your choice (rock,paper,scissors) :-   ")
    print(f"player = {player}")
    print(f"computer = {computer}")  
        
       
            
               

    if player == computer:
                print("its a tie!")

    elif player == 'rock' and computer == 'scissor':
                print("you win!")
    elif player == 'paper' and computer == 'rock':
                print("you wins!")
    elif player == 'scissor' and computer == 'paper':
                print("you win!")

    else:
                print("you loose")




    if not input("try again? (y/n) :-  ").lower() == 'y':
              running= False
print()
print("thanks for playing")
      
