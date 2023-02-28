import math

X = float(input("Введіть довжину сторони чотирикутника - X: "))
Y = float(input("Введіть довжину сторони чотирикутника - Y: "))
Z = float(input("Введіть довжину сторони чотирикутника - Z: "))
T = float(input("Введіть довжину сторони чотирикутника - T: "))


def calcArea(sideX, sideY, sideZ, sideT):
    perimetr = (sideX + sideY + sideZ + sideT)/2
    area = math.sqrt((perimetr - sideX) * (perimetr - sideY) * (perimetr - sideZ) * (perimetr - sideT))
    return f"Площа = {area}"

print(calcArea(X, Y, Z, T))
