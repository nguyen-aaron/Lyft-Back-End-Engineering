from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from tire.michelin_tire import MichelinTire
from car import Car

def ExampleCar(current_year, last_battery_service_date, current_mileage, last_engine_service_mileage, last_tire_service_mileage):
  engine = WilloughbyEngine(current_mileage, last_engine_service_mileage)
  battery = SpindlerBattery(current_year, last_battery_service_date)
  tire = MichelinTire(current_mileage, last_tire_service_mileage)
  car = Car(engine, battery, tire)
  return car