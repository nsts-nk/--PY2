import doctest


class ElectricKettle:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Электрический чайник"

        :param capacity_volume: Объем чайника
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> electric_kettle = ElectricKettle(250, 250)
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем чайника должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем чайника должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем воды в чайнике должен быть типа int или float")
        if capacity_volume < 0:
            raise ValueError("Объем воды в чайнике не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def add_water_to_kettle(self, water: float):
        """
        Добавление воды в чайник.
        :param water: Объем добавляемой жидкости
        :raise ValueError: Если кол-во добавляемой жидкости превышает оставшееся место в чайнике, то вызываем ошибку

        Примеры:
        >>> electric_kettle = ElectricKettle(250, 100)
        >>> electric_kettle.add_water_to_kettle(100)
        """
        if not isinstance(water, (float, int)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость не может быть отрицательным числом")
        ...
            
    def boil_the_kettle(self, current_temp: float):
        """
        Вскипятить воду в чайнике
        :param current_temp: Текущая температура воды в чайнике
        :return Вскипятилась ли вода в чайнике
        """
        if not isinstance(current_temp, (int, float)):
            raise TypeError("Температура в чайнике должна быть типа int или float")
        ... 
    
    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.
        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Возвращать  ошибку, если объем извлекаемой жидкости больше изначально занятого объема
        :return Объем извлеченной жидкости
        >>> electric_kettle = ElectricKettle(250, 100)
        >>> electric_kettle.remove_water_from_glass(100)
        """
        if not isinstance(estimate_water, (float, int)):
            raise TypeError("Извлекаемая жидкость должна быть типа int или float")
        if estimate_water < 0:
            raise ValueError("Извлекаемая жидкость не может быть отрицательным числом")
        ...
if __name__ == "__main__":
    doctest.testmod()
    pass


class TableLamp:
    def __init__(self, energy_spent: float, incoming_voltage: float ):
        """
        Создание и подготовка к работе объекта "Настольная Лампа"

        :param energy_spent: Расход энергии лампочки
        :param incoming_voltage: Поступающее напряжение

        Примеры:
        >>> tablelamp1 = TableLamp(60, 220)
        """
        if not isinstance(energy_spent, (float,int)):
            raise TypeError("Количество расходуемоой энергии должно быть типа int или float")
        if energy_spent <= 0:
            raise ValueError("Количество раходуемой энергии не может быть отрицательным")
        self.energy_spent = energy_spent

        if not isinstance(incoming_voltage, (float,int)):
            raise TypeError("Поступающее напряжение должно быть типа int или float")
        if energy_spent <= 0:
            raise ValueError("Поступающее напряжение не может быть отрицательным")
        self.incoming_voltage = incoming_voltage

    def is_lamp_on(self) -> bool:
        """
        Функции проверяет выключена ли лампа
        :return: Является ли лампа выключенной

        Примеры:
        >>> tablelamp1 = TableLamp(0,0)
        >>> tablelamp1.is_lamp_on()
        """
        ...
    def how_many_hours_lamp_on(self, lamp_power: int):
        """
        Сколько часов горит лампа
        :param lamp_power: Мощность лампочки (затрачиваемая энергия за 1 час времени)

        Пример:
        >>> tablelamp1 = TableLamp(60, 220)
        >>> tablelamp1.how_many_hours_lamp_on(60)

        """
        if not isinstance(lamp_power, (float, int)):
            raise TypeError("Мощность лампочка должна быть типа int или float")
        if lamp_power <=0:
            raise ValueError("Мощность лампочки должна быть положительна")
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass


class DanceHall:
    def __init__(self, capacity_people: int, current_numbers_people: int):
        """
        Создание и подготовка к работе объекта "Танцевальный зал"
        :param capacity_people: На сколько человек рассчитан зал
        :param current_numbers_people: Текущее количество человек человек в зале

        Примеры:
        >>> dancehall1 = DanceHall(50, 15)
        """
        if not isinstance(capacity_people, int):
            raise TypeError("Вместимость людей в зале должна быть типа int")
        if capacity_people <= 0:
            raise ValueError("Вместимость людей в зале должна быть положительным числом")
        self.capacity_people = capacity_people


        if not isinstance(current_numbers_people, int):
            raise TypeError("Количество людей в зале должно быть типа int")
        if capacity_people <= 0:
            raise ValueError("Количество людей в зале должно быть положительным числом")
        self.current_numbers_people = current_numbers_people

    def is_emty_hall(self) -> bool:
        """
        Функции проверяет пустой ли зал
        :return: Является ли зал пустым

        Примеры:
        >>> dancehall1 = DanceHall(50,3)
        >>> dancehall1.is_emty_hall()
        """
    def add_people_to_hall(self, new_people: int):
        """
        Присоединение новых людей пришедших в зал
        :param new_people: Новые люди пришедшие на тренировку
        :raise ValueError: Если кол-во новых людей превышает вместимость зала, то вызываем ошибку

        Примеры:
        >>> dancehall1 = DanceHall(50,15)
        >>> dancehall1.add_people_to_hall(30)
        """
        if not isinstance(new_people, int):
            raise TypeError("Количество новых людей должно быть типа int")
        if new_people <0:
            raise ValueError("Количество новых людей не должно быть отрицательным")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass