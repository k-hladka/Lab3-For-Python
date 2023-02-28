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