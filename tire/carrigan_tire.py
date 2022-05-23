from tire.tire import Tire

class CarriganTire(Tire):
  def __init__(self, tire_wear, tire_wear_total):
    self.tire_wear = tire_wear
    self.tire_wear_total = tire_wear_total

  def needs_service(self):
    self.tire_wear.sort()
    if self.tire_wear[3] > .9:
      return True
    else:
      return False
