class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)    #вызывает метод родительского класса
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
            return self._pages

    @pages.setter
        def pages(self, new_pages: int) -> None:
            """Устанавливает количество страниц в книге."""
            if not isinstance(new_pages, int):
                raise TypeError("Количество страниц должно быть типа int")
            if new_pages <= 0:
                raise ValueError("Количество страниц должно быть положительным числом")
            self._pages = new_pages




class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)   #вызывает метод родительского класса
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность аудиокниги {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
        def duration(self):
            """Возвращает продолжительность аудиокниги."""
            return self._pages


    @pages.setter
    def pages(self, new_duration: int) -> None:
        """Устанавливает продолжительность аудиокниги."""
        if not isinstance(new_duration, (int, float)):
            raise TypeError("Количество страниц должно быть типа int или float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
        self._duration = new_duration

