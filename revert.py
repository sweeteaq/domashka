# Ввод данных от пользователя
month = input("Введите месяц своего рождения: ")
day = int(input("Введите день своего рождения: "))

# Определение знака зодиака
if (month == "Январь" and day >= 20) or (month == "Февраль" and day <= 18):
    zodiac_sign = "Водолей (Aquarius)"
elif (month == "Февраль" and day >= 19) or (month == "Март" and day <= 20):
    zodiac_sign = "Рыбы (Pisces)"
elif (month == "Март" and day >= 21) or (month == "Апрель" and day <= 19):
    zodiac_sign = "Овен (Aries)"
# ... и так далее для всех остальных знаков зодиака ...

# Вывод результата
print(zodiac_sign)
