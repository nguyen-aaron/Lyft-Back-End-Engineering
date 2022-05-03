from abc import ABC
from car import Car

class NubbinBattery(Car, ABC):
    def __init__(self, last_battery_service_date, current_year):
        super().__init__(last_battery_service_date)
        self.current_year = current_year
        self.last_battery_service_date = last_battery_service_date

    def battery_should_be_serviced(self):
        return self.current_year - self.last_battery_service_date > 4