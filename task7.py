M = int(input("Введіть число M: "))
N = int(input("Введіть число N: "))


def searchNumber(M, N):
    arrNumbers = []
    while M <= N:
        rangeInFor = M
        count = 0

        for i in range(rangeInFor):
            if M % rangeInFor == 0:
                count += 1
            rangeInFor -= 1

        if count > 2:
            arrNumbers.append(M)
        M += 1

    return arrNumbers

print(f"Числа, що мають найбільше дільників з інтервалу [{M}, {N}]")
for i in searchNumber(M, N):
    print(i)
