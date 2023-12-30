# Ввод основания системы счисления k
k = int(input("Введите целое число k (2 < k < 9): "))

# Ввод числа n в k-ичной системе счисления
n_str = input("Введите число n в {}-ичной системе: ".format(k))

# Функция для конвертации из k-ичной в десятичную систему
def convert_to_decimal(number_str, base):
    decimal_number = 0
    power = 0
    for digit in reversed(number_str):
        decimal_number += int(digit) * (base ** power)
        power += 1
    return decimal_number

# Конвертируем число n в десятичную систему
decimal_n = convert_to_decimal(n_str, k)

# Функция для проверки, что все цифры числа нечетные
def all_digits_odd(number):
    for digit in str(number):
        if int(digit) % 2 == 0:
            return False
    return True

# Проверяем, что все цифры числа нечетные
result = all_digits_odd(decimal_n)

# Выводим результат проверки и получившееся число
print(decimal_n)
print(result)
