import time
a = int(input("enter time in sec :"))
for x in range(a, 0, -1):
    sec = x % 60
    minute = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02} : {minute:02} : {sec}")
    time.sleep(1)

print("happy new year")
