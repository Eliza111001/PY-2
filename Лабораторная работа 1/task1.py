import doctest


class Book:
    def __init__(self, author: str, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param author: Автор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Толстой Л.Н.", "Война и мир", 1300) # инициализация экземпляра класса
        """
        if not isinstance(author, str):
            raise TypeError("Автор должен быть типа str")
        self.author = author
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages


    # TODO Написать 3 класса с документацией и аннотацией типов
    def get_page(self, page):
        """
        Функция, которая перенаправляет на указанную страницу в книге и копирует текст
        :param page:
        :return: скопированный текст с указанной страницы
        """
        ...
    def laying (self, page):
        """
        Функция, которая позволяет поместить закладку на указанную страницу
        :param page:
        :return: страница с закладкой
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


class Shoes:
    def __init__(self, color: str, brand: str, size: (int, float), quantity: int):
        """
        Создание и подготовка к рабготе объекта Туфли
        :param color: цвет
        :param brand: бренд
        :param size: размер
        :param quantity: количество в наличии
        Примеры:
        >>> shoes = Shoes("pink", "Manolo Blahnik", 37.5, 2) #инициализация экземпляра класса

        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть типа str")
        self.brand = brand
        if not isinstance(size, (int, float)):
            raise TypeError("Размер должен быть типа int или float")
        if size <= 33 or size >= 42:
            raise ValueError("Размеры в наличии с 34 до 41")
        self.size = size
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть типа int")

    def add (self, add_quantity) -> int:
        """
        Функция добавления новых пар туфель
        :param add_quantity:
        :return: добавленное количество

        Примеры:
        >>> shoes = Shoes("pink", "Manolo Blahnik", 37.5, 2)
        >>> shoes.add(3)
        """
        if not isinstance(add_quantity, int):
            raise TypeError("Добавленное количество должно быть типа int")
        ...
    def is_empty(self, quantity) -> bool:
        """
        Функция проверяет, есть ли туфли по данным параметрам в наличии
        :param quantity:
        :return: Есть ли туфли в наличии

        Примеры:
        >>> shoes = Shoes("pink", "Manolo Blahnik", 37.5, 0)
        >>> shoes.is_empty(0)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()

    pass


class Microwave:
    def __init__(self, intensity: {1, 2, 3}, work_time: (int, float)):
        """
        Создание и подготовка к работе объекта Микроволновка
        :param intensity: Интенсивность работы
        :param work_time: Время работы в минутах

        Примеры:
        >>> microwave = Microwave(3, 1.5) #инициализация экземпляра класса
        """
        if not isinstance(intensity, int):
            raise TypeError("Интенсивность должна быть типа int")
        if not intensity == (1, 2, 3):
            raise ValueError("Доступны 3 уровня интенсивности: 1, 2, 3.")
        self.intensity = intensity

        if not isinstance(work_time, (int, float)):
            raise TypeError("Время работы должно быть типа int или float")
        if work_time < 0 or work_time > 240:
            raise ValueError("Время работы должно быть неотрицательным числом, не больше 240.")
        self.work_time = work_time

    def add_time(self, add_time) -> None:
        """
        Функция, позволяющая увеличить доступное время работы микроволновки
        :param add_time:
        Примеры:
        >>> microwave = Microwave(2, 3)
        >>> microwave.add_time(30) #доступное время работы будет увеличено на 30 мин
        """
        if not isinstance(add_time, (int, float)):
            raise TypeError("Время должно быть типа int или float")
        ...

    def eco_intensity(self) -> None:
        """
        Функция режима экономии, убирающая из возможных максимальный режим интенсивности

        Примеры:
        >>> microwave = Microwave(3, 1.5)
        >>> microwave.eco_intensity()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()

    pass