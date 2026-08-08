foods = []
prices = []
total = 0

while True:
    food = (input("enter a food to buy(q to quit) : "))
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of a {food} : $ "))
        foods.append(food)
        prices.append(price)

print('-------your cart-------')

for food in foods:
    print(food, end=", ")
for price in prices:
    total = total + price
    
print(input(f"makes total of : $ {total}"))
