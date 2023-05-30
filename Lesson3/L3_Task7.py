nums = [1, 1]
n = None
while n is None:
    try:
        n = int(input("Введите номер в ряду Фиббоначи: "))
    except ValueError:
        print("Ошибка ввода!")

if n == 1:
    print(1)
else:
    for i in range(2, n):
        nums.append(nums[i-1] + nums[i-2])

print(nums[n-1])
