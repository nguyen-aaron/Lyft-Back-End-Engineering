from tire.tire import Tire

class MichelinTire(Tire):
    def __init__(self, last_tire_service_mileage, current_mileage):
      self.last_tire_service_mileage = last_tire_service_mileage
      self.current_mileage = current_mileage
      
#tires need service every 80000 miles, Michelin is better than Bridgestone
    def needs_service(self):
      if self.current_mileage - self.last_tire_service_mileage > 80000:
        return True
      else:
        return False