def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return sum(a-1, b+1)

a = int(input("Input A: "))
b = int(input("Input B: "))

print(sum(a, b))