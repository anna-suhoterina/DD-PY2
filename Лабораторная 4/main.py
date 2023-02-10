import doctest


class Fruit:
    def __init__(self, name: str, country: str, weight: int):
        """
        Создание и подготовка к работе объекта "Фрукт"

        :param name: Название фрукта
        :param country: Страна произрастания
        :param weight: Вес в граммах

        Примеры:
        >>> orange = Fruit("Апельсин", "Турция", 320)
        """
        self._name = name  # protected атрибут + getter для предотвращения изменения имени экземпляра
        self.country = country
        self.weight = weight  # добавляем setter с проверками по типу и допустимым значениям

    @property
    def name(self) -> str:
        """Возвращает название фрукта"""
        return self._name

    @property
    def weight(self) -> int:
        """Возвращает вес фрукта"""
        return self._weight

    @weight.setter
    def weight(self, new_weight: int) -> None:
        """Устанавливает вес фрукта в граммах"""
        if not isinstance(new_weight, int):
            raise TypeError("Вес фрукта в граммах должен быть типа int")
        if new_weight <= 0:
            raise ValueError("Вес фрукта должен быть положительным числом")
        self._weight = new_weight

    def find_amount(self, kg: float) -> float:
        """
        Метод, вычисляющий количество фруктов в искомом весе

        :param kg: вес, для которого необходимо вычислить количество фруктов, кг
        :return: количество целых фруктов

        Примеры:
        >>> orange = Fruit("Апельсин", "Турция", 320)
        >>> orange.find_amount(1.5)
        4.0
        """
        if kg <= 0:
            raise ValueError("Вес должен быть положительным числом")

        return kg * 1000 // self.weight

    def find_recipe(self) -> None:
        """
        Метод, который находит рецепт десерта с данным фруктом

        Примеры:
        >>> orange = Fruit("Апельсин", "Турция", 320)
        >>> orange.find_recipe()
        """
        ...

    def __str__(self) -> str:
        return f"Фрукт - {self.name}. Страна произрастания - {self.country}. Вес - {self.weight} г."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, country={self.country!r}, weight={self.weight})"


class Vegetable(Fruit):
    def __init__(self, name: str, country: str, weight: int):
        """
        Создание и подготовка к работе объекта "Овощ"

        :param name: Название овоща
        :param country: Страна произрастания
        :param weight: Вес в граммах

        Примеры:
        >>> tomato = Vegetable("Помидор", "Россия", 180)
        """
        super().__init__(name, country, weight)

    def find_recipe(self) -> None:
        """
        Метод, который находит рецепт салата с данным овощем
        Перегружаем метод, чтобы поменять область поиска рецептов (десерты для овощей не подходят)

        Примеры:
        >>> tomato = Vegetable("Помидор", "Россия", 180)
        >>> tomato.find_recipe()
        """
        ...

    def __str__(self) -> str:
        # Перегружаем метод, чтобы откорректировать строковое представление экземпляра
        return f"Овощ - {self.name}. Страна произрастания - {self.country}. Вес - {self.weight} г."


if __name__ == "__main__":
    doctest.testmod()

