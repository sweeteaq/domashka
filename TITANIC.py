import csv

survived_female_count = 0
survived_male_count = 0
with open('train.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for row in csv_reader:
        survived = int(row[1])
        sex = row[4]

        if survived == 1:
            if sex == 'female':
                survived_female_count += 1
            elif sex == 'male':
                survived_male_count += 1

print("Количество выживших женщин:", survived_female_count)
print("Количество выживших мужчин:", survived_male_count)