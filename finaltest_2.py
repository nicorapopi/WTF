while True:
    nums = input("enter number : ")
    if nums == "":
        print("end")
        break
    if not nums.isdigit():
        print("error")
        break
    num = int(nums)
    for i in range(1,13):
        total = num * i
        print(f"{num} x {i} = {total}")