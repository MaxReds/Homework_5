def num_count(k, s):
    if k == 1:
        return 1 if s <= 9 else 0
    elif s == 0:
        return 0
    res = 0
    for i in range(min(s, 9), 0, -1):
        res += num_count(k - 1, s - i)
    return res
 
k = int(input())
s = int(input())
print(num_count(k, s))