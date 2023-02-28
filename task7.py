from LibraryFunctions import searchNumbers
M = int(input("Введіть число M: "))
N = int(input("Введіть число N: "))

print(f"Числа, що мають найбільше дільників з інтервалу [{M}, {N}]")
for i in searchNumbers.searchNumber(M, N):
    print(i)
