from LibraryFunctions import InputSides

sidesRectangles = InputSides.Input(6, "прямокутника")
def AreaRectangles(arr):
    area1 = arr[0]*arr[1]
    area2 = arr[2]*arr[3]
    area3 = arr[4]*arr[5]
    return area1, area2, area3

area1, area2, area3 = AreaRectangles(sidesRectangles)
print(f"Площа першого прямокутника = {area1} \nПлоща другого прямокутника = {area2} \nПлоща третього прямокутника = {area3}")