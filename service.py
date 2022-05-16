from abc import ABC, abstractmethod

class Servicing(ABC):
  @abstractmethod
  def needs_service(self):
    pass