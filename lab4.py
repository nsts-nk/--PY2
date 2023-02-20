
class Car:
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand : Марка автомобиля
        :param load_capacity: Грузоподъемность автомобиля

        """

    def __init__(self, brand: str, load_capacity: int):
        self.brand = brand                  # марка автомобиля
        self.load_capacity = load_capacity  # грузоподъемность автомобиля

    def __str__(self):
        return f"Автомобиль {self.brand}. Грузоподъемность {self.load_capacity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.brand!r}, load_capacity={self.load_capacity!r})"

    def get_max_speed(self, weight: float, speed: int):
        """
        Метод устанавливает максимальную безопасную скорость автомобиля при движении вне населенных пунктах

        :param weight: Масса автомобиля
        :param speed: Допустимая скорость автомобиля
        """
        if not isinstance(weight, float)):
            raise TypeError("Масса автомобиля должна быть типа float")
        if tank_fullness < 0:
            raise ValueError("Масса автомобиля не может быть отрицательным числом")

        if weight >= 3,5:
            speed = 90
        else:
            speed = 110


    def get_min_amount_fuel(self, tank_fullness: float):
        """
        Метод проверяет можно ли по заполненности бака продолжать поездку
        (Не менее четверти бака должно быть заполнено, чтобы соответствующие системы работали исправно)

        :param tank_fullness: Заполненность бака

        """
        if not isinstance(tank_fullness, float)):
            raise TypeError("Заполненность бака должна быть типа float")
        if tank_fullness < 0:
            raise ValueError("Заполненность бака не может быть отрицательным числом")
        if tank_fullness > 1:
            raise ValueError("Заполненность бака не может быть больше 1")

        if tank_fullness > 0,25
            print("Движение можно продолжать")



class Truck(Car):
    """
    Дочерний класс грузового автомобиля.
    :param car_body_space: Объем кузова


    """

    def __init__(self, brand: str, load_capacity: int, car_body_space: float ):
        super().__init__(brand, load_capacity)  # вызывает метод родительского класса
        self.car_body_space = car_body_space

    def __str__(self):
        return f"Автомобиль {self.brand}. Грузоподъемность {self.load_capacity}. Объем кузова{self.car_body_space}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, load_capacity={self.load_capacity!r}, car_body_space{self.car_body_space!r})"

    def get_max_speed(self, weight: float, speed: float):
        """
        Метод вычисляет максимальную безопасную скорость грузового автомобиля при движении вне населенных пунктах. Метод необходимо перегрузить т.к.
        для грузовых автомобилей дейтсвуют другие стандарты скорости

        :param weight: Масса автомобиля
        :param speed: Допустимая скорость автомобиля
        """
        if not isinstance(weight, float)):
            raise TypeError("Масса автомобиля должна быть типа float")
        if tank_fullness < 0:
            raise ValueError("Масса автомобиля не может быть отрицательным числом")

        if weight >= 3,5:
            speed = 60
        else:
            speed = 90

