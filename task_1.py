def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

a = int(input("Input A: "))
b = int(input("Input B: "))

print(power(a, b))