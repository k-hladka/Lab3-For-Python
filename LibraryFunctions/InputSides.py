def Input(count, figure):
    sides = []
    indexSides = 1
    indexFigures = 1
    for i in range(count):
        if (indexSides == 1):
            str = "шу"
        if (indexSides == 2):
            str = "гу"

        sides.append(float(input(f"Введіть {indexSides}-{str} сторону {indexFigures}-го {figure}: ")))
        indexSides += 1

        if (indexSides == 3):
            indexSides = 1
            indexFigures += 1

    return sides