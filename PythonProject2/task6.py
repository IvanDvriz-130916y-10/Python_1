data = input().strip()

# Инициализация счетчиков
count_zero = 0
count_one = 0

# Подсчет количества нулей и единиц
for char in data:
    if char == '0':
        count_zero += 1
    elif char == '1':
        count_one += 1

# Проверка на баланс
if count_zero == count_one:
    print("yes")
else:
    print("no")