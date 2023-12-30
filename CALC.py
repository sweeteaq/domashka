def сложение(x, y):
    return x + y

def вычитание(x, y):
    return x - y

def умножение(x, y):
    return x * y

def деление(x, y):
    if y == 0:
        return "Деление на ноль невозможно"
    return x / y

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выйти")

    выбор = input("Введите номер операции (1/2/3/4/5): ")

    if выбор == '5':
        print("До свидания!")
        break

    if выбор in ('1', '2', '3', '4'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if выбор == '1':
            print("Результат:", сложение(num1, num2))
        elif выбор == '2':
            print("Результат:", вычитание(num1, num2))
        elif выбор == '3':
            print("Результат:", умножение(num1, num2))
        elif выбор == '4':
            print("Результат:", деление(num1, num2))
    else:
        print("Некорректный ввод")
