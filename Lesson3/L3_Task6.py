x = None
while x is None:
    try:
        x = int(input("Введите положительное число: "))
    except ValueError:
        print("Ошибка ввода!")
if x == 1:
    print("Простое")
else:
    div_count = 2
    for i in range(2, x):
        if x % i == 0:
            div_count += 1
    if div_count > 2:
        print("Составное")
    else:
        print("Простое")
