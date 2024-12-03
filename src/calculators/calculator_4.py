from flask import request as FlaskRequest
from ..errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def calculate(self, numbers: list) -> dict:
        if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
            raise HttpUnprocessableEntityError("body mal formatado!")

        average = sum(numbers) / len(numbers)
        response = self.__format_response(average)

        return response

    def __format_response(self, average: float) -> dict:
        return {"data": {"Calculator": 4, "average": round(average, 2)}}
