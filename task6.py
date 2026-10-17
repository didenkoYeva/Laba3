n = int(input("Введіть суму n: "))
all_bills = [64, 32, 16, 8, 4, 2, 1]
result = {}
total_notes = 0
print("Для виплати суми потрібно такі купюри:")
for coin in all_bills:
    if n >= coin:
        count = n // coin 
        n = n % coin
        result[coin] = count
        total_notes += count
        print(f"Купюр номіналом {coin}: {count} шт.")
print(f"Загальна найменша кількість купюр: {total_notes}")
