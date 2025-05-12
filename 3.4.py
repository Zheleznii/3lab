from typing import List


class Car:
    manufacturer: str = "Generic"  # Производитель
    category: str = "Sedan"  # Категория автомобиля (например, седан)

    def __init__(self, model: str, year: int, color: str, fuel_type: str, mileage: float) -> None:
        """
        Инициализирует объект автомобиля.

        :param model: Модель автомобиля (строка)
        :param year: Год выпуска автомобиля (целое число)
        :param color: Цвет автомобиля (строка)
        :param fuel_type: Тип топлива (строка, например, "бензин", "дизель")
        :param mileage: Пробег автомобиля (число с плавающей точкой)
        """
        self.model: str = model
        self.year: int = year
        self.color: str = color
        self.fuel_type: str = fuel_type
        self.mileage: float = mileage

    def __str__(self) -> str:
        """Возвращает строковое представление объекта автомобиля."""
        return f"{self.year} {self.model} ({self.color}) - {self.mileage} km"

    def drive(self, distance: float) -> None:
        """Метод для увеличения пробега машины."""
        if distance > 0:
            self.mileage += distance
        else:
            raise ValueError("Distance must be a positive value")

    def change_color(self, new_color: str) -> None:
        """Метод для изменения цвета машины."""
        self.color = new_color

    def is_electric(self) -> bool:
        """Проверяет, является ли автомобиль электрическим."""
        return self.fuel_type.lower() == "electric"

    def __len__(self) -> int:
        """Переопределённый магический метод __len__ для возвращения пробега автомобиля."""
        return int(self.mileage)


# Создание объектов класса
car1 = Car("Tesla Model 3", 2022, "White", "electric", 15000.5)
car2 = Car("BMW X5", 2019, "Black", "diesel", 45000.7)

# Вывод информации об автомобилях
print(car1)
print(car2)

# Вызов методов
car1.drive(500)  # Добавляем пробег
car2.change_color("Blue")  # Меняем цвет

# Проверка типа топлива
print(f"Car1 is electric: {car1.is_electric()}")
print(f"Car2 is electric: {car2.is_electric()}")

# Печать пробега через магический метод __len__
print(f"Car1 mileage using __len__: {len(car1)} km")
print(f"Car2 mileage using __len__: {len(car2)} km")

