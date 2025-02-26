phone_number = input().strip()

# Инициализация переменной для хранения очищенного номера
cleaned_number = ''

# Проходим по каждому символу в строке
for char in phone_number:
    if char.isdigit() or char == '+':
        cleaned_number += char

# Выводим очищенный номер телефона
print(cleaned_number)