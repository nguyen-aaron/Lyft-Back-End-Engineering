from battery.battery import Battery

class NubbinBattery(Battery):
  def __init__(self,last_battery_service_date, current_year):
    self.last_battery_service_date = last_battery_service_date
    self.current_year = current_year

  def needs_service(self):
    if self.current_year - self.last_battery_service_date > 4:
      return True
    else:
      return False
