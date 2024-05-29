import datetime
import math


class Vehicle:
    def __init__(self, spot_size) -> None:
        self._spot_size = spot_size

    def get_spot_size(self):
        return self._spot_size


class Driver:
    def __init__(self, id, vehicle) -> None:
        self._id = id
        self._vehicle = vehicle
        self._payment_due = 0

    def get_vehicle(self):
        return self._vehicle

    def get_id(self):
        return self._id

    def charge(self, amount):
        self._payment_due += amount


class Car(Vehicle):
    def __init__(self):
        super().__init__(1)


class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)


class SemiTruck(Vehicle):
    def __init__(self):
        super().__init__(3)


class ParkingFloor:
    def __init__(self, spot_count) -> None:
        self._spot = [0] * spot_count
        self._vehicles = {}

    def park_vehicle(self, vehicle):
        for i in range(len(self._spot)):
            if self._spot[i] == 0:
                self._spot[i] = vehicle.get_spot_size()
                return True
        return False

    def remove_vehicle(self, vehicle):
        for i in range(len(self._spot)):
            if self._spot[i] == vehicle.get_spot_size():
                self._spot[i] = 0
                return True
        return False

    def get_parking_spot(self):
        return self._spot

    def get_vehicles(self, vehicle):
        return self._vehicles[vehicle]


class ParkingGarage:
    def __init__(self, floor_count, spots_per_floor) -> None:
        self._parking_floors = [
            ParkingFloor(spots_per_floor) for _ in range(floor_count)
        ]

    def park_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.remove_vehicle(vehicle):
                return True
        return False


class ParkingSystem:
    def __init__(self, parkingGarage, hourlyRate) -> None:
        self._parking_garage = parkingGarage
        self._hourly_rate = hourlyRate
        self._time_parked = {}

    def park_vehicle(self, driver):
        current_hour = datetime.datetime.now().hour
        is_parked = self._parking_garage.park_vehicle(driver.get_vehicle())

        if is_parked:
            self._time_parked[driver.get_id()] = current_hour
        return is_parked

    def remove_vehicle(self, driver):
        is_removed = self._parking_garage.remove_vehicle(driver.get_vehicle())
        if is_removed:
            self._time_parked.pop(driver.get_id())
        return is_removed
