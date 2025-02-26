side_length = float(input())
# Вычисление периметра
perimeter = 4 * side_length
# Вычисление площади
area = side_length * side_length
# Вычисление диагонали (по теореме Пифагора)
diagonal = (2 ** 0.5) * side_length
# Вывод значений с округлением до 2 знаков
print(f"{perimeter:.2f}, {area:.2f}, {diagonal:.2f}")