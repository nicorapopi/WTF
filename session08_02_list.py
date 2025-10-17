# list simple 1

# การสร้าง list โดยทั่วไป
mylist = [1,2,3]
print(mylist)
print(type(mylist))


# การแปลง tuple เป็น list
mylist1 = list((1,2,3))
print(mylist1)
print(type(mylist1))

# การแปลง set เป็น list
mylist2 = list({1,2,3})
print(mylist2)
print(type(mylist2))

# การแปลง string เป็น list
mylist3 = list("hello")
print(mylist3)
print(type(mylist3))

mylist = ['python', 'java', 'c++']
print(mylist)

mylist1 = [1,3,4,5,9,8]
print(mylist1)

mylist2 = ["hello",1,False,30,"mall"]
print(mylist2)


# ---------------------------------
# การเข้าถึงข้อมูลใน list

mylist = ['python', 'java', 'c++', 'c#', 'php']
print(mylist[0])   # python
print(mylist[2])   # c++
print(mylist[4])   # php
print(mylist[-1])  # php
print(mylist[-3])  # c++


mylist = ['python', 'java', 'c++', 'c#', 'php']
print(len(mylist))   # 5


mylist = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
print(mylist[1:4])    # ['banana', 'cherry', 'date
print(mylist[:3])     # ['apple', 'banana', 'cherry']
print(mylist[2:])     # ['cherry', 'date', 'fig',
print(mylist[-4:-1])  # ['cherry', 'date', 'fig']
print(mylist[:])      # ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# ---------------------------------
# การตรวจสอบรายการใน list

mylist = ['apple', 'banana', 'cherry']
print('banana' in mylist)   # True
print('grape' in mylist)    # False

if 'apple' in mylist:
    print("apple is in the list")



# ---------------------------------
# การเปลี่ยนแปลงค่าข้อมูลใน list
mylist = ['apple', 'banana', 'grape','papaya','mango']
print(mylist)   # ['apple', 'banana', 'grape','papaya','mango']

mylist[1] = 'pine apple'
print(mylist)   # ['apple', 'pine apple', 'grape','papaya','mango']

mylist[1:3] = ['fruit1', 'fruit2']
print(mylist)   # ['apple', 'fruit1', 'fruit2', 'papaya','mango']

mylist[1:3] = ['fruit']
print(mylist)   # ['apple', 'fruit', 'papaya','mango']


# ---------------------------------
# การ loop for ใน list

mylist = ['papaya', 'mango', 'cherries']
for x in mylist:
    print(x)

# ---------------------------------

mylist = ['papaya', 'mango', 'cherries']
for i in range(len(mylist)):
    print(mylist[i])

# ---------------------------------

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)


# ---------------------------------

newlist = [x for x in fruits if 'a' in x]
print(newlist)

# ---------------------------------
mylist = ['papaya', 'mango', 'cherries']
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1


# ---------------------------------
# เรียงข้อมูลใน list

# เรียงข้อมูลตามลำดับตัวอักษร
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(mylist)
mylist.sort()
print(mylist)



# ---------------------------------
# เรียงข้อมูลตามลำดับตัวเลข
mylist = [100, 50, 65, 82, 23]
print(mylist)
mylist.sort()
print(mylist)


# ---------------------------------
# การเรียวข้อมูลมากไปน้อย
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(mylist)
mylist.sort(reverse=True)
print(mylist)


# ---------------------------------
# การเรียวข้อมูลตัวเลขมากไปน้อย
mylist = [100, 50, 65, 82, 23]
print(mylist)
mylist.sort(reverse=True)
print(mylist)

# ---------------------------------
# การคัดลอก list
mylist = ['apple', 'banana', 'cherry']
print(mylist)
mylist2 = mylist.copy()
print(mylist2)

# ---------------------------------
# การเชื่อมต่อ list โดย +
print(mylist)
print(mylist2)
mylist3 = mylist + mylist2
print(mylist3)

# ---------------------------------
# การเชื่อมต่อโดยใช้ append()
print(mylist)
mylist = ['apple', 'banana', 'cherry']
mylist1 = [10,20,30]
for x in mylist1:
    mylist.append(x)
print(mylist)





# ---------------------------------
# ภาคผนวก
def input_values(prompt): # รับค่า input คั่นด้วยช่องว่าง
    result = [int(tmp) for tmp in input(prompt).split()]
    return result

a = input_values("Enter numbers (space separated): ")
print(a)
print(type(a))



# ---------------------------------
# คำถามทบทวน
# รับตัวเลขเข้ามาทางตคีบอด 10 ชุด แต่ละชุดคั่นด้วยช่องว่าง แล้วนำมาเรียงกันจากน้อยไปมาก และ เรื่ยงจากมากไปน้อย แล้ววนรับข้อมูลชุดใหม่ จนกระทั่งกดเครื่องหมาย \ จึงออกจาก โปรแกรม

while True:
    nums = input("enter number or / to exit: ")
    if nums == '/':
        break
    numlist = [int(x)for x in nums.split()]
    print("น้อยไปมาก: ",sorted(nums))
    print("มากไปน้อย: ",sorted(nums, reverse=True))