import unittest
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from tire.michelin_tire import MichelinTire
from tire.bridgestone_tire import BridgestoneTire


class TestNubbinBattery(unittest.TestCase):
  def test_nubbin_battery_should_be_serviced(self):
    last_battery_service_date = 2017
    current_year = 2022
    battery = NubbinBattery(last_battery_service_date, current_year)
    self.assertTrue(battery.needs_service())
      
  def test_nubbin_battery_should_not_be_serviced(self):
    last_battery_service_date = 2021
    current_year = 2022
    battery = NubbinBattery(last_battery_service_date, current_year)
    self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
  def test_spindler_battery_should_be_serviced(self):
    last_battery_service_date = 2019
    current_year = 2022
    battery = SpindlerBattery(last_battery_service_date, current_year)
    self.assertTrue(battery.needs_service())


  def test_spindler_battery_should_not_be_serviced(self):
    current_year = 2022
    last_battery_service_date = 2021
    battery = SpindlerBattery(current_year, last_battery_service_date)
    self.assertFalse(battery.needs_service())


class TestCaputletEngine(unittest.TestCase):
  def test_capulet_engine_should_be_serviced(self):
    last_engine_service_mileage = 0
    current_mileage = 30001
    engine = CapuletEngine(last_engine_service_mileage, current_mileage)
    self.assertTrue(engine.needs_service())

  def test_capulet_engine_should_not_be_serviced(self):
    last_engine_service_mileage = 0
    current_mileage = 29999
    engine = CapuletEngine(last_engine_service_mileage, current_mileage)
    self.assertFalse(engine.needs_service())

    
class TestWilloughbyEngine(unittest.TestCase):
  def test_willoughby_engine_should_be_serviced(self):
    last_engine_service_mileage = 0
    current_mileage = 60001
    engine = WilloughbyEngine(last_engine_service_mileage, current_mileage)
    self.assertTrue(engine.needs_service())

  def test_willoughby_engine_should_not_be_serviced(self):
    last_engine_service_mileage = 0
    current_mileage = 59999
    engine = WilloughbyEngine(last_engine_service_mileage, current_mileage)
    self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
  def test_sternman_engine_should_be_serviced(self):
    warning_light_is_on = True
    engine = SternmanEngine(warning_light_is_on)
    self.assertTrue(engine.needs_service())

  def test_sternman_engine_should_not_be_serviced(self):
    warning_light_is_on = False
    engine = SternmanEngine(warning_light_is_on)
    self.assertFalse(engine.needs_service())

    
class TestMichelinTire(unittest.TestCase):
  def test_michelin_tire_should_be_serviced(self):
    last_tire_service_mileage = 0
    current_mileage = 80001
    tire = MichelinTire(last_tire_service_mileage, current_mileage)
    self.assertTrue(tire.needs_service())

  def test_michelin_tire_should_not_be_serviced(self):
    last_tire_service_mileage = 0
    current_mileage = 79999
    tire = MichelinTire(last_tire_service_mileage, current_mileage)
    self.assertFalse(tire.needs_service())


class TestBridgestoneTire(unittest.TestCase):
  def test_bridgestone_tire_should_be_serviced(self):
    last_tire_service_mileage = 0
    current_mileage = 50001
    tire = BridgestoneTire(last_tire_service_mileage, current_mileage)
    self.assertTrue(tire.needs_service())
    
  def test_bridgestone_tire_should_not_be_serviced(self):
    last_tire_service_mileage = 0
    current_mileage = 4999
    tire = BridgestoneTire(last_tire_service_mileage, current_mileage)
    self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()