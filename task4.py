maximum = 0
number = int(input("Введіть перше число: "))
while number != 0:
    
    if number > maximum:
        maximum = number
        
    number = int(input("Введіть наступне число (або 0 для завершення): "))

print("Найбільший елемент:", maximum)
