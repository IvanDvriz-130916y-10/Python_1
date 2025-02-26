def fast_power(a, n):
    if n == 0:
        return 1  # любое число в степени 0 равно 1
    elif n % 2 == 0:
        half_power = fast_power(a, n // 2)  # рекурсивно вычисляем a^(n/2)
        return half_power * half_power  # возвращаем (a^(n/2))^2
    else:
        return a * fast_power(a, n - 1)  # для нечетного n возвращаем a * a^(n-1)

# Пример использования
input_values = input("Введите a и n через пробел: ")
a, n = map(float, input_values.split())  # Преобразуем ввод в числа (a может быть дробным)
n = int(n)  # n должно быть целым числом
result = fast_power(a, n)
print(result)