from abc import ABC
from car import Car

class MichelinTire(Car, ABC):
    def __init__(self, tire_service_date, current_mileage, last_tire_service_mileage):
        super().__init__(tire_service_date)
        self.current_mileage = current_mileage
        self.last_tire_service_mileage = last_tire_service_mileage

    def tire_should_be_serviced(self):
        return self.current_mileage - self.last_tire_service_mileage > 80000