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