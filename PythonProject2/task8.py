data = input().strip()

# Инициализация переменной для хранения результата
result = ''

# Переменная для хранения текущего слова
current_word = ''

# Проходим по каждому символу строки
for char in data:
    if char == ' ':
        # Если встречаем пробел, добавляем последнюю букву текущего слова в результат
        if current_word != '':
            result += current_word[-1]
            current_word = ''
    else:
        # Собираем текущее слово
        current_word += char

# Добавляем последнюю букву последнего слова
if current_word != '':
    result += current_word[-1]

print(result)