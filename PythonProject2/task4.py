data = input().strip()

if data.isdigit() and int(data) > 0:
    number = int(data)

    # Преобразование в двоичную систему
    binary = ''
    n = number
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    # Преобразование в восьмеричную систему
    octal = ''
    n = number
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8

    # Преобразование в шестнадцатеричную систему
    hex_digits = '0123456789ABCDEF'
    hexadecimal = ''
    n = number
    while n > 0:
        hexadecimal = hex_digits[n % 16] + hexadecimal
        n //= 16

    print(f"{binary}, {octal}, {hexadecimal}")
else:
    print("Неверный ввод")