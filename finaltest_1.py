while True:
    nums = input("enter number : ")
    if nums == "":
        break

    if "a" in nums or "b" in nums or "c" in nums or "d" in nums or "e" in nums or "f" in nums or "g" in nums or "h" in nums or "i" in nums or "j" in nums or "k" in nums or "l" in nums or "m" in nums or "n" in nums or "o" in nums or "p" in nums or "q" in nums or "r" in nums or "s" in nums or "t" in nums or "u" in nums or "v" in nums or "w" in nums or "x" in nums or "y" in nums or "z" in nums \
        or "A" in nums or "B" in nums or "C" in nums or "D" in nums or "E" in nums or "F" in nums or "G" in nums or "H" in nums or "I" in nums or "J" in nums or "K" in nums or "L" in nums or "M" in nums or "N" in nums or "O" in nums or "P" in nums or "Q" in nums or "R" in nums or "S" in nums or "T" in nums or "U" in nums or "V" in nums or "W" in nums or "X" in nums or "Y" in nums or "Z" in nums:
        print("error")
        continue
    num = [int(x) for x in nums.split()]
    total = sum(num)
    print(total)