
def tub_Count(list1: list[int]) -> int:
    result = 0
    for i in list1:
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c == 2:
            result += 1
    return result
list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tub_Count(list1))