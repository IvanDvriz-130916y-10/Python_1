data = input().strip()

# Разделяем строку на s и i
s = ''
i = ''
separator_found = False
for char in data:
    if char == ',' and not separator_found:
        separator_found = True
    elif not separator_found:
        s += char
    else:
        i += char

# Инициализация счетчика
count = 0

# Подсчет количества символов i в начале строки s
for char in s:
    if char == i:
        count += 1
    else:
        break

print(count)
