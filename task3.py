from math import pow

R = float(input("Введіть радіус: "))
x, y = map(float, input("Введіть координати центра кола x та y: ").split())
p1, p2 = map(float, input("Введіть точки p1 та p2: ").split())
f1, f2 = map(float, input("Введіть точки f1 та f2: ").split())
l1, l2 = map(float, input("Введіть точки l1 та l2: ").split())

def checkDotsInsideCircle(radius, x, y, *dots):
    return 1 if ((pow(x - dots[0], 2) + pow(y - dots[1], 2)) == pow(radius, 2)) else 0

countDots = checkDotsInsideCircle(R, x, y, p1, p2) + checkDotsInsideCircle(R, x, y, f1, f2) + checkDotsInsideCircle(R, x, y, l1, l2)

print(f"Кількість точок, що лежать всередині кола = {countDots}")
