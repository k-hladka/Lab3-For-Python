stringList = input("Введіть список натуральних чисел через пробіл: ")
arrayList = stringList.split(' ')


def createNewListFromMinToMax(*arr):
    minNumber = min(*arr)
    maxNumber = max(*arr)
    newList = []
    for i in range(minNumber, maxNumber + 1):
        newList.append(i)

    return newList


try:
    intArrayList = []

    for i in arrayList:
        intArrayList.append(int(i))

    for i in createNewListFromMinToMax(intArrayList):
        print(i)

except ValueError:
    print("Ви ввели символи невірного типу!")
except BaseException:
    print("Помилка! Спробуйте ввести інші значення в список")
