import numpy
from typing import Dict
from .interfaces.driver_handler_interface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def calculate_average(self, numbers: list) -> dict:
        return self.__np.std(numbers)
