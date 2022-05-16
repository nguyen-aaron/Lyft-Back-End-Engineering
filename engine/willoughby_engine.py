from engine.engine import Engine

class WilloughbyEngine(Engine):
  def __init__(self, last_engine_service_mileage, current_mileage):
    self.last_engine_service_mileage = last_engine_service_mileage
    self.current_mileage = current_mileage

  def needs_service(self):
    if self.current_mileage - self.last_engine_service_mileage > 60000:
      return True
    else:
      return False