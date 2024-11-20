from typing import Dict
from .calculator_4 import Calculator4
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

    def test_calculate_average(self):
        mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
        calculate_4 = Calculator4()

        response = calculate_4.calculate(mock_request)

        assert "data" in response
        assert "Calculator" in response["data"]
        assert "average" in response["data"]

    def test_calculate_average_with_error_body(self):
        mock_request = MockRequest(body={"something": 1})
        calculator_4 = Calculator4()

        with raises(Exception) as excinfo:
            calculator_4.calculate(mock_request)
        assert str(excinfo.value) == "Números inválidos"
