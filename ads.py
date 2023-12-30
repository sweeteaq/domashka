count_male = 0
count_female = 0
with open('train.csv', 'r') as file:
    file.readline()
    while s := file.readline():
        survivors = s[s.find(',') + 1] == '1'
        if survivors:
            count_male += s.find('male') > 0
            count_female += s.find('female') > 0
print('Количество выживших мужчин = ', count_m)
print('Количество выживших женщин = ', count_f)