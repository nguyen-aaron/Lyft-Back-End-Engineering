from battery.battery import Battery

class SpindlerBattery(Battery):
  def __init__(self, last_battery_service_date, current_year):
    self.current_year = current_year
    self.last_battery_service_date = last_battery_service_date

  def needs_service(self):
    if self.current_year - self.last_battery_service_date > 3:
      return True
    else:
      return False