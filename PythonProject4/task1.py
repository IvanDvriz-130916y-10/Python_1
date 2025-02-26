def analyze_numbers(numbers):
    unique_numbers = set(numbers)  # Преобразуем список в множество для получения уникальных значений

    if len(unique_numbers) == 1:
        return "Все числа равны"
    elif len(unique_numbers) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

# Пример использования
input_numbers = input("Введите числа через пробел: ")
numbers_list = list(map(int, input_numbers.split()))  # Преобразуем ввод в список чисел
result = analyze_numbers(numbers_list)
print(result)