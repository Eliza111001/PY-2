class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
    @property
    def name(self) -> str:
        return self._name
    @property
    def author(self):
        return self._author

class PaperBook(Book):
    """ Дочерний класс книги """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages!r})'

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц в книге."""

        if not isinstance(pages, int):
          raise TypeError("Значение pages должно быть типа int")
        if self.pages <= 0:
          raise ValueError("Значение pages должно быть положительным")
        self._pages =pages


class AudioBook(Book):
    """ Дочерний класс книги """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})'

    @property
    def duration(self) -> float:
        """Возвращает длительность аудиокниги."""
        return self._duration

    @duration.setter
    def pages(self, duration: float) -> None:
        """Устанавливает количество страниц в книге."""

        if not isinstance(duration, float):
          raise TypeError("Значение duration должно быть типа float")
        if self.duration <= 0:
          raise ValueError("Значение duration должно быть положительным")
        self._duration = duration

