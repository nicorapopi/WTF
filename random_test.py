import random

num = []
for i in range(0,11):
    n = random.randint(1,100)
    num.append(n)
print("จำนวน  " , *num)
print("บวก  " , sum(num))
print("max  " , max(num))
print("min  " , min(num))