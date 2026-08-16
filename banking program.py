

balance = 0

running = True

while running:
    print("********************")
    print("WELCOME IN A BANKING PROGRAM")
    print("********************")
    print("1. for show balance")
    print("2. for deposit")
    print("3. for withdraw")
    print("4. exit")
    print("********************")
    choice = input("enter your choice :- ")
    print("********************")
    if choice == "1":
        print(f'your balance is ${balance:.2f}')
        print("********************")
    elif choice == '2':
        amount = (float(input("enter the amount to deposite :-  ")))
        if amount >= 0:
            balance += amount
        else:
            print('enter a valid amount')
            print("********************")
    elif choice == '3':
        amount = (float(input("enter the amount to withdraw :- ")))
        if amount >= balance:
            print("insufficient balance")
        elif amount < balance:
            balance -= amount
        else:
            print("enter a valid amount")
            print("********************")
    elif choice == '4':
        print("thanks for using")
        print("********************")
        running = False
    else:
        print("enter a valid option")
        print("********************")