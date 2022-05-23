from tire.tire import Tire

class OctoprimeTire(Tire):
  def __init__(self, tire_wear, tire_wear_total):
    self.tire_wear = tire_wear
    self.tire_wear_total = tire_wear_total

  def needs_service(self):
    for x in range (0,4):
      self.tire_wear_total += self.tire_wear[x]
    if self.tire_wear_total > 3:
      return True
    else:
      return False
  
