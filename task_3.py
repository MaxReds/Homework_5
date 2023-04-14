def secondMax():
    second_max = 0
    maximum = 0
    input_num = int(input())
    while input_num != 0:
        if input_num > maximum:
            second_max = maximum
            maximum = input_num
        if input_num > second_max and input_num < maximum:
            second_max = input_num
        input_num = int(input())
    return second_max

print(secondMax())
