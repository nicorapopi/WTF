while True:
    num = input("บอกอายุมา : ")
    if num == "":
        break
    if not num.isdigit():
        print("number only")
        continue
    i = 4
    nums = int(num)
    total = nums+ i
    print(f"เดาว่าอีก 4 ปี คุณจะอายุ {total} ขวบ")