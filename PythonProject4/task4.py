def can_form_palindrome(s):
    char_count = {}

    # Подсчитываем количество вхождений каждого символа
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Проверяем количество символов с нечетным количеством вхождений
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    if odd_count > 1:
        return None  # Невозможно составить палиндром

    # Составляем палиндром
    half_palindrome = []
    middle_char = ""

    for char, count in char_count.items():
        if count % 2 != 0:
            middle_char = char  # Сохраняем символ с нечетным количеством
        half_palindrome.append(char * (count // 2))  # Добавляем половину символов

    # Объединяем половину и формируем палиндром
    first_half = ''.join(half_palindrome)
    palindrome = first_half + middle_char + first_half[::-1]

    return palindrome

input_string = input("Введите строку: ")
result = can_form_palindrome(input_string)
if result:
    print(result)
else:
    print("Невозможно составить палиндром из данной строки.")