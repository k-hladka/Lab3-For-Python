from math import sqrt


def searchNumber(M, N):
    arrNumbers = []
    while M <= N:
        count = 0
        rangeInFor = M

        for i in range(rangeInFor):
            if i != 0 and M % i == 0:
                count += 1
            rangeInFor -= 1

            if count > 1:
                arrNumbers.append(M)
                break
            if i >= sqrt(M):
                break
        M += 1

    return arrNumbers
