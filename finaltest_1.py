while True:
    nums = input("enter number : ")
    if nums == "":
        break

    if "a" in nums or "b" in nums or "c" in nums or "d" in nums or "e" in nums or "f" in nums or "g" in nums or "h" in nums or "i" in nums or "j" in nums or "k" in nums or "l" in nums or "m" in nums or "n" in nums or "o" in nums or "p" in nums or "q" in nums or "r" in nums or "s" in nums or "t" in nums or "u" in nums or "v" in nums or "w" in nums or "x" in nums or "y" in nums or "z" in nums:
        print("error")
        continue
    num = [int(x) for x in nums.split()]
    total = sum(num)
    print(total)