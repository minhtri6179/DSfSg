from enum import Enum


class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    ELECTRIC = 3
    VAN = 4
    MOTORBIKE = 5


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person:
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
