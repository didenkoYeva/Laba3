n = int(input("Введіть число n (до 1000): "))
if n < 10:
    print("Помилка: неправильний інтервал! Число n має бути більшим або дорівнювати 10.")
else:
    for number in range(10, n + 1):
        pod = True
        for digit_char in str(number):
            digit = int(digit_char) 
            if digit == 0 or number % digit != 0:
                pod = False 
                break           
        if pod:
            print(number, end=" ")
            
