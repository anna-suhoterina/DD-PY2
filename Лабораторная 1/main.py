import doctest
from typing import Union


class Wallet:
    def __init__(self, material: str, money_amount: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Кошелек"

        :param material: Материал, из которого сделан кошелек
        :param money_amount: Количество денег в кошельке

        Примеры:
        >>> wallet = Wallet("Кожа", 7500)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа данных str")
        self.material = material

        if not isinstance(money_amount, (int, float)):
            raise TypeError("Количество денег в кошельке должно быть типа int или float")
        if money_amount < 0:
            raise ValueError("Количество денег в кошельке не может быть отрицательным числом")
        self.money_amount = money_amount

    def take_money_from_wallet(self, take_money: Union[int, float]) -> None:
        """
        Извлечение денег из кошелька.

        :param take_money: Количество извлекаемых денег
        :raise ValueError: Если количество извлекаемых денег превышает количество денег в кошельке,
        то возвращается ошибка.

        Примеры:
        >>> wallet = Wallet("Кожа", 7500)
        >>> wallet.take_money_from_wallet(199.90)
        """
        if not isinstance(take_money, (int, float)):
            raise TypeError("Количество извлекаемых денег должно быть типа int или float")
        if take_money <= 0:
            raise ValueError("Количество извлекаемых денег должно быть положительным числом")
        if take_money > self.money_amount:
            raise ValueError("Недостаточно денег в кошельке")

        self.money_amount -= take_money

    def add_money_to_wallet(self, add_money: Union[int, float]) -> None:
        """
        Добавление денег в кошелек.

        :param add_money: Количество добавляемых денег

        Примеры:
        >>> wallet = Wallet("Кожа", 7500)
        >>> wallet.add_money_to_wallet(3000)
        """
        if not isinstance(add_money, (int, float)):
            raise TypeError("Количество добавляемых денег должно быть типа int или float")
        if add_money <= 0:
            raise ValueError("Количество добавляемых денег должно быть положительным числом")

        self.money_amount += add_money


class Window:
    def __init__(self, height: int, width: int):
        """
        Создание и подготовка к работе объекта "Окно"

        :param height: Высота окна, мм
        :param width: Ширина окна, мм

        Примеры:
        >>> window = Window(2500, 1500)  # инициализация экземпляра класса
        """
        if not isinstance(height, int):
            raise TypeError("Высота окна должна быть целочисленным значением")
        if height <= 0:
            raise ValueError("Высота окна должна быть положительным значением")
        self.height = height

        if not isinstance(width, int):
            raise TypeError("Ширина окна должна быть целочисленным значением")
        if width <= 0:
            raise ValueError("Ширина окна должна быть положительным значением")
        self.width = width

    def close_window(self) -> None:
        """
        Закрытие окна.

        Примеры:
        >>> window = Window(2500, 1500)
        >>> window.close_window()
        """
        ...

    def is_open_window(self) -> bool:
        """
        Функция, которая проверяет, открыто ли окно.

        :return: Является ли окно открытым

        Примеры:
        >>> window = Window(2500, 1500)
        >>> window.is_open_window()
        """
        ...


class Apartment:
    def __init__(self, room_number: int, area: float, location: str):
        """
        Создание и подготовка к работе объекта "Квартира"

        :param room_number: Количество комнат
        :param area: Площадь
        :param location: Адрес

        Примеры:
        >>> apartment = Apartment(2, 58.7, "Невский пр-т, 56")  # инициализация экземпляра класса
        """
        if not isinstance(room_number, int):
            raise TypeError("Количество комнат должно быть типа int")
        if room_number <= 0:
            raise ValueError("Количество комнат должно быть положительным числом")
        self.room_number = room_number

        if not isinstance(area, float):
            raise TypeError("Площадь должна быть типа float")
        if area <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        self.area = area

        if not isinstance(location, str):
            raise TypeError("Адрес должен быть типа str")
        self.location = location

    def is_free_apartment(self) -> bool:
        """
        Функция, которая проверяет, находится ли квартира в продаже.

        :return: Не продана ли квартира

        Примеры:
        >>> apartment = Apartment(2, 58.7, "Невский пр-т, 56")
        >>> apartment.is_free_apartment()
        """
        ...

    def buy_apartment(self, cost: int) -> None:
        """
        Покупка квартиры.

        :param cost: Стоимость квартиры

        Примеры:
        >>> apartment = Apartment(2, 58.7, "Невский пр-т, 56")
        >>> apartment.buy_apartment(10000000)
        """
        if not isinstance(cost, int):
            raise TypeError("Стоимость квартиры должна быть типа int")
        if cost <= 0:
            raise ValueError("Стоимость квартиры должна быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()

