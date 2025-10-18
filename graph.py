import matplotlib.pyplot as plt

x = []
y = []

print("กรอกค่า x และ y อย่างละ 10 ค่า")
for i in range(10):
    a = float(input(f"x[{i+1}] = "))
    b = float(input(f"y[{i+1}] = "))
    x.append(a)
    y.append(b)

plt.plot(x, y, marker='o')
plt.title("x , y")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# pip install matplotlib