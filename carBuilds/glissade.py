from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from car import Car

def Glissade(current_year, last_battery_service_date, current_mileage, last_engine_service_mileage):
  engine = WilloughbyEngine(current_mileage, last_engine_service_mileage)
  battery = SpindlerBattery(current_year, last_battery_service_date)
  car = Car(engine, battery)
  return car