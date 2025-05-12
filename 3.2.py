import math


# Функции калькулятора

def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Делитель не может быть нулем!")
    return a / b


def power(a: float, b: float) -> float:
    return a ** b


def factorial(a: int) -> int:
    if a < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    return math.factorial(a)


def sine(a: float) -> float:
    return math.sin(math.radians(a))


def median(values: list) -> float:
    if len(values) == 0:
        raise ValueError("Список не может быть пустым!")
    values.sort()
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]


# Основная логика калькулятора

def calculator():
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Синус")
    print("8. Медиана")

    while True:
        try:
            operation = input("\nВыберите операцию (или 'exit' для выхода): ").strip().lower()

            if operation == 'exit':
                print("Программа завершена.")
                break

            if operation == '1':
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                print(f"Результат: {add(a, b)}")

            elif operation == '2':
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                print(f"Результат: {subtract(a, b)}")

            elif operation == '3':
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                print(f"Результат: {multiply(a, b)}")

            elif operation == '4':
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                print(f"Результат: {divide(a, b)}")

            elif operation == '5':
                a = float(input("Введите основание: "))
                b = float(input("Введите показатель степени: "))
                print(f"Результат: {power(a, b)}")

            elif operation == '6':
                a = int(input("Введите число для вычисления факториала: "))
                print(f"Результат: {factorial(a)}")

            elif operation == '7':
                a = float(input("Введите угол в градусах: "))
                print(f"Результат: {sine(a)}")

            elif operation == '8':
                values = list(map(float, input("Введите числа через пробел: ").split()))
                print(f"Результат: {median(values)}")

            else:
                print("Неверная операция. Пожалуйста, выберите правильную операцию.")

        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


# Запуск калькулятора
calculator()
