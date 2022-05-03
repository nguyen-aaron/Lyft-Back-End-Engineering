import unittest
from datetime import datetime, date

from engine.carBuilds.calliope import Calliope
from engine.carBuilds.glissade import Glissade
from engine.carBuilds.palindrome import Palindrome
from engine.carBuilds.rorschach import Rorschach
from engine.carBuilds.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_battery_service_date = date.today().year - 3
        current_year = date.today().year
      
        car = Calliope(last_battery_service_date, current_year)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_battery_service_date = date.today().year - 1
        current_year = date.today().year
      
        car = Calliope(last_battery_service_date, current_year)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_engine_service_date = datetime.today().date()
        current_mileage = 30001
        last_engine_service_mileage = 0

        car = Calliope(last_engine_service_date, current_mileage, last_engine_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_engine_service_date = datetime.today().date()
        current_mileage = 30000
        last_engine_service_mileage = 0

        car = Calliope(last_engine_service_date, current_mileage, last_engine_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_battery_service_date = date.today().year - 3
        current_year = date.today().year
      
        car = Glissade(last_battery_service_date, current_year)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_battery_service_date = date.today().year - 1
        current_year = date.today().year
      
        car = Glissade(last_battery_service_date, current_year)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_engine_service_date = datetime.today().date()
        current_mileage = 60001
        last_engine_service_mileage = 0

        car = Glissade(last_engine_service_date, current_mileage, last_engine_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_engine_service_date = datetime.today().date()
        current_mileage = 59999
        last_engine_service_mileage = 0

        car = Glissade(last_engine_service_date, current_mileage, last_engine_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_battery_service_date = date.today().year - 5
        current_year = date.today().year
        warning_light_is_on = False

        car = Palindrome(last_battery_service_date, current_year, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_battery_service_date = date.today().year - 3
        current_year = date.today().year
        warning_light_is_on = False

        car = Palindrome(last_battery_service_date, current_year, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_engine_service_date = datetime.today().date()
        warning_light_is_on = True

        car = Palindrome(last_engine_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_engine_service_date = datetime.today().date()
        warning_light_is_on = False

        car = Palindrome(last_engine_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
      last_battery_service_date = date.today().year - 5
      current_year = date.today().year
      current_mileage = 0
      last_engine_service_mileage = 0
      
      car = Rorschach(last_battery_service_date, current_year, current_mileage, last_engine_service_mileage)
      self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
      last_battery_service_date = date.today().year - 3
      current_year = date.today().year
      current_mileage = 0
      last_engine_service_mileage = 0

      car = Rorschach(last_battery_service_date, current_year, current_mileage, last_engine_service_mileage)
      self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
      last_engine_service_date = datetime.today().date()
      current_mileage = 60001
      last_engine_service_mileage = 0
      
      car = Rorschach(last_engine_service_date, current_mileage, last_engine_service_mileage)
      self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
      last_service_date = datetime.today().date()
      current_mileage = 59999
      last_engine_service_mileage = 0

      car = Rorschach(last_service_date, current_mileage, last_engine_service_mileage)
      self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_year = date.today().year
        last_battery_service_date = date.today().year - 5
        current_mileage = 0
        last_engine_service_mileage = 0

        car = Thovex(last_battery_service_date, current_year, current_mileage, last_engine_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_year = date.today().year
        last_battery_service_date = date.today().year - 3
        current_mileage = 0
        last_engine_service_mileage = 0

        car = Thovex(last_battery_service_date, current_year, current_mileage, last_engine_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_engine_service_date = datetime.today().date()
        current_mileage = 30001
        last_engine_service_mileage = 0

        car = Thovex(last_engine_service_date, current_mileage, last_engine_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_engine_service_date = datetime.today().date()
        current_mileage = 29999
        last_engine_service_mileage = 0

        car = Thovex(last_engine_service_date, current_mileage, last_engine_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()