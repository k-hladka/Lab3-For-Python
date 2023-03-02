from math import sqrt
from task10 import countTime

N = int(input("Введіть число N: "))


def searchSimpleNumber(N):
    arr = []
    index = 1
    while index <= N:
        rangeInFor = index + 1
        count = 0
        for i in range(rangeInFor):
            if i != 0 and index % i == 0 and index != i:
                count += 1
            rangeInFor -= 1
            if count > 1:
                break

            if i >= sqrt(index) and (count == 1 or count == 0):
                arr.append(index)
                break
        index += 1

    return arr


def chooseFormat(format, arr):
    match format:
        case "list":
            print(str(arr))
        case "string":
            for i in arr:
                print(i)
        case "countNumbers":
            print(len(arr))


print(f"Числа, які є простими з інтервалу [{0}, {N}]")
arr = searchSimpleNumber(N)

print("В форматі списку: ")
chooseFormat("list", arr)

print("В форматі рядку: ")
chooseFormat("string", arr)

print("В форматі виводу кількості елементів: ")
chooseFormat("countNumbers", arr)

f = countTime(searchSimpleNumber)
f(10)
f(100)
f(10 ** 3)
f(10 ** 4)
f(10 ** 5)
f(10 ** 6)

