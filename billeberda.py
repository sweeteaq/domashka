# Ввод размера массива
n = int(input("Введите размер массива: "))

# Инициализация массива
arr = []
for i in range(n):
    arr.append(int(input()))

# Ввод множителя
multiplier = int(input("Введите множитель: "))

# Развернуть массив
for i in range(n // 2):
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

# Поделить каждый элемент массива на множитель
for i in range(n):
    arr[i] = arr[i] // multiplier

# Вывод результата
for i in range(n):
    print(arr[i])
