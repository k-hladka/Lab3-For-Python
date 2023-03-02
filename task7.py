from LibraryFunctions import searchNumbers
from task10 import countTime

M = int(input("Введіть число M: "))
N = int(input("Введіть число N: "))

print(f"Числа, що мають найбільше дільників з інтервалу [{M}, {N}]")
for i in searchNumbers.searchNumber(M, N):
    print(i)

f = countTime(searchNumbers.searchNumber)
f(1, 10)
f(1, 100)
f(1, 10**3)
f(1, 10**4)
f(1, 10**5)
f(1, 10**6)