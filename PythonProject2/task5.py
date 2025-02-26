domain = input().strip()

# Инициализация списка для хранения частей домена
parts = []
current_part = ''

# Проходим по каждому символу в строке для разделения домена
for char in domain:
    if char == '.':
        parts.append(current_part)
        current_part = ''
    else:
        current_part += char

# Добавляем последнюю часть
parts.append(current_part)

# Выводим каждую часть на новой строке
for part in reversed(parts):
    print(part)