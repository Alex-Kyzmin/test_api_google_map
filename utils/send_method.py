import allure
import requests

from utils.logger import Logger as Log


class SendMethod:
    """Кастомный класс http методов"""

    headers = {'Content-Type': 'application/json'}

    @staticmethod
    def read(url: str):
        """Классовый метод получение информации по локации"""

        with allure.step('GET'):
            Log.add_request(url, method="READ")
            result = requests.get(
                url,
                headers=SendMethod.headers
            )
            Log.add_response(result)
            return result

    @staticmethod
    def create(url: str, data: dict):
        """Классовый метод создания локации"""

        with allure.step('POST'):
            Log.add_request(url, method="CREATE")
            result = requests.post(
                url,
                headers=SendMethod.headers,
                json=data,
            )
            Log.add_response(result)
            return result

    @staticmethod
    def update(url: str, data: dict):
        """Классовый метод изменения локации"""

        with allure.step('PUT'):
            Log.add_request(url, method="UPDATE")
            result = requests.put(
                url,
                headers=SendMethod.headers,
                json=data,
            )
            Log.add_response(result)
            return result

    @staticmethod
    def delete(url: str, data: dict):
        """Классовый метод удаления локации"""

        with allure.step('DELETE'):
            Log.add_request(url, method="DELETE")
            result = requests.delete(
                url,
                headers=SendMethod.headers,
                json=data,
            )
            Log.add_response(result)
            return result
