# sum of all odd digit from rigt to left and sum of digit sum of even no. * 2 from right to left should be devisible by 10

sum_of_even = 0
sum_of_odd = 0
total = 0

card_num = input("enter your credit card no. :-   ")
card_num = card_num.replace("-", "")
card_num = card_num.replace(" ", "")
card_num = card_num[::-1]

for x in card_num[::2]:
    sum_of_odd += int(x)

for x in card_num[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_of_even += 1 + (x % 10)
    else:
        sum_of_even += x
total = sum_of_even + sum_of_odd
if total % 10 == 0:
        print("valid credit card no.")
else:
        print("invalid credit card no.")
