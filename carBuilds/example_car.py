from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from tire.michelin_tire import MichelinTire

class ExampleCar(WilloughbyEngine, SpindlerBattery, MichelinTire):
    def needs_service(self):
      if self.battery_should_be_serviced() or self.engine_should_be_serviced() or self.tire_should_be_serviced():
        return True
      else:
        return False