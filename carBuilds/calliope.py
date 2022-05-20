from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from car import Car

def Calliope(current_year, last_battery_service_date, current_mileage, last_engine_service_mileage):
  engine = CapuletEngine(current_mileage, last_engine_service_mileage)
  battery = SpindlerBattery(current_year, last_battery_service_date)
  car = Car(engine, battery)
  return car