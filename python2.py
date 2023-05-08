import random
number = []
n = int(input("enter list s lengh : "))
while len(number) < n:
    num =random.randint(1,10000)
    if number.count(num)==0:
        number.append(num)
print (number)
