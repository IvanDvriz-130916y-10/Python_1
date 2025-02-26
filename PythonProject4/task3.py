def gcd(a, b):
    if b == 0:
        return a  # Если b равно 0, то НОД(a, b) = a
    else:
        return gcd(b, a % b)  # Рекурсивный вызов с b и остатком от деления a на b

# Пример использования
input_values = input("Введите a и b через пробел: ")
a, b = map(int, input_values.split())  # Преобразуем ввод в целые числа
result = gcd(a, b)
print(result)