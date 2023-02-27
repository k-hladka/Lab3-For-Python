sidesRectangles = []
indexSides = 1
indexRectangles = 1
# Цикл вводу значень
for i in range(6):
    if (indexSides == 1):
        str = "шу"
    if (indexSides == 2):
        str = "гу"

    sidesRectangles.append(float(input(f"Введіть {indexSides}-{str} сторону {indexRectangles}-го прямокутника: ")))
    indexSides += 1

    if (indexSides == 3):
        indexSides = 1
        indexRectangles += 1

def AreaRectangles(arr):
    area1 = arr[0]*arr[1]
    area2 = arr[2]*arr[3]
    area3 = arr[4]*arr[5]
    return area1, area2, area3

area1, area2, area3 = AreaRectangles(sidesRectangles)
print(f"Площа першого прямокутника = {area1} \nПлоща другого прямокутника = {area2} \nПлоща третього прямокутника = {area3}")