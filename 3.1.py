from typing import List

def multiply_elements(numbers: List[int], multiplier: int = 2) -> List[int]:
    return [x * multiplier for x in numbers]

multiply_elements_lambda = lambda numbers, multiplier=2: list(map(lambda x: x * multiplier, numbers))

numbers_input = input("Введите список чисел через пробел: ").split()
numbers = [int(x) for x in numbers_input]

multiplier_input = input("Введите множитель (по умолчанию 2): ")
multiplier = int(multiplier_input) if multiplier_input else 2

result_function = multiply_elements(numbers, multiplier)
result_lambda = multiply_elements_lambda(numbers, multiplier)

print(f"Результат (функция): {result_function}")
print(f"Результат (лямбда-функция): {result_lambda}")