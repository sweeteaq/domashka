# Ввод данных от пользователя
salary_per_month = int(input("Введите заработную плату в месяц: "))
car_expenses_percent = int(input("Введите сколько процентов уходит на машину: "))
living_expenses_percent = int(input("Введите сколько процентов уходит на жизнь: "))
bonus_per_year = int(input("Введите количество премий за год: "))

# Вычисление суммы, потраченной на машину в год
car_expenses_per_year = (salary_per_month * car_expenses_percent / 100) * 12

# Вычисление суммы, накопленной на пенсию в год
savings_per_year = salary_per_month * 12 - car_expenses_per_year
savings_per_year += (salary_per_month * bonus_per_year) / 2

# Вывод результатов
print("На машину было потрачено: {} рублей".format(car_expenses_per_year))
print("Было накоплено: {} рублей".format(savings_per_year))
