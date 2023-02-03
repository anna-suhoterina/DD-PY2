class Book:
    """Базовый класс книги"""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги"""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги"""
        return self._author

    def __str__(self) -> str:
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в бумажной книге"""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц в бумажной книге"""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __str__(self) -> str:
        return f"Бумажная книга '{self.name}'. Автор {self.author}. Количество страниц {self.pages}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Аудиокнига"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги"""
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """Устанавливает продолжительность аудиокниги"""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = duration

    def __str__(self) -> str:
        return f"Аудиокнига '{self.name}'. Автор {self.author}. Продолжительность {self.duration} мин."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

