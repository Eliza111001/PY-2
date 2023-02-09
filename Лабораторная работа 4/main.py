class Household_app:
    def __init__(self, model: str, power: int):
        """
        Базовый класс бытовых электроприборов.
        : param model: название модели
        : param power: мощность электроприбора в Ваттах

        Пример:
        >>> test_household_app = Household_app("LG F2V3GS6W", 3000)
        """
        self.model = model
        self.power = power

    def __str__(self):
        """
        Возвращает название модели, мощность в Ваттах и список доступных режимов работы.
        Examples:
        >>> test_household_app = Household_app("LG F2V3GS6W",3000)
        >>> print(test_household_app)
        Модель"LG F2V3GS6W", мощность 3000 Вт.
        """
        return f"Модель {self.model}, мощность {self.power} Вт"

    def __repr__(self):
        """
        Метод выдаёт строку для инициализации объекта.
        Examples:
        >>> test_household_app = Household_app("LG F2V3GS6W", 3000)
        >>> repr(test_household_app)
        "Household_app(model='LG F2V3GS6W', power=3000)
        """
        return f"{self.__class__.__name__}(model={self.model!r}, power={self.power!r})"

    @property
    def model(self) -> str:
        return self._model

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, power: int) -> None:
        """Устанавливает мощность прибора в Ваттах"""

        if not isinstance(power, int):
            raise TypeError("Значение power должно быть типа int")
        if self.power <= 0:
            raise ValueError("Значение power должно быть положительным")
        self._power = power

    def opinion(self, comment: str):
        """
        Метод позволяет оставить отзыв о модели на сайте.
        :param comment: отзыв
        :return:
        Examples:
        >>> test_household_app = Household_app("LG F2V3GS6W", 3000)
        >>> test_household_app.opinion("Отличная стиральная машина")
        """
        self.comment = comment


class Iron(Household_app):
    """ Дочерний класс бытовой техники - утюг.
    : param model: название модели
    : param power: мощность электроприбора в Ваттах
    : param max_temperature: максимальная температура в градусах Цельсия
    : param min_temperature: минимальная температура в градусах Цельсия
    : param water: возможность заливания воды для отпаривания
    Examples:
    >>> test_household_app = Iron("Loewe Premium Power Station", 1000, 205, 70, "Да")
    """

    def __init__(self, model: str, power: int, max_temperature: int,
                 min_temperature: int, water=("Да", "Нет")):
        super().__init__(model, power)
        self.max_temperature = max_temperature
        self.min_remperature = min_temperature
        self.water = water
        self.opinion = None  # Отзыв по умолчанию отсутствует

    def __str__(self):  # Перегружаем, так как добавляются дополнительные параметры
        """
         Возвращает название модели, мощность в Ваттах,
         максимальную и минимальную температуру в градусах Цельсия,
         возмонжность заливания воды.
         Examples:
         >>> test_iron = Iron("Loewe Premium Power Station", 1000, 205, 70, "Да")
         >>> print(test_iron)
         Модель"Loewe Premium Power Station", мощность 1000 Вт, максимальная температура 205,
         минимальная температура 70, возможность заливания воды - "Да".
         """
        return f"Модель {self.model}, мощность {self.power} Вт, " \
               f"максимальная температура {self.max_temperature}, " \
               f"миммальная температура {self.min_remperature}, " \
               f"возможность заливания воды - {self.water}"

    def __repr__(self) -> str:  # Перегружаем, так как добавляется новый метод
        """
        Метод выдаёт строку для инициализации объекта.
        Examples:
        >>> test_iron = Iron("Loewe Premium Power Station", 1000, 205, 70, "Да")
        >>> repr(test_iron)
        "Iron(model='Loewe Premium Power Station', power=1000,
        max_temperature=205, min_temperature=70, water='Да')
        """
        return f'{self.__class__.__name__}(model={self.model!r}, ' \
               f'power={self.power!r}, water={self.water!r})'

    def add_picture(self):  # Метод перегружен, так как характерен
                            # не для всех бытовых приборов
        """
        Метод позволяет добавить фото результата работы утюга
        :return:
        """


if __name__ == "__main__":
    # Write your solution here
    pass
