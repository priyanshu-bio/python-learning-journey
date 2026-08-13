menu =  {"pizza" : 2.50, 'soda' : 0.50, 'chips' : 0.80, 'burger' : 1.50}
cart = []
total = 0

print("------------menu------------" )

for keys, values in menu.items():
    print(f'{keys} : {values}')

while True :
    food = input("select your item (enter q to finish order) :  ")

    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------your oder------")        

for food in cart:
    
    total += menu.get(food)
    print(food, end=',')
    
print()    
print(f'your total = ${total}')    
        
        
