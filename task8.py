from LibraryFunctions import searchNumbers

N = int(input("Введіть число N: "))


def searchSimpleNumber(N):
    arr = []
    arrWithFunc = searchNumbers.searchNumber(1, N)
    rangeInFor = N + 1
    for k in range(rangeInFor):
        check = 0
        for j in arrWithFunc:
            if k != j:
                check += 1

        if len(arrWithFunc) == check:
            arr.append(k)
        rangeInFor -= 1

    return arr

def chooseFormat(format, arr):
    match format:
        case "list" : print(str(arr))
        case "string" :
            for i in arr:
                print(i)
        case "countNumbers" : print(len(arr))

print(f"Числа, які є простими з інтервалу [{0}, {N}]")
arr = searchSimpleNumber(N)

print("В форматі списку: ")
chooseFormat("list", arr)

print("В форматі рядку: ")
chooseFormat("string", arr)

print("В форматі виводу кількості елементів: ")
chooseFormat("countNumbers", arr)


