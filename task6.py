n = int(input("Введіть число n: "))

def searchNaturalNumbers(n):
    number = n-1
    arr = []
    while number:
        if(n%number==0):
            arr.append(number)
        number-=1
    return  arr

print(f"Натуральні числа, які < n і n ділиться на них націло: ")
for i in reversed(searchNaturalNumbers(n)):
    print(i)