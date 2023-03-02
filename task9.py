from task10 import countTime

stringList = input("Введіть список натуральних чисел через пробіл: ")


def fromStringToArray(str):
    intArrayList = []
    arrayList = str.split(' ')
    for i in arrayList:
        intArrayList.append(int(i))
    return intArrayList


def createNewListFromMinToMax(*arr):
    minNumber = min(*arr)
    maxNumber = max(*arr)
    newList = []
    for i in range(minNumber, maxNumber + 1):
        newList.append(i)

    return newList


try:
    intArrayList = fromStringToArray(stringList)
    for i in createNewListFromMinToMax(intArrayList):
        print(i)

except ValueError:
    print("Ви ввели символи невірного типу!")
except BaseException:
    print("Помилка! Спробуйте ввести інші значення в список")


f = countTime(createNewListFromMinToMax)
arrayList = fromStringToArray("1 10")
f(arrayList)
arrayList = fromStringToArray("1 100")
f(arrayList)
arrayList = fromStringToArray("1 1000")
f(arrayList)
arrayList = fromStringToArray("1 10000")
f(arrayList)
arrayList = fromStringToArray("1 100000")
f(arrayList)
arrayList = fromStringToArray("1 1000000")
f(arrayList)