from tire.tire import Tire

class BridgestoneTire(Tire):
    def __init__(self, last_tire_service_mileage, current_mileage):
      self.last_tire_service_mileage = last_tire_service_mileage
      self.current_mileage = current_mileage
      
#tires need service every 50000 miles
    def needs_service(self):
      if self.current_mileage - self.last_tire_service_mileage > 50000:
        return True
      else:
        return False