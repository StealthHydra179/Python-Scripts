prod = 1
for i in range(1, 1995, 2):
    print(i)
    prod *= i

    prod %= 1000

print("p", prod)