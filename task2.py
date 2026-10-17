n = int(input("Введіть кількість днів (n): "))
total_errors = 0
for day in range(1, n + 1):
    m = int(input(f"Введіть кількість помилок за день {day} (m): "))
    total_errors += m  
print(f"Загальна кількість помилок за {n} днів: {total_errors}")
