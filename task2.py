from LibraryFunctions import InputSides
import math

triangles = InputSides.Input(4, "трикутника")


def hypotenuse(arr):
    hypotenuse1 = math.sqrt(math.pow(arr[0], 2) + math.pow(arr[1], 2))
    hypotenuse2 = math.sqrt(math.pow(arr[2], 2) + math.pow(arr[3], 2))

    return hypotenuse1, hypotenuse2


hypotenuse1, hypotenuse2 = hypotenuse(triangles)
print(f"Гіпотенуза першого трикутника = {hypotenuse1} \nГіпотенуза другого трикутника = {hypotenuse2}")

maxHypotenuse = "перша" if (hypotenuse1 > hypotenuse2) else "друга"
print(f"Більшою є {maxHypotenuse} гіпотенуза")
