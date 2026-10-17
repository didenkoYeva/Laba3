n = int(input("Введіть ціле число n (більше 20): "))
if n > 20:
  for i in range(20, n + 1):
    print(i, end=" ")
else:
  print("Число має бути більше за 20!")
