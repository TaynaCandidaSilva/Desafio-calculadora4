from typing import List
from abc import ABC, abstractmethod


class DriverHandlerInterface(ABC):

    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def calculate_average(self, numbers: List[float]) -> float:
        pass
