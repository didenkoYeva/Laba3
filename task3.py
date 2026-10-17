n = int(input("Введіть кількість сходинок: "))
for i in range(1, n + 1):
    print(' ' * (n - i) + '#' * i)
