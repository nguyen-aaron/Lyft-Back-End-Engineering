from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from car import Car

def Rosharch(current_year, last_battery_service_date, current_mileage, last_engine_service_mileage):
  engine = WilloughbyEngine(current_mileage, last_engine_service_mileage)
  battery = NubbinBattery(current_year, last_battery_service_date)
  car = Car(engine, battery)
  return car