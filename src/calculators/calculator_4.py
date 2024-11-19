from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def calcular_media(self, numeros: list) -> dict:
        if not numeros or not all(isinstance(num, (int, float)) for num in numeros):
            raise HttpUnprocessableEntityError("Números inválidos")

        media = sum(numeros) / len(numeros)
        resposta = self.__formato_resposta(media)

    def __formato_resposta(self, media: float) -> dict:
        return {"dados": {"Calculator": 4, "media": round(media, 2)}}
